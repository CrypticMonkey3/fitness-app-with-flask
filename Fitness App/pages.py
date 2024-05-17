from flask import Blueprint, render_template, request

# blueprints are modules that help organise the structure of applications into subdirectories.
bp = Blueprint("pages", __name__)


@bp.route("/")
def home():
    return render_template("pages/home.html")  # render_template expects parameter to be in a templates/ folder already.


@bp.route("/handle_setup_data", methods=["POST"])
def handle_setup_data():
    x = request.form["user_dob"]
    print(x)
    return render_template("pages/about.html")
