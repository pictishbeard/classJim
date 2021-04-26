from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.gymclass import gymClass
import repositories.gymclass_repository as gymclass_repository

gymclasses_blueprint = Blueprint("gymclasses", __name__)

@gymclasses_blueprint.route("/gynclasses")
def gymclasses():
    gymclasses = gymclass_repository.select_all()
    return render_template("gymclasses/index.html", gymclasses = gymclasses)
