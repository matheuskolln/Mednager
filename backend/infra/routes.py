from typing import Tuple
from flask import Blueprint, request
from infra.controllers.employee_controller import EmployeeController


routes = Blueprint("routes", __name__)
employee_controller = EmployeeController()


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
