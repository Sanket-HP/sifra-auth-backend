import azure.functions as func
import bcrypt
import uuid
import os
from utils.db import create_user, user_exists

def main(req: func.HttpRequest) -> func.HttpResponse:
    data = req.get_json()
    full_name = data.get('full_name')
    email = data.get('email')
    role = data.get('role')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if not all([full_name, email, role, password, confirm_password]):
        return func.HttpResponse("All fields required", status_code=400)

    if password != confirm_password:
        return func.HttpResponse("Passwords do not match", status_code=400)

    if user_exists(email):
        return func.HttpResponse("User already exists", status_code=409)

    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    create_user(full_name, email, role, hashed_pw)
    return func.HttpResponse("Signup successful", status_code=200)
