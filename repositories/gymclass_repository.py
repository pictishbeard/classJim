from db.run_sql import run_sql

import pdb

from models.gymclass import gymClass
from models.member import Member

def save(gymclass):
    sql = "INSERT INTO gymclasses(lesson_name, duration, difficulty_level, capacity) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [gymclass.lesson_name, gymclass.duration, gymclass.difficulty_level, gymclass.capacity]
    results = run_sql( sql, values )
    gymclass.id = results[0]['id']
    return gymclass

def select_all():
    gymclasses = []

    sql = "SELECT * FROM gymclasses"
    results = run_sql(sql)

    for row in results:
        gymclass = gymClass(row['lesson_name'], row['duration'], row['difficulty_level'], row['capacity'])
        gymclasses.append(gymclass)
    return gymclasses

def select(id):
    gymclass = None
    sql = "SELECT * FROM gymclasses WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gymclass = gymClass(result['lesson_name'], result['duration'], result['difficulty_level'], result['capacity'])
    return gymclass

def members(gymclass):
    members = []

    sql = "SELECT members.* FROM members INNER JOIN schedules ON schedules.member_id = members.id WHERE gymclass_id = %s"
    values = [gymclass.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['full_name'], row['experience_level'])
        members.append(member)
    
    return members

def delete_all():
    sql = "DELETE FROM gymclasses"
    run_sql(sql)