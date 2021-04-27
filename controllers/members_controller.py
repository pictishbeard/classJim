from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

#index route
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

#update route
@members_blueprint.route("/members/<id>")
def show_members(id):
    member = member_repository.select(id)
    gymclass = member_repository.gymclass(member)
    return render_template("members/show.html", member=member, gymclass=gymclass)

#create route

#new route

#edit route

#delete route
