from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    ci = db.Column(db.String(20))
    area = db.Column(db.String(50))

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "ci": self.ci,
            "area": self.area
        }


class Subject(db.Model):

    __tablename__ = "subjects"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }


class Module(db.Model):

    __tablename__ = "modules"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"))

    subject = db.relationship("Subject")

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "subject_id": self.subject_id
        }


class Grade(db.Model):

    __tablename__ = "grades"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"))
    module_id = db.Column(db.Integer, db.ForeignKey("modules.id"))

    nota = db.Column(db.Integer)

    student = db.relationship("Student")
    subject = db.relationship("Subject")
    module = db.relationship("Module")

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "subject_id": self.subject_id,
            "module_id": self.module_id,
            "nota": self.nota
        }