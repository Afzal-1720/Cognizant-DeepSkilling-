from flask import Flask

from config import Config

from extensions import db
from extensions import migrate

from students.routes import students_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    app.register_blueprint(students_bp)

    return app


app = create_app()

if __name__ == "__main__":

    app.run(
        port=5002,
        debug=True
    )
