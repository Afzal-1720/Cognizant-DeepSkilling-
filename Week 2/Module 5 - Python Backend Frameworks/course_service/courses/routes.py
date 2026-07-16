from flask import Blueprint
from flask import jsonify
from flask import request

from extensions import db

from .models import Course


courses_bp = Blueprint(

    "courses",

    __name__,

    url_prefix="/api/courses"

)


@courses_bp.route("/", methods=["GET"])
def get_courses():

    courses = Course.query.all()

    return jsonify(

        [course.to_dict() for course in courses]

    )


@courses_bp.route("/<int:id>", methods=["GET"])
def get_course(id):

    course = Course.query.get_or_404(id)

    return jsonify(

        course.to_dict()

    )


@courses_bp.route("/", methods=["POST"])
def create_course():

    data = request.get_json()

    course = Course(

        name=data["name"],

        code=data["code"],

        credits=data["credits"],

        department=data["department"]

    )

    db.session.add(course)

    db.session.commit()

    return jsonify(

        course.to_dict()

    ), 201