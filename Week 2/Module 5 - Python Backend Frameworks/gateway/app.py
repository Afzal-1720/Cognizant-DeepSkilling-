from flask import Flask, request
import requests

app = Flask(__name__)


# ----------------------------
# COURSE SERVICE
# ----------------------------

@app.route(
    "/api/courses/",
    defaults={"path": ""},
    methods=["GET", "POST"]
)
@app.route(
    "/api/courses/<path:path>",
    methods=["GET", "POST", "PUT", "DELETE"]
)
def course_gateway(path):

    url = f"http://127.0.0.1:5001/api/courses/{path}"

    response = requests.request(
        method=request.method,
        url=url,
        json=request.get_json(silent=True)
    )

    return (
        response.content,
        response.status_code,
        response.headers.items()
    )


# ----------------------------
# STUDENT SERVICE
# ----------------------------

@app.route(
    "/api/students/",
    defaults={"path": ""},
    methods=["GET", "POST"]
)
@app.route(
    "/api/students/<path:path>",
    methods=["GET", "POST"]
)
def student_gateway(path):

    url = f"http://127.0.0.1:5002/api/students/{path}"

    response = requests.request(
        method=request.method,
        url=url,
        json=request.get_json(silent=True)
    )

    return (
        response.content,
        response.status_code,
        response.headers.items()
    )


if __name__ == "__main__":
    app.run(
        port=5000,
        debug=True
    )