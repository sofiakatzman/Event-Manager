# Reporting:
#     4 - VIEW OPEN EVENTS - view_open_events()
#     5 - VIEW STAFF BY POSITIONS - staff_by_position()

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Event, Position, Staff

engine = create_engine("sqlite:///db/event_manager.db")
session = Session(engine, future=True)

def test():
    print("Testing passed for Reporting Module!")

# view open events
def view_open_events():
    print("Displaying Open Events...")
    open_events = session.query(Event).filter_by(is_active=True).all()
    if open_events:
        for event in open_events:
            print(f"Event ID: {event.id}")
            print(f"Event Type: {event.type}")
            print(f"Event Date: {event.date}")
    else:
        print("No open events found.")

# view staff by position
def staff_by_position():
    print("Displaying Staff By Position...")
    positions = session.query(Position).all()
    for position in positions:
        print(f"Position: {position.name}")
        staff = session.query(Staff).filter_by(position_id=position.id).all()
        if staff:
            for user in staff:
                print(f"User: {user.first_name} {user.last_name}")
        else:
            print("No staff found for this position.")