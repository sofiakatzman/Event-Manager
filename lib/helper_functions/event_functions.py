# Event:
#     1 - CREATE AN EVENT - add_event()
#     2 - CREATE AN EVENT STAFF SCHEDULE - create_schedule()
#     3 - EDIT AN EVENT STAFF SCHEDULE - edit_schedule()
#     4 - CLOSE OUT AN EVENT - closeout()

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import (Events, Schedules, Positions, Tips)

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
    new_event = Events(name = new_name , description = new_description , date = new_date )
    session.add(new_event)
    session.commit()

# create a staff schedule 
def create_schedule():
    print("Creating a Schedule...")
    pass

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
    active = session.query(Events).filter(Events.is_active == "True").all()
    print(active)
    print("Please enter the ID of the event you would like to closeout")
    
    # find event 
    find_id = int(input())
    event = session.query(Events).filter(Events.id == find_id).first()
    print("This is the event you've selected.")
    
    # print schedule for selected event 
    event_schedule = session.query(Schedules).filter(Schedules.event_id == find_id).all()
    print(event_schedule)
    print("Is this the final event schedule?") 
    # add yes / no path 

# enter final event tip
    print("Please enter the total tipout amount:")
    event_tip = int(input())

# add logic that counts the amount of each type of staff 
    tips = []
    for scheduled in event_schedule:
        event_id = find_id
        user_id = scheduled.user_id    

        # find position of current scheduled employee
        position = session.query(Positions).filter(Positions.id == scheduled.position_id).first()    

        # hold the position's tipout percent in variable tip_out_percent
        tip_out_percent = position.tipout_percent

        # query amongst how many the tip will be distributed by based on that position
        tip_out_split = session.query(Schedules).filter(Schedules.event_id == find_id, Schedules.position_id == position.id).count()
        
        # calculate tipout amount for scheduled employee: 
        # tipout is based on total tip multiplied by the tipout percentage and then divided in the amount of employees who worked that position
        tip_out_amount = (event_tip * tip_out_percent) / tip_out_split 

        tipout_amount = tip_out_amount

        # create new tips entry : 
        tip = Tips(event_id=event_id, user_id=user_id, tipout_amount=tipout_amount )
        tips.add(tip)

    # make event inactive
    event.is_active = False
    session.add(tips)
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
    active = session.query(Events).all()
    print(active)




 # submit tipout
    # create tipout from data: event_id, user_id, tipout_amount + tiout amounts calculated above
    # query that will return staff  
    # for every staff memeber that is in event - create a tipout 
