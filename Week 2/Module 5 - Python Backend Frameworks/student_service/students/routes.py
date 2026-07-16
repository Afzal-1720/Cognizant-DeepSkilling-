from flask import Blueprint
from flask import jsonify
from flask import request
import requests

from extensions import db
from .models import Student

students_bp = Blueprint(
    "students",
    __name__,
    url_prefix="/api/students"
)


@students_bp.route("/", methods=["GET"])
def get_students():

    students = Student.query.all()

    return jsonify(
        [student.to_dict() for student in students]
    )


@students_bp.route("/", methods=["POST"])
def create_student():

    data = request.get_json()

    student = Student(

        first_name=data["first_name"],

        last_name=data["last_name"],

        email=data["email"],

        department=data["department"]

    )

    db.session.add(student)

    db.session.commit()

    return jsonify(
        student.to_dict()
    ), 201


@students_bp.route("/<int:id>/enroll", methods=["POST"])
def enroll_student(id):

    data = request.get_json()

    course_id = data["course_id"]

    try:

        response = requests.get(
            f"http://127.0.0.1:5001/api/courses/{course_id}"
        )

        if response.status_code != 200:

            return jsonify({

                "message": "Course not found"

            }), 404

        return jsonify({

            "message": "Student enrolled successfully",

            "student_id": id,

            "course_id": course_id

        }), 201

    except requests.exceptions.ConnectionError:

        return jsonify({

            "message": "Course Service unavailable"

        }), 503
