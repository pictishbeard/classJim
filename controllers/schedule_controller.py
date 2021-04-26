from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.schedule import Schedule
import repositories.schedule_repository as schedule_repository
import repositories.member_repository as member_repository
import repositories.gymclass_repository as gymclass_repository

schedules_blueprint = Blueprint("schedules", __name__)
@schedules_blueprint.route("/schedules")
def schedules():
    schedules = schedule_repository.select_all()
    return render_template("schedules/index.html", schedules = schedules)