from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Event, Position, Staff, Schedule
from pyfiglet import Figlet

engine = create_engine("sqlite:///db/event_manager.db")
session = Session(engine, future=True)

# view open events
def view_open_events():
    print("")
    print("                      O P E N   E V E N T S")
    open_events = session.query(Event).filter_by(is_active=True).all()
    if open_events:
        for event in open_events:
            print("              ----------------------------------------")
            print("")
            print(f"                   Event ID: {event.id}")
            print(f"                   Event Type: {event.type}")
            print(f"                   Event Date: {event.date}")
            print("")

    else:
        print("              ----------------------------------------")
        print("")
        print("                   No open events found.")

# view open events
def view_closed_events():
    print("")
    print("                      C L O S E D   E V E N T S")
    open_events = session.query(Event).filter_by(is_active=False).all()
    if open_events:
        for event in open_events:
            print("               ----------------------------------------")
            print("")
            print(f"                   Event ID: {event.id}")
            print(f"                   Event Type: {event.type}")
            print(f"                   Event Date: {event.date}")
            print("")
    else:
        print("              ----------------------------------------")
        print("")
        print("                  No closed events found.")

# view event schedules
def view_event_schedules():
    print("")
    print("                     E V E N T   S C H E D U L E S")
    schedules = session.query(Schedule).all()
    if schedules:
        event_ids = [schedule.event_id for schedule in schedules]
        events = session.query(Event).filter(Event.id.in_(event_ids)).all()
        for event in events:
            print("               ----------------------------------------")
            print("")
            print(f"                   Event ID: {event.id}")
            print(f"                   Event Name: {event.type}")
            print(f"                   Event Description: {event.description}")
            print(f"                   Event Date: {event.date}")
            print("")
            print("                   Positions and Staff:")

            positions = session.query(Position).all()
            for position in positions:
                position_schedules = [schedule for schedule in schedules if schedule.event_id == event.id and schedule.position_id == position.id]
                if position_schedules:
                    print("")
                    print(f"                      Position ID: {position.id}")
                    print(f"                      Position Name: {position.name}")

                    staff_ids = [schedule.staff_id for schedule in position_schedules]
                    staff_records = session.query(Staff).filter(Staff.id.in_(staff_ids)).all()
                    if staff_records:
                        for staff in staff_records:
                            print(f"                      - {staff.first_name} {staff.last_name}")
                    else:
                        print("                      No staff scheduled for this position.")

            print("")  # Add empty line between events

    else:
        print("              ----------------------------------------")
        print("")
        print("                  No event schedules found.")
# view staff by position
def staff_by_position():
    print("")
    print("                      S T A F F   B Y   P O S I T I O N")
    positions = session.query(Position).all()
    for position in positions:
        print("")
        print(f"                                        {position.name.upper()}")
        # print(Figlet(font = "digital").renderText(f'POSITION : {position.name.upper()}'))
        print("")
        print("              -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        # print(f"Position: {position.name}")
        staff = session.query(Staff).filter_by(position_id=position.id).all()
        if staff:
            for user in staff:

                print(f"                  {user.id} : {user.first_name} {user.last_name}")
                print("              ------------------------------------------")
        else:
            print("")
            print("                  No staff found for this position.")
            print("                  Consider hiring some.")
            print("")
            print("                ------------------------------------------")