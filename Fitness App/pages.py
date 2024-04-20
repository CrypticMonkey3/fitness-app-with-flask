from flask import Blueprint, render_template

# blueprints are modules that help organise the structure of applications into subdirectories.
bp = Blueprint("pages", __name__)


@bp.route("/")
def home():
    return render_template("pages/home.html")  # render_template expects parameter to be in a templates/ folder already.


@bp.route("/about")
def about():
    return render_template("pages/about.html")


@bp.route("/friends")
def friends():
    return render_template("pages/friends.html")


@bp.route("/online")
def online():
    return render_template("pages/online.html")


@bp.route("/profile")
def profile():
    return render_template("pages/profile.html")

