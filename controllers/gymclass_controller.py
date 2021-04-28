from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.gymclass import gymClass
import repositories.gymclass_repository as gymclass_repository

gymclasses_blueprint = Blueprint("gymclasses", __name__)

@gymclasses_blueprint.route("/gymclasses")
def gymclasses():
    gymclasses = gymclass_repository.select_all()
    return render_template("/gymclasses/index.html", gymclasses = gymclasses)

@gymclasses_blueprint.route("/gymclasses/<id>", methods=['GET'])
def show(id):
    gymclass = gymclass_repository.select(id)
    members = gymclass_repository.members(gymclass)
    return render_template("gymclasses/show.html", gymclass=gymclass, members=members)

@gymclasses_blueprint.route("/gymclasses/<id>/edit", methods=['GET'])
def gymclasses_edit(id):
    gymclass = gymclass_repository.select(id)
    return render_template('/gymclasses/edit.html', gymclass = gymclass)

@gymclasses_blueprint.route("/gymclasses/<id>", methods=['POST'])
def gymclasses_update(id):
    lesson_name = request.form['lesson_name']
    difficulty_level = request.form['difficulty_level']
    duration = request.form['duration']
    capacity = request.form['capacity']
    day = request.form['day']
    gymclass = gymClass(lesson_name, difficulty_level, duration, capacity, day, id)
    gymclass_repository.update(gymclass)
    return redirect('/gymclasses/index.html')

@gymclasses_blueprint.route("/gymclasses/new", methods=['GET'])
def gymclasses_new_form():
    return render_template('gymclasses/new.html', title='Add New Gym Class')

@gymclasses_blueprint.route("/gymclasses/new", methods=['POST'])
def gymclasses_add_new():
    lesson_name = request.form['lesson_name']
    duration = request.form['duration']
    day = request.form['day']
    difficulty_level = request.form['difficulty_level']
    capacity = request.form['capacity']
    gymclass = gymClass(lesson_name, duration, difficulty_level, capacity, day)
    gymclass_repository.save(gymclass)
    return redirect('/gymclasses')

@gymclasses_blueprint.route("/gymclasses/<id>/delete", methods=['POST'])
def gymclasses_delete(id):
    gymclass_repository.delete(id)
    return redirect('/gymclasses')
