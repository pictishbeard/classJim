import pdb

from models.gymclass import gymClass
from models.member import Member
from models.schedule import Schedule

import repositories.member_repository as member_repository
import repositories.schedule_repository as schedule_repository
import repositories.gymclass_repository as gymclass_repository

member_repository.delete_all()
schedule_repository.delete_all()
gymclass_repository.delete_all()

member1 = Member('Eddie Hall', 'Elite')
member_repository.save(member1)

member2 = Member('Not Jim', 'Intermediate')
member_repository.save(member2)

member3 = Member('Jo Smith', 'Beginner')
member_repository.save(member3)

gymclass1 = gymClass('Strongman Prep', 60, 'Advanced', 10)
gymclass_repository.save(gymclass1)

gymclass2 = gymClass('Zumba Intro', 30, 'Beginner', 20)
gymclass_repository.save(gymclass2)

gymclass3 = gymClass('HIIT Intermediate', 15, 'Intermediate', 25)
gymclass_repository.save(gymclass3)

schedule1 = Schedule(member1, gymclass1)
schedule_repository.save(schedule1)

schedule2 = Schedule(member2, gymclass3)
schedule_repository.save(schedule2)

schedule3 = Schedule(member3, gymclass2)
schedule_repository.save(schedule3)

pdb.set_trace()