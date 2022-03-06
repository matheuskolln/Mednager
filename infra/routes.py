from typing import Tuple
from flask import Blueprint, request
from infra.controllers.doctor_controller import DoctorController
from infra.controllers.employee_controller import EmployeeController
from infra.controllers.exam_controller import ExamController
from infra.controllers.medical_appointment_controller import (
    MedicalAppointmentController,
)
from infra.controllers.medical_prescription_controller import (
    MedicalPrescriptionController,
)
from infra.controllers.medical_unit_controller import MedicalUnitController
from infra.controllers.patient_controller import PatientController
from infra.controllers.plan_controller import PlanController
from infra.controllers.problem_controller import ProblemController
from infra.controllers.speciality_controller import SpecialityController


routes = Blueprint("routes", __name__)

employee_controller = EmployeeController()
plans_controller = PlanController()
patient_controller = PatientController()
medical_unit_controller = MedicalUnitController()
problem_controller = ProblemController()
medical_appointment_controller = MedicalAppointmentController()
specialities_controller = SpecialityController()
doctor_controller = DoctorController()
exam_controller = ExamController()
medical_prescription_controller = MedicalPrescriptionController()


@routes.route("/employee", methods=["POST"])
def create_employee() -> Tuple[dict, int]:
    body = request.get_json()
    employee = employee_controller.create(
        fullname=body["fullname"],
        birthdate=body["birthdate"],
        email=body["email"],
        password=body["password"],
    )
    return {"employee": employee.to_dict()}, 201


@routes.route("/plans", methods=["GET"])
def find_plans() -> Tuple[dict, int]:
    plans = plans_controller.find()
    return {"plans": [plan.to_dict() for plan in plans]}, 200


@routes.route("/patient", methods=["POST"])
def create_patient() -> Tuple[dict, int]:
    body = request.get_json()
    patient = patient_controller.create(
        fullname=body["fullname"],
        birthdate=body["birthdate"],
        document=body["document"],
    )
    return {"patient": patient.to_dict()}, 201


@routes.route("/patient/<int:patient_id>/plan", methods=["POST"])
def add_plan_to_patient(patient_id: int) -> Tuple[dict, int]:
    body = request.get_json()
    patient = patient_controller.add_plan_to(
        patient_id=patient_id,
        plan_id=body["plan_id"],
    )
    return {"patient": patient.to_dict()}, 201


@routes.route("/medical-units", methods=["GET"])
def find_medical_units() -> Tuple[dict, int]:
    medical_units = medical_unit_controller.find()
    return {
        "medical_units": [medical_unit.to_dict() for medical_unit in medical_units]
    }, 200


@routes.route("/patient/<int:patient_id>/problem/<int:problem_id>", methods=["POST"])
def create_problem(patient_id: int) -> Tuple[dict, int]:
    body = request.get_json()
    problem = problem_controller.create(
        patient_id=patient_id,
        description=body["description"],
    )
    return {"problem": problem.to_dict()}, 201


@routes.route(
    "/patient/<int:patient_id>/problem/<int:problem_id>/medical-appointment",
    methods=["POST"],
)
def create_medical_appointment(patient_id: int, problem_id: int) -> Tuple[dict, int]:
    body = request.get_json()
    medical_appointment = medical_appointment_controller.create(
        date=body["date"],
        patient_id=patient_id,
        problem_id=problem_id,
        employee_id=body["employee_id"],
    )
    return {"medical_appointment": medical_appointment.to_dict()}, 201


@routes.route("/specialities", methods=["GET"])
def find_specialities() -> Tuple[dict, int]:
    specialities = specialities_controller.find()
    return {"specialities": [speciality.to_dict() for speciality in specialities]}, 200


@routes.route("/doctors", methods=["GET"])
def find_doctors() -> Tuple[dict, int]:
    doctors = doctor_controller.find()
    return {"doctors": [doctor.to_dict() for doctor in doctors]}, 200


@routes.route("/doctors/<int:doctor_id>/exams", methods=["POST"])
def create_exam(doctor_id: int) -> Tuple[dict, int]:
    body = request.get_json()
    exam = exam_controller.create(
        date=body["date"],
        employee_id=body["employee_id"],
        previous_medical_appointment_id=body["previous_medical_appointment_id"],
        patient_id=body["patient_id"],
        doctor_id=doctor_id,
    )
    return {"exam": exam.to_dict()}, 201


@routes.route("/patients/<int:patient_id>/medical-prescriptions", methods=["POST"])
def create_medical_prescription(patient_id: int) -> Tuple[dict, int]:
    body = request.get_json()
    medical_prescription = medical_prescription_controller.create(
        description=body["description"],
        date=body["date"],
        patient_id=patient_id,
        doctor_id=body["doctor_id"],
    )
    return {"medical_prescription": medical_prescription.to_dict()}, 201
