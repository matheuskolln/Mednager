from typing import Tuple
from flask import Blueprint, request
from infra.controllers.employee_controller import EmployeeController
from infra.controllers.medical_unit_controller import MedicalUnitController
from infra.controllers.patient_controller import PatientController
from infra.controllers.plan_controller import PlanController
from infra.controllers.problem_controller import ProblemController


routes = Blueprint("routes", __name__)
employee_controller = EmployeeController()
plans_controller = PlanController()
patient_controller = PatientController()
medical_unit_controller = MedicalUnitController()
problem_controller = ProblemController()


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


@routes.route("/patient/<int:patient_id>/problem", methods=["POST"])
def create_problem(patient_id: int) -> Tuple[dict, int]:
    body = request.get_json()
    problem = problem_controller.create(
        patient_id=patient_id,
        description=body["description"],
    )
    return {"problem": problem.to_dict()}, 201
