from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.gymclass import gymClass
import repositories.gymclass_repository as gymclass_repository

gymclasses_blueprint = Blueprint("gymclasses", __name__)

@gymclasses_blueprint.route("/gymclasses")
def gymclasses():
    gymclasses = gymclass_repository.select_all()
    return render_template("/gymclasses/index.html", gymclasses = gymclasses)

@gymclasses_blueprint.route("/gymclasses/<id>")
def show(id):
    gymclass = gymclass_repository.select(id)
    members = gymclass_repository.members(gymclass)
    return render_template("gymclasses/show.html", gymclass=gymclass, members=members)