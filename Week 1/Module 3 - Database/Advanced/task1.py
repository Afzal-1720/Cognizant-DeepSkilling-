from sqlalchemy.orm import joinedload
import urllib.parse
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Date,
    Numeric,
    Boolean,
    create_engine
)

from sqlalchemy.orm import (
    relationship,
    declarative_base
)

password = urllib.parse.quote_plus("Afzal@2006")

engine = create_engine(
    f"postgresql+psycopg2://postgres:{password}@localhost/college_db_orm",echo= True
)

Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True)
    dept_name = Column(String(100), nullable=False)
    hod_name = Column(String(100))
    budget = Column(Numeric(12, 2))

    students = relationship(
        "Student",
        back_populates="department"
    )

    courses = relationship(
        "Course",
        back_populates="department"
    )

    professors = relationship(
        "Professor",
        back_populates="department"
    )



class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)

    first_name = Column(
        String(50),
        nullable=False
    )

    last_name = Column(
        String(50),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    date_of_birth = Column(Date)

    department_id = Column(
        Integer,
        ForeignKey("departments.department_id")
    )

    enrollment_year = Column(Integer)

    department = relationship(
        "Department",
        back_populates="students"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="student"
    )
    is_active = Column(
    Boolean,
    nullable=False,
    default=True
    )



class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True)

    course_name = Column(
        String(150),
        nullable=False
    )

    course_code = Column(
        String(20),
        unique=True
    )

    credits = Column(Integer)

    department_id = Column(
        Integer,
        ForeignKey("departments.department_id")
    )

    department = relationship(
        "Department",
        back_populates="courses"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="course"
    )



class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(
        Integer,
        primary_key=True
    )

    student_id = Column(
        Integer,
        ForeignKey("students.student_id")
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.course_id")
    )

    enrollment_date = Column(Date)

    grade = Column(String(2))

    student = relationship(
        "Student",
        back_populates="enrollments"
    )

    course = relationship(
        "Course",
        back_populates="enrollments"
    )


class Professor(Base):
    __tablename__ = "professors"

    professor_id = Column(
        Integer,
        primary_key=True
    )

    prof_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.department_id")
    )

    salary = Column(
        Numeric(10, 2)
    )

    department = relationship(
        "Department",
        back_populates="professors"
    )
class CourseSchedule(Base):

    __tablename__ = "course_schedules"

    schedule_id = Column(
        Integer,
        primary_key=True
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.course_id")
    )

    day_of_week = Column(
        String(20),
        nullable=False
    )

    start_time = Column(
        String(10),
        nullable=False
    )

    end_time = Column(
        String(10),
        nullable=False
    )

    course = relationship("Course")



if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("All tables created successfully!")

#C:\Users\fmdaf\Documents\Cognizant Deepskilling 2027>C:\Users\fmdaf\AppData\Local\Microsoft\WindowsApps\python3.13.exe "c:/Users/fmdaf/Documents/Cognizant Deepskilling 2027/Week 1/Module 3 - Database/Advanced/task1.py"
#All tables created successfully!