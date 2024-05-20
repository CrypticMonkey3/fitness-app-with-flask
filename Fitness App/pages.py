from flask import Blueprint, render_template, request, redirect, url_for, Response
from typing import Union

# blueprints are modules that help organise the structure of applications into subdirectories.
bp = Blueprint("pages", __name__)


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


@bp.route("/dob", methods=["GET", "POST"])
def dob() -> Union[str, Response]:
    """
    Date of Birth route
    :return: Union[str, Response]
    """
    if request.method == "POST":

        print(request.form)
        print(list(request.form))
        print(request.values)
        return redirect(url_for("pages.home"))

    return render_template("pages/dob.html")


@bp.route("/menu", methods=["GET", "POST"])
def menu() -> str:
    """
    Menu route for user once logged in or registered.
    :return: str
    """
    return render_template("pages/menu.html")
