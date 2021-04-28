from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

#index route for members
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

#show member info route
@members_blueprint.route("/members/<id>", methods=['GET'])
def show_members(id):
    member = member_repository.select(id)
    gymclasses = member_repository.gymclasses(member)
    return render_template("/members/show.html", member=member, gymclasses=gymclasses)

#New member form
@members_blueprint.route("/members/new", methods=['GET'])
def new_member_form():
    return render_template("/members/new.html", title="Add New Gym Member")

# Create new member entry
@members_blueprint.route("/members/new", methods=['POST'])
def create_member():
    full_name = request.form["full_name"]
    experience_level = request.form["experience_level"]
    new_member = Member(full_name, experience_level)
    return render_template('/members/new.html', title="New Gym Member Added", result=member_repository.save(new_member))

# Edit member entry
@members_blueprint.route("/members/<id>/edit", methods=['GET'])
def edit_member(id):
    member = member_repository.select(id)
    return render_template('/members/edit.html', member = member)

# Update member entry
@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    full_name = request.form["full_name"]
    experience_level = request.form["experience_level"]
    member = Member(full_name, experience_level, id)
    member_repository.update(member)
    return redirect("/members")

# Delete member entry
@members_blueprint.route("/members/<id>/delete", methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")