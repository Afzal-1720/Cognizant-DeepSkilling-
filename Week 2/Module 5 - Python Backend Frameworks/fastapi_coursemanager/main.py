from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import BackgroundTasks
from database import engine, Base, get_db
from models import Department, Course
from schema import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
    EnrollmentCreate,
)
from fastapi import Body
from fastapi import Response
from sqlalchemy import or_
from security import get_password_hash

from models import User

from schema import UserRegister
from auth import create_access_token
from security import verify_password
from schema import UserLogin
from models import User
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from auth import SECRET_KEY, ALGORITHM
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(

    title="Course Management API",

    description="Course Management Backend using FastAPI",

    version="1.0.0",

    contact={

        "name":"Muhammad Afzal",

        "email":"afzal@example.com"

    },
    license_info={
        "name": "MIT"
    }

)
app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)

from fastapi.responses import JSONResponse


def error_response(

    code,

    message,

    field=None

):

    return JSONResponse(

        status_code=404,

        content={

            "error":{

                "code":code,

                "message":message,

                "field":field

            }

        }

    )

def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")

@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post(
    "/api/v1/auth/login",
    tags=["Authentication"]
)
async def login(
    user: UserLogin,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(User).where(
            User.email == user.email
        )
    )

    db_user = result.scalar_one_or_none()

    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        user.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(
        {"sub": db_user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):

    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid or expired token"
    )

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    result = await db.execute(
        select(User).where(
            User.email == email
        )
    )

    user = result.scalar_one_or_none()

    if user is None:
        raise credentials_exception

    return user


@app.get("/")
async def root():
    return {
        "message": "API running"
    }


from fastapi import Response, status

@app.post(
    "/api/v1/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create a new course",
    response_description="Course created successfully"
)
async def create_course(
    course: CourseCreate,
    response: Response,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)

    # Add Location header
    response.headers.append(
    "Location",
    f"/api/courses/{new_course.id}"
)

    return new_course


@app.get(
    "/api/v1/courses/",
    tags=["Courses"],
    summary="Get all courses with pagination and search"
)
async def get_courses(

    page: int = 1,
    page_size: int = 2,
    search: str | None = None,

    db: AsyncSession = Depends(get_db)

):

    # Base query
    query = select(Course)

    # Search by course name or course code
    if search:
        query = query.where(
            or_(
                Course.name.ilike(f"%{search}%"),
                Course.code.ilike(f"%{search}%")
            )
        )

    # Get total matching records
    total_result = await db.execute(query)
    total_courses = total_result.scalars().all()
    total_count = len(total_courses)

    # Pagination
    offset = (page - 1) * page_size

    result = await db.execute(
        query.offset(offset).limit(page_size)
    )

    courses = result.scalars().all()

    # Previous page URL
    previous = None
    if page > 1:
        previous = (
            f"/api/v1/courses/?page={page-1}"
            f"&page_size={page_size}"
        )

    # Next page URL
    next_page = None
    if offset + page_size < total_count:
        next_page = (
            f"/api/v1/courses/?page={page+1}"
            f"&page_size={page_size}"
        )

    return {
        "count": total_count,
        "next": next_page,
        "previous": previous,
        "results": courses
    }


from fastapi.responses import JSONResponse

@app.get(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
async def get_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Course).where(
            Course.id == course_id
        )
    )

    course = result.scalar_one_or_none()

    # Standardized error response
    if course is None:
        return JSONResponse(
            status_code=404,
            content={
                "error": {
                    "code": "NOT_FOUND",
                    "message": f"Course with id {course_id} does not exist",
                    "field": None
                }
            }
        )

    return course

from fastapi import status

@app.put(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,
    status_code=status.HTTP_200_OK,
     tags=["Courses"]
)
async def update_course(
    course_id: int,
    course_data: CourseUpdate,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    if course_data.name is not None:
        course.name = course_data.name

    if course_data.code is not None:
        course.code = course_data.code

    if course_data.credits is not None:
        course.credits = course_data.credits

    if course_data.department_id is not None:
        course.department_id = course_data.department_id

    await db.commit()

    await db.refresh(course)

    return course

@app.delete(
    "/api/v1/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT, tags=["Courses"]
)
async def delete_course(

    course_id: int,

    current_user: User = Depends(get_current_user),

    db: AsyncSession = Depends(get_db)

):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    await db.delete(course)

    await db.commit()

from models import Student, Enrollment
@app.get("/api/v1/courses/{course_id}/students",tags=["Students"])
async def get_course_students(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Student)
        .join(
            Enrollment,
            Student.id == Enrollment.student_id
        )
        .where(
            Enrollment.course_id == course_id
        )
    )

    students = result.scalars().all()

    return students

@app.post(
    "/api/v1/enrollments/",
    tags=["Enrollments"]
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(
        send_confirmation_email,
        enrollment.student_email
    )

    return {
        "message": "Enrollment created successfully"
    }


@app.patch(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"],
    summary="Partially update a course"
)
async def patch_course(
    course_id: int,
    course_data: CourseUpdate = Body(...),
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    update_data = course_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(course, key, value)

    await db.commit()
    await db.refresh(course)

    return course

@app.post(
    "/api/v1/auth/register",
    tags=["Authentication"]
)
async def register_user(

    user: UserRegister,

    db: AsyncSession = Depends(get_db)

):

    result = await db.execute(
        select(User).where(
            User.email == user.email
        )
    )

    existing_user = result.scalar_one_or_none()

    if existing_user:

        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    hashed_password = get_password_hash(
        user.password
    )

    new_user = User(

        email=user.email,

        hashed_password=hashed_password,

        is_active=True

    )

    db.add(new_user)

    await db.commit()

    await db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }



"""
API Versioning Strategies

1. URL Versioning
Example:
    /api/v1/courses/
    /api/v2/courses/

Advantages:
- Easy to understand
- Easy to test
- Most commonly used

2. Header Versioning

Accept: application/json;version=1

Advantages:
- Clean URLs
- Useful for enterprise APIs

For this project, URL Versioning is used.
"""

"""
OAuth2 Authorization Code Flow

1. User logs into the application.

2. Authorization Server verifies credentials.

3. Server returns an Authorization Code.

4. Client exchanges the Authorization Code for an Access Token.

5. Client sends the Access Token in the Authorization header.

6. Protected endpoints validate the JWT before allowing access.

Difference from this project:

This project uses simple JWT Login.
The client sends email and password directly to the server.
The server immediately returns a JWT.

OAuth2 Authorization Code Flow is more secure because
the client never handles the user's password after login
and supports third-party authentication providers such as
Google, Microsoft and GitHub.
"""