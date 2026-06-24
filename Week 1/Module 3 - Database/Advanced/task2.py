from sqlalchemy.orm import sessionmaker
from task1 import (
    engine,
    Department,
    Student,
    Course,
    Enrollment
)

Session = sessionmaker(bind=engine)
session = Session()

cs = Department(
    dept_name="Computer Science",
    hod_name="Dr. Ramesh Kumar",
    budget=850000
)

ece = Department(
    dept_name="Electronics",
    hod_name="Dr. Priya Nair",
    budget=620000
)

mech = Department(
    dept_name="Mechanical",
    hod_name="Dr. Suresh Iyer",
    budget=540000
)

session.add_all([cs, ece, mech])
session.commit()

s1 = Student(
    first_name="Arjun",
    last_name="Mehta",
    email="arjun.orm@college.edu",
    department_id=cs.department_id,
    enrollment_year=2022
)

s2 = Student(
    first_name="Priya",
    last_name="Suresh",
    email="priya.orm@college.edu",
    department_id=cs.department_id,
    enrollment_year=2022
)

s3 = Student(
    first_name="Rohan",
    last_name="Verma",
    email="rohan.orm@college.edu",
    department_id=ece.department_id,
    enrollment_year=2021
)

s4 = Student(
    first_name="Vikram",
    last_name="Das",
    email="vikram.orm@college.edu",
    department_id=mech.department_id,
    enrollment_year=2022
)

s5 = Student(
    first_name="Kavya",
    last_name="Menon",
    email="kavya.orm@college.edu",
    department_id=cs.department_id,
    enrollment_year=2021
)

session.add_all([s1, s2, s3, s4, s5])
session.commit()

c1 = Course(
    course_name="Data Structures",
    course_code="CS101",
    credits=4,
    department_id=cs.department_id
)

c2 = Course(
    course_name="Database Systems",
    course_code="CS102",
    credits=3,
    department_id=cs.department_id
)

c3 = Course(
    course_name="Circuit Theory",
    course_code="EC101",
    credits=3,
    department_id=ece.department_id
)

session.add_all([c1, c2, c3])
session.commit()

e1 = Enrollment(
    student_id=s1.student_id,
    course_id=c1.course_id
)

e2 = Enrollment(
    student_id=s2.student_id,
    course_id=c1.course_id
)

e3 = Enrollment(
    student_id=s3.student_id,
    course_id=c3.course_id
)

e4 = Enrollment(
    student_id=s5.student_id,
    course_id=c2.course_id
)

session.add_all([e1, e2, e3, e4])
session.commit()

students = (
    session.query(Student)
    .join(Department)
    .filter(
        Department.dept_name == "Computer Science"
    )
    .all()
)

for student in students:
    print(
        student.first_name,
        student.last_name
    )

enrollments = (
    session.query(Enrollment)
    .all()
)

for enrollment in enrollments:

    print(
        enrollment.student.first_name,
        enrollment.student.last_name,
        "->",
        enrollment.course.course_name
    )

student = (
    session.query(Student)
    .filter(
        Student.email == "kavya.orm@college.edu"
    )
    .first()
)

student.enrollment_year = 2023

session.commit()

print(
    student.first_name,
    student.enrollment_year
)

enrollment = (
    session.query(Enrollment)
    .first()
)
session.delete(enrollment)

session.commit()

remaining = (
    session.query(Enrollment)
    .count()
)

print(
    "Remaining enrollments:",
    remaining
)

