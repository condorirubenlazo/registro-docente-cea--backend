from flask import request, jsonify
from models import db, Student, Subject, Module, Grade


def register_routes(app):

    # registrar estudiante
    @app.route("/students", methods=["POST"])
    def add_student():

        data = request.json

        student = Student(
            nombre=data["nombre"],
            ci=data["ci"],
            area=data["area"]
        )

        db.session.add(student)
        db.session.commit()

        return jsonify({"mensaje": "Estudiante registrado"})


    # ver estudiantes
    @app.route("/students", methods=["GET"])
    def get_students():

        students = Student.query.all()

        return jsonify([s.to_dict() for s in students])


    # registrar materia
    @app.route("/subjects", methods=["POST"])
    def add_subject():

        data = request.json

        subject = Subject(nombre=data["nombre"])

        db.session.add(subject)
        db.session.commit()

        return jsonify({"mensaje": "Materia creada"})


    # ver materias
    @app.route("/subjects", methods=["GET"])
    def get_subjects():

        subjects = Subject.query.all()

        return jsonify([s.to_dict() for s in subjects])


    # registrar modulo
    @app.route("/modules", methods=["POST"])
    def add_module():

        data = request.json

        module = Module(
            nombre=data["nombre"],
            subject_id=data["subject_id"]
        )

        db.session.add(module)
        db.session.commit()

        return jsonify({"mensaje": "Modulo creado"})


    # registrar nota
    @app.route("/grades", methods=["POST"])
    def add_grade():

        data = request.json

        grade = Grade(
            student_id=data["student_id"],
            subject_id=data["subject_id"],
            module_id=data["module_id"],
            nota=data["nota"]
        )

        db.session.add(grade)
        db.session.commit()

        return jsonify({"mensaje": "Nota registrada"})


    # calcular promedio
    @app.route("/average/<int:student_id>/<int:subject_id>")
    def calculate_average(student_id, subject_id):

        grades = Grade.query.filter_by(
            student_id=student_id,
            subject_id=subject_id
        ).all()

        if len(grades) == 0:
            return jsonify({"mensaje": "Sin notas"})

        total = sum(g.nota for g in grades)
        promedio = total / len(grades)

        estado = "APROBADO" if promedio >= 51 else "REPROBADO"

        return jsonify({
            "promedio": promedio,
            "estado": estado
        })