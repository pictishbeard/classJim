from db.run_sql import run_sql

from models.gymclass import gymClass
from models.member import Member

def save(member):
    sql = "INSERT INTO members( full_name, experience_level ) VALUES ( %s, %s ) RETURNING id"
    values = [member.full_name]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

