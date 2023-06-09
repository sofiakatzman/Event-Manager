# Reporting:
#     1 - VIEW TIP TOTALS BY EVENT - tips_by_event() - REMOVE
#     2 - CALCULATE USER WAGE YTD - wage_ytd() - REMOVE 
#     3 - CALCULATE PAYROLL COST - payroll_cost() - REMOVE 
#     4 - VIEW OPEN EVENTS - view_open_events()
#     5 - VIEW STAFF BY POSITIONS - staff_by_position()

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Events, Positions, Users, Tips, Schedules

engine = create_engine("sqlite:///db/event_manager.db")
session = Session(engine, future=True)

def test():
    print("Testing passed for Reporting Module!")

# view tip totals by event
def tips_by_event():
    print("Viewing tip totals by event...")
    print("Enter the ID of the event:")
    event_id = int(input())
    event = session.query(Events).get(event_id)
    if event is not None:
        # Perform the logic to calculate and display tip totals for the event
        tips = session.query(Tips).filter_by(event_id=event_id).all()
        if tips:
            for tip in tips:
                user = session.query(Users).get(tip.user_id)
                print(f"User: {user.first_name} {user.last_name}")
                print(f"Tip Amount: {tip.tipout_amount}")
        else:
            print("No tips found for this event.")
    else:
        print("Event not found.")

# calculate user wage YTD
def wage_ytd():
    pass
#     print("Calculating user wage YTD...")
#     print("Enter the ID of the user:")
#     user_id = int(input())
#     user = session.query(Users).get(user_id)
#     if user is not None:
#         # Perform the logic to calculate and display the user's wage year-to-date
#         schedules = session.query(Schedules).filter_by(user_id=user_id).all()
#         wage_ytd = 0
#         for schedule in schedules:
#             wage_ytd += schedule.position.tipout_percent
#         print(f"Wage Year-to-Date for {user.first_name} {user.last_name}: {wage_ytd}")
#     else:
#         print("User not found.")

# calculate payroll cost
def payroll_cost():
    pass

# view open events
def view_open_events():
    print("Displaying Open Events...")
    open_events = session.query(Events).filter_by(is_active=True).all()
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
    positions = session.query(Positions).all()
    for position in positions:
        print(f"Position: {position.name}")
        staff = session.query(Users).filter_by(position_id=position.id).all()
        if staff:
            for user in staff:
                print(f"User: {user.first_name} {user.last_name}")
        else:
            print("No staff found for this position.")