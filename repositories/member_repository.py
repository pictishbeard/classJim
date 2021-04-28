from db.run_sql import run_sql

from models.schedule import Schedule
from models.gymclass import gymClass
from models.member import Member

def save(member):
    sql = "INSERT INTO members( full_name, experience_level ) VALUES ( %s, %s ) RETURNING id"
    values = [member.full_name, member.experience_level]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return f"Notification: A new member, {member.full_name}, who is at a {member.experience_level} level, has been saved"

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['full_name'], row['experience_level'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['full_name'], result['experience_level'], result['id'])
    return member

def gymclasses(member):
    gymclasses = []

    sql = "SELECT gymclasses.* FROM gymclasses INNER JOIN schedules ON schedules.gymclass_id = gymclasses.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        gymclass = gymClass(row['lesson_name'], row['duration'], row['difficulty_level'], row['capacity'], row['id'])
        gymclasses.append(gymclass)

    return gymclasses

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(member):
    sql = "UPDATE members SET (full_name, experience_level) = (%s, %s) WHERE id = %s"
    values = [member.full_name, member.experience_level, member.id]
    run_sql(sql, values)