from flask import Blueprint, render_template, request
from flask_bcrypt import generate_password_hash
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database_objects import *
from typing import *

# blueprints are modules that help organise the structure of applications into subdirectories.
bp = Blueprint("pages", __name__)

FILE_NAME = "users.db"
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


@bp.route("/login")
def login() -> str:
    """
    Login route
    :return: str
    """
    return render_template("pages/login.html")


@bp.route("/dob", methods=["POST"])
def dob() -> Union[str, Tuple[str, int]]:
    """
    Date of Birth route
    :return: Union[str, Response]
    """
    if request.method == "POST":
        login_info = request.get_json()  # parses as JSON
        # for true security, should probably hash the password in the JS script too, as well as having a larger amounts of rounds to bcrypt.
        session.add(User(email=login_info["email"], password=generate_password_hash(login_info["password"], 12)))
        session.commit()

        return "OK", 200

    return render_template("pages/dob.html")


@bp.route("/menu", methods=["GET", "POST"])
def menu() -> str:
    """
    Menu route for user once logged in or registered.
    :return: str
    """
    return render_template("pages/menu.html")
