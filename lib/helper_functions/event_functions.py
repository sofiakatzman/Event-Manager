# Event:
#     1 - CREATE AN EVENT - add()
#     2 - CREATE AN EVENT STAFF SCHEDULE - create_schedule()
#     3 - EDIT AN EVENT STAFF SCHEDULE - edit_schedule()
#     4 - CLOSE OUT AN EVENT - closeout()

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import (Events)

engine = create_engine("sqlite:///db/event_manager.db")
session = Session(engine, future=True)

def test():
    print('Entering Event Module...')

# create an event
def add_event():
    print("Creating an Event...")

# create a staff schedule 
def create_schedule():
    print("Creating a Schedule...")

# edit an event schedule
def edit_schedule():
    print("Editing a Schedule...")

# close out an event
def closeout():
    print("Closing out an event...")


def view():
    print("Printing Event History...")    
    print(session.query(Events).all())
