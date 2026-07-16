from extensions import db


class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    first_name = db.Column(
        db.String(100),
        nullable=False
    )

    last_name = db.Column(
        db.String(100)
    )

    email = db.Column(
        db.String(100),
        unique=True
    )

    department = db.Column(
        db.String(100)
    )

    def to_dict(self):

        return {

            "id": self.id,

            "first_name": self.first_name,

            "last_name": self.last_name,

            "email": self.email,

            "department": self.department

        }
