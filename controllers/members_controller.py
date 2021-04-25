from flask import Blueprint, Flask, redirect, render_template, request

from models.member import Member
import member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

#index route
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

#update route
@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    full_name = request.form["full_name"]
    member = Member(full_name, experience_level, id)
    member_repository.update(member)
    return redirect("/members")

#create route

#new route

#edit route

#delete route
