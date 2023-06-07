from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import random

from models import (Users, Events, Positions)

fake = Faker()

engine = create_engine("sqlite:///event_manager")
session = Session(engine, future=True)

# clear data when session runs
session.query(Users).delete()
session.query(Positions).delete()
session.query(Events).delete()

positions_list = {
    0 : "Standby",
    1 : "Waitress" , 
    2 : "Bartender",
    3 : "Busser",
    4 : "Hostess",
    5 : "Administration"
    }

# generate users seeded data
users = []
for i in range(30):
    user = Users(
        first_name=f'{fake.first_name()}',
        last_name=f'{fake.last_name()}',
        position_id=random.randint(1, 4)
    )
    users.append(user)


# generate position data
positions = []
for position_id, position_name in positions_list.items():
    position = Positions(
        id=position_id,
        name=position_name,
        tipout_percent=0
    )
    positions.append(position)

# generate event data
#=> NO EVENT DATA FOR NOW ** 

#seed data
print("Seeding data...")
session.add_all(users)
session.add_all(positions)
session.commit()
