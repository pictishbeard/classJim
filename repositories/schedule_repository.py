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
    sql = "SELECT * FROM gymclasses"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        gymclass = gymclass_repository.select(row['gymclass_id'])
        schedule = Schedule(member, gymclass, row['id'])
        schedules.append(schedule)
    return schedules

