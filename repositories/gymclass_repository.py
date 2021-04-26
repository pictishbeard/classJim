from db.run_sql import run_sql

from models.gymclass import gymClass
from models.member import Member

def save(gymclass):
    sql = "INSERT INTO gymclasses( lesson_name, duration, difficulty_level, capacity ) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [gymclass.lesson_name, gymclass.duration, gymclass.difficulty_level, gymclass.capacity]
    results = run_sql(sql, values)
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
