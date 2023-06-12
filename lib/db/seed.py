from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from datetime import date
import random

from models import (Staff, Event, Position, Schedule)

fake = Faker()

engine = create_engine("sqlite:///event_manager.db")
session = Session(engine, future=True)

# clear data when session runs
session.query(Staff).delete()
session.query(Position).delete()
session.query(Event).delete()
session.query(Schedule).delete()

# generate staff seeded data
staff = []
for i in range(75):
    new_staff = Staff(
        first_name=f'{fake.first_name()}',
        last_name=f'{fake.last_name()}',
        position_id=random.randint(0, 5)
    )
    staff.append(new_staff)

# generate position data
positions_list = {
    0 : "Standby",
    1 : "Waitress" , 
    2 : "Bartender",
    3 : "Busser",
    4 : "Hostess",
    5 : "Administration"
    }

positions = []
for position_id, position_name in positions_list.items():
    position = Position(
        id=position_id,
        name=position_name
    )
    positions.append(position)

# generate event data
event_types = {"Art Gallery Opening" : "Art Gallery Opening for P&W" ,
                "Private Event" : "Private Event for Sir Elton John",
                "Music Show" : "Music Event at The Edge",
                "Talent Showcase" : "Talent Showcase at Sony Hall", 
                "Music Festival" : "CircoLoco Music Festival"}

events = []
start_date = date(2022, 1, 1)
end_date = date(2023, 6, 1)
for event_type, event_description in event_types.items():
    event = Event(
        type = f'{event_type}',
        description = f'{event_description}',
        date = f'{fake.date_between_dates(date_start=start_date, date_end=end_date)}'
    )
    events.append(event)

# generate schedyke data
schedule1 = Schedule(event_id=1, event_type = "Art Gallery Opening", staff_id = 1, position_id = 5, arrival_time = "12:00")
schedule2 = Schedule(event_id=1, event_type = "Art Gallery Opening", staff_id = 2, position_id = 3, arrival_time = "12:00")
schedule3 = Schedule(event_id=1, event_type = "Art Gallery Opening", staff_id = 6, position_id = 3, arrival_time = "12:00")
schedule4 = Schedule(event_id=1, event_type = "Art Gallery Opening", staff_id = 15, position_id = 2, arrival_time = "12:00")
schedule5 = Schedule(event_id=1, event_type = "Art Gallery Opening", staff_id = 23, position_id = 5, arrival_time = "12:00")
print("Seeding data...")
# Add all data to the session
schedules = [schedule1, schedule2, schedule3, schedule4, schedule5]
all_objects = staff + positions + events + schedules
session.add_all(all_objects)
session.commit()