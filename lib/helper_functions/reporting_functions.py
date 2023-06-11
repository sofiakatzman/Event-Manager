from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Event, Position, Staff

engine = create_engine("sqlite:///db/event_manager.db")
session = Session(engine, future=True)

# view open events
def view_open_events():
    print("")
    print("       O P E N   E V E N T S")
    open_events = session.query(Event).filter_by(is_active=True).all()
    if open_events:
        for event in open_events:
            print("______________________________________")
            print("")
            print(f"Event ID: {event.id}")
            print(f"Event Type: {event.type}")
            print(f"Event Date: {event.date}")

    else:
        print("______________________________________")
        print("")
        print("No open events found.")

# view open events
def view_closed_events():
    print("")
    print("    C L O S E D   E V E N T S")
    open_events = session.query(Event).filter_by(is_active=False).all()
    if open_events:
        for event in open_events:
            print("______________________________________")
            print("")
            print(f"Event ID: {event.id}")
            print(f"Event Type: {event.type}")
            print(f"Event Date: {event.date}")
    else:
        print("______________________________________")
        print("")
        print("No closed events found.")

# view staff by position
def staff_by_position():
    print("Displaying Staff By Position...")
    positions = session.query(Position).all()
    for position in positions:
        print("")
        print("")
        print("")
        print(f"Position: {position.name}")
        staff = session.query(Staff).filter_by(position_id=position.id).all()
        if staff:
            for user in staff:
                print("--------------------------------------")
                print(f"User: {user.first_name} {user.last_name}")
        else:
            print("______________________________________")
            print("")
            print("No staff found for this position.")