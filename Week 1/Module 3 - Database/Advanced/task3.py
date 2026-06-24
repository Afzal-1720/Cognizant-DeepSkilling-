"""
TASK 90

N+1 ANALYSIS

Before joinedload:

1 query fetched enrollments.

Additional queries were issued
for each student and course.

Total query count increased
with the number of enrollments.

After joinedload:

SQLAlchemy generated one JOIN query.

Student and Course objects were
loaded eagerly.

Total SQL statements reduced
from many queries to one query.

This eliminates the N+1 problem
and improves performance.
"""

from sqlalchemy.orm import joinedload
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

enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(
            Enrollment.student
        ),
        joinedload(
            Enrollment.course
        )
    )
    .all()
)

for enrollment in enrollments:
    print(
        enrollment.student.first_name,
        enrollment.student.last_name,
        "->",
        enrollment.course.course_name
    )


#Enrollment.objects.select_related(
#    "student",
 #   "course"
#).all()

#2026-06-24 14:18:41,103 INFO sqlalchemy.engine.Engine [generated in 0.00036s] {}
#Priya Suresh -> Data Structures
#Rohan Verma -> Circuit Theory
#Kavya Menon -> Database Systems

