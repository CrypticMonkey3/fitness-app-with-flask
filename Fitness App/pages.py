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


@bp.route("/login", methods=["GET", "POST", "HEAD"])
def login() -> Union[str, Tuple[str, int]]:
    """
    Login route
    :return: Union[str, Tuple[str, int]]
    """
    if request.method == "POST":
        login_info = request.get_json()  # parses as JSON

        # checks if the registered user is already in the database or not.
        if len(session.query(User).where(User.email == login_info["email"]).all()) == 0:
            # for true security, should probably hash the password in the JS script too,
            # as well as having a larger amounts of rounds to bcrypt.
            session.add(User(email=login_info["email"], password=generate_password_hash(login_info["password"], 12)))
            session.commit()

            return "OK", 200

        return "I'm a teapot", 418  # The email is already in use.

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
