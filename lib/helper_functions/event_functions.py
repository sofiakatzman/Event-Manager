from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import (Event, Schedule, Position, Staff)

engine = create_engine("sqlite:///db/event_manager.db")
session = Session(engine, future=True)

# create an event
def add_event():
    print("Let's crate an event...")
    print("Please enter an Event Type:")
    new_name = str(input())
    print("Please enter an Event Description:")
    new_description = str(input())
    print("Please enter Event Date - Follow Date Format : YEAR-MM-DD :")
    new_date = str(input())
    new_event = Event(type = new_name , description = new_description , date = new_date )
    session.add(new_event)
    session.commit()

# create a staff schedule 
def create_schedule():
    print("Let's create a schedule...")
    # print all events 
    print("Please enter the ID of the event you would like to create a schedule for:")
    all_active_events = session.query(Event).filter(Event.is_active == True).all()
    print(all_active_events)
    event_selection = int(input())

    print("You've Selected :")
    selected_event = session.query(Event).filter(Event.id == event_selection).first()
    print(selected_event)
    print("Initiating schedule creation...")

    # new_schedule = Schedules()

    # iterate through the positions table positions to capture how many of each type of staff you want to hire 
    positions = session.query(Position).all()
    staff_counts = {}
    for position in positions:
        print(f"How many {position.name} staff will you need for the event?")
        count = int(input())
        staff_counts[position.id] = count

    # ask user to pick staff based on position 
    selected_staff = {}
    for position_id, count in staff_counts.items():
        staff_time = None
        if count > 0:
            staff_time = input(f"What time should {next((p.name for p in positions if p.id == position_id), '')}s arrive? : ")
            print(f"Please pick {count} {next((p.name for p in positions if p.id == position_id), '')} to work the event :")
            available_staff = session.query(Staff).filter(Staff.position_id == position_id).all()
            selected_staff[position_id] = []
            if available_staff:
                for staff in available_staff:
                    print(f''' 
                                Staff ID: {staff.id}
                                Staff Name: {staff.first_name} {staff.last_name}
                            ''')
                for _ in range(count):
                    while True:
                        staff_selection = input("Enter the ID of the staff member youd like to book: ")
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
                print("Sorry, there is no staff available for this position. ")
                selected_staff[position_id] = []
        else:
            selected_staff[position_id] = []


    # create a Schedule entry per staff that uses the event name, position id, staff id, time of arrival, etc.
    for position_id, staff_list in selected_staff.items():
        if staff_list:
            for staff in staff_list:
                if staff is not None:
                    arrival_time = staff_time
                    new_schedule = Schedule(
                        event_id=selected_event.id,
                        event_type=selected_event.type,
                        staff_id=staff.id,
                        position_id=position_id,
                        arrival_time=arrival_time
                        )
                session.add(new_schedule)
    session.commit()
    print("Your event schedule was created successfully!")

# close out an event
def closeout():
    print("Let's closeout an event!")

    # print all active events
    print("These are your currently open events : ")
    active = session.query(Event).filter(Event.is_active == True).all()
    print(active)
    print("Please enter the ID of the event you would like to closeout : ")
    
    # find event 
    find_id = int(input())
    event = session.query(Event).filter(Event.id == find_id).first()
    print("This is the event you've selected : ")
    print(event)
    
    # are you sure you'd like to proceed?
    check = 0
    print(f'''
            Please confirm if this is correct. This action cannot be undone. 
            1 - YES
            2 - NO
        ''')
    check = int(input())
    while check != 3:
        if check == 1:
            # make event inactive
            event.is_active = False
            session.commit()
            print("Great! Your changes have been saved!")
            check = 3

        if check == 2:
            print("Oh no! Let's try that again...")
            closeout()


# view all event history 
def view():
    print("Printing Event History...")  
    active = session.query(Event).all()
    print(active)
