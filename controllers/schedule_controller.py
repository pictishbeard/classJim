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

#GET method for new schedule entry form
@schedules_blueprint.route("/schedules/new", methods=['GET'])
def new_entry():
    members = member_repository.select_all()
    gymclasses = gymclass_repository.select_all()
    return render_template("schedules/new.html", members = members, gymclasses = gymclasses)

#POST method for creating new schedule entry
@schedules_blueprint.route("/schedules", methods=['POST'])
def create_entry():
    member_id = request.form['member_id']
    gymclass_id = request.form['gymclass_id']
    member = member_repository.select(member_id)
    gymclass = gymclass_repository.select(gymclass_id)
    schedule = Schedule(member, gymclass)
    schedule_repository.save(schedule)
    return redirect('/schedules')

#DELETE method for removing schedule entries
@schedules_blueprint.route("/schedules/<id>/delete")
def delete_entry(id):
    schedule_repository.delete(id)
    return redirect('/schedules')