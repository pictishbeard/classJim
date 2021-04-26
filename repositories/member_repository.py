from db.run_sql import run_sql

from models.gymclass import gymClass
from models.member import Member

def save(member):
    sql = "INSERT INTO members( full_name, experience_level ) VALUES ( %s, %s ) RETURNING id"
    values = [member.full_name]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

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

def class_bookings(member):
    class_bookings = []

    sql = "SELECT class_bookings.* FROM class_bookings INNER JOIN gym_classes ON gym_classes.gymclass_id = gymclasses.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        class_booking = gymClass(row['lesson_name'], row['duration'], row['difficulty_level'], row['capacity'])
        class_bookings.append(class_booking)

    return class_bookings

