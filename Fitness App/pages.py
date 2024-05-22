from flask_bcrypt import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database_objects import *
from typing import *

# blueprints are modules that help organise the structure of applications into subdirectories.
bp = Blueprint("pages", __name__)

FILE_NAME = "users.db"
SLOWNESS = 12
engine = create_engine(f"sqlite:///{FILE_NAME}", echo=True)
session = Session(engine)
Base.metadata.create_all(engine)


@bp.route("/")
def home() -> str:
    """
    Landing page route
    :return: str
    """
    return render_template("pages/home.html")  # render_template expects parameter to be in a templates/ folder already.


@bp.route("/login/validate_registration", methods=["POST"])
def validate_registration() -> Tuple[str, int]:
    """
    Route to check registration
    :return: Tuple[str, int]
    """
    if request.method == "POST":
        registration_info = request.get_json()  # parses as JSON

        # checks if the user is registering and whether the email being setup is already in the database or not.
        if len(session.query(User).where(User.email == registration_info["email"]).all()) == 0:
            # for true security, should probably hash the password in the JS script too,
            # as well as having a larger amounts of rounds to bcrypt.
            session.add(User(email=registration_info["email"], password=generate_password_hash(registration_info["password"], SLOWNESS)))
            session.commit()

            return "OK", 200

        return "I'm a teapot", 418

    raise NotImplementedError("Not implemented a GET for 'validate_registration()'.")


@bp.route("/login/validate_login", methods=["POST"])
def validate_login() -> Tuple[str, int]:
    """
    Route to check login information.
    :return: Tuple[str, int]
    """
    if request.method == "POST":
        login_info = request.get_json()
        # get a query for all emails that match the provided one- should only be one occurrence
        email_occurrences = session.query(User).where(User.email == login_info["email"]).all()

        if len(email_occurrences) == 0:  # if there are no emails to the one provided
            return "non existent email", 418

        # if the email's password doesn't equal the one being used to login with
        elif not check_password_hash(email_occurrences[0].password, login_info["password"]):
            return "incorrect password", 418

        return "OK", 200  # when email and password are both existent and correct, respectively.

    raise NotImplementedError("Not implemented a GET for 'validate_login()'.")


@bp.route("/login")
def login() -> str:
    """
    Login route
    :return: str
    """
    return render_template("pages/login.html")


@bp.route("/dob")
def dob() -> str:
    """
    Date of Birth route
    :return: str
    """
    return render_template("pages/dob.html")


@bp.route("/menu", methods=["GET", "POST"])
def menu() -> str:
    """
    Menu route for user once logged in or registered.
    :return: str
    """
    return render_template("pages/menu.html")
