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

gymclass1 = gymClass('Strongman Prep', 60, 'Advanced', 10)
gymclass_repository.save(gymclass1)

schedule1 = Schedule(member1, gymclass1)
schedule_repository.save(schedule1)

pdb.set_trace()