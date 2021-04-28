from db.run_sql import run_sql

from models.schedule import Schedule
from models.gymclass import gymClass
from models.member import Member
import repositories.member_repository as member_repository
import repositories.gymclass_repository as gymclass_repository

def save(schedule):
    sql = "INSERT INTO schedules ( member_id, gymclass_id ) VALUES ( %s, %s ) RETURNING id"
    values = [schedule.member.id, schedule.gymclass.id]
    results = run_sql(sql, values)
    schedule.id = results[0]['id']
    return schedule

def select_all():
    schedules = []
    sql = "SELECT * FROM schedules"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        gymclass = gymclass_repository.select(row['gymclass_id'])
        schedule = Schedule(member, gymclass, row['id'])
        schedules.append(schedule)
    return schedules

def select(id):
    schedule = None
    sql = "SELECT * FROM schedules WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

def gymclass(schedule):
    sql = "SELECT * FROM gymclasses WHERE id = %s"
    values = [schedule.gymclass.id]
    results = run_sql(sql, values)[0]
    member = Member(results['full_name'], results['experience_level'])
    return member

def delete_all():
    sql = "DELETE FROM schedules"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM visits WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(schedule):
    sql = "UPDATE schedules SET (member_id, gymclass_id) = (%s, %s) WHERE id = %s" 
    values = [schedule.member.id, schedule.gymclass.id, gymclass.id]
    run_sql(sql, values)