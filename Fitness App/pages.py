from flask import Blueprint, render_template, request

# blueprints are modules that help organise the structure of applications into subdirectories.
bp = Blueprint("pages", __name__)


@bp.route("/")
def home():
    return render_template("pages/home.html")  # render_template expects parameter to be in a templates/ folder already.


@bp.route("/login")
def login():
    return render_template("pages/login.html")


@bp.route("/dob", methods=["GET", "POST"])
def dob():
    if request.method == "POST":
        email = request.form.get("email")

        print(email)
        print(request.form)
        print(list(request.form))
        print(request.form["email"])
        return render_template("pages/home.html")
    return render_template("pages/dob.html")


@bp.route("/menu", methods=["GET", "POST"])
def menu():
    return render_template("pages/menu.html")


# NOTE FOR FUTURE: MAKE LOGIN AND REGISTRATION ON THE SAME FORM

