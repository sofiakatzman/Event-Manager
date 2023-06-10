# Event:
#     1 - CREATE AN EVENT - add_event()
#     2 - CREATE AN EVENT STAFF SCHEDULE - create_schedule()
#     3 - EDIT AN EVENT STAFF SCHEDULE - edit_schedule()
#     4 - CLOSE OUT AN EVENT - closeout()

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import (Event, Schedule, Position, Tip, Staff)

engine = create_engine("sqlite:///db/event_manager.db")
session = Session(engine, future=True)

def test():
    print('Entering Event Module...')

# create an event
def add_event():
    print("Creating an Event...")
    print("Please enter an Event Type:")
    new_name = str(input())
    print("Please enter an Event Description:")
    new_description = str(input())
    print("Please enter Event Date: 00")
    new_date = str(input())
    new_event = Event(name = new_name , description = new_description , date = new_date )
    session.add(new_event)
    session.commit()

# create a staff schedule 
def create_schedule():
    print("Let's create a schedule...")
    # print all events 
    print("What event would you like to create a schedule for?")
    all_active_events = session.query(Event).filter(Event.is_active == True).all()
    print(all_active_events)
    event_selection = int(input())

    print("This is the event you've selected:")
    selected_event = session.query(Event).filter(Event.id == event_selection).first()
    print(selected_event)

    # new_schedule = Schedules()

    # iterate through the positions table positions to capture how many of each type of staff you want to hire 
    positions = session.query(Position).all()
    staff_counts = {}
    for position in positions:
        print(f"How many {position.name} staff do you want to add?")
        count = int(input())
        staff_counts[position.id] = count

    # ask user to pick staff based on position -- DICTIONARY! 
    selected_staff = {}
    for position_id, count in staff_counts.items():
        staff_time = None
        if count > 0:
            staff_time = input(f"Enter the time for {next((p.name for p in positions if p.id == position_id), '')}: ")
            print(f"Select {count} staff for {next((p.name for p in positions if p.id == position_id), '')}:")
            available_staff = session.query(Staff).filter(Staff.position_id == position_id).all()
            selected_staff[position_id] = []
            if available_staff:
                for staff in available_staff:
                    print(f"{staff.id}. {staff.first_name} {staff.last_name}")
                for _ in range(count):
                    while True:
                        staff_selection = input("Enter the ID of the staff member: ")
                        if staff_selection.isdigit():
                            staff_selection = int(staff_selection)
                            if staff_selection not in [staff.id for staff_list in selected_staff.values() for staff in staff_list if staff is not None]:
                                if staff_selection in [staff.id for staff in available_staff]:
                                    break
                                else:
                                    print("Invalid staff ID. Please try again.")
                            else:
                                print("Staff member has already been selected. Please choose a different ID.")
                        else:
                            print("Invalid input. Please enter a valid staff ID.")
                    selected_staff[position_id].append(next((staff for staff in available_staff if staff.id == staff_selection), None))
            else:
                print("No staff available for this position.")
                selected_staff[position_id] = []
        else:
            selected_staff[position_id] = []

    # create a Schedule entry per staff that uses the event name, position id, staff id, time of arrival, etc.
    for position_id, staff_list in selected_staff.items():
        if staff_list:
            for staff in staff_list:
                if staff is not None:
                    print(f"Enter the arrival time for {staff.first_name} {staff.last_name}:")
                    arrival_time = int(staff_time)
                    new_schedule = Schedule(
                        event_id=selected_event.id,
                        event_type=selected_event.type,
                        staff_id=staff.id,
                        position_id=position_id,
                        arrival_time=arrival_time
                    )
                    session.add(new_schedule)
    session.commit()
    print("Schedule created successfully!")


# edit an event schedule
def edit_schedule():
    print("Let's edit an event schedule!")
    print(f'''
          What would you like to do? 
          1 - EDIT POSITION START TIME
          2 - ADD STAFF TO AN EVENT SCHEDULE
          3 - DROP STAFF FROM AN EVENT SCHEDULE
          4 - DELETE AN ENTIRE EVENT SCHEDULE 
          5 - NEVERMIND
    ''')
    #=> THIS USER PATH NEEDS TO BE CREATED ###


# close out an event
def closeout():
    print("Let's closeout an event!")
    
    # print all active events
    active = session.query(Event).filter(Event.is_active == True).all()
    print(active)
    print("Please enter the ID of the event you would like to closeout")
    
    # find event 
    find_id = int(input())
    event = session.query(Event).filter(Event.id == find_id).first()
    print("This is the event you've selected.")

# removing concept of tipout closing, kiss - 
# print schedule for selected event 
#     event_schedule = session.query(Schedules).filter(Schedules.event_id == find_id).all()
#     print(event_schedule)
#     print("Is this the final event schedule?") 
#     # add yes / no path 

# # enter final event tip
#     print("Please enter the total tipout amount:")
#     event_tip = int(input())

# add logic that counts the amount of each type of staff 
    
    #     event_id = find_id
    #     staff = scheduled.staff_id    

    #     # find position of current scheduled employee
    #     position = session.query(Positions).filter(Positions.id == scheduled.position_id).first()    

    #     # hold the position's tipout percent in variable tip_out_percent
    #     tip_out_percent = position.tipout_percent

    #     # query amongst how many the tip will be distributed by based on that position
    #     tip_out_split = session.query(Schedules).filter(Schedules.event_id == find_id, Schedules.position_id == position.id).count()
        
    #     # calculate tipout amount for scheduled employee: 
    #     # tipout is based on total tip multiplied by the tipout percentage and then divided in the amount of employees who worked that position
    #     tip_out_amount = (event_tip * tip_out_percent) / tip_out_split 

    #     tipout_amount = tip_out_amount

    #     # create new tips entry : 
    #     Tips(event_id=event_id, staff_id=staff_id, tipout_amount=tipout_amount )
    #     session.commit()

    print("Your changes have been made!")
    # make event inactive
    event[0].is_active = False
    session.commit()

  


    # print(f'''
          
    #     Based on Total Tipout of: ${event_tip} : Each position's tipout amount is: 

    #     Position ID:
    #     Position Staff Count: 
    #     Tip Disbursement: 

    #     Would you like to continue? 

    # ''')
    # # add yes / no path 
    # # tipout = event_tip *** 

    # make event inactive

# view all event history 
def view():
    print("Printing Event History...")  
    active = session.query(Event).all()
    print(active)




 # submit tipout
    # create tipout from data: event_id, staff_id, tipout_amount + tiout amounts calculated above
    # query that will return staff  
    # for every staff memeber that is in event - create a tipout 
