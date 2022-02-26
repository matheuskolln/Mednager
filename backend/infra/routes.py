from typing import Tuple
from flask import Blueprint, request
from infra.controllers.employee_controller import EmployeeController
from infra.controllers.plan_controller import PlanController


routes = Blueprint("routes", __name__)
employee_controller = EmployeeController()
plans_controller = PlanController()


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
