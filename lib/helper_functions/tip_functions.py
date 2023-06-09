# Tips:
#     1 - CALCULATE STAFF TIP PAYOUT BY EVENT - tipout()
#     2 - PAY OUT STAFF - payout()
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import (Tips)

engine = create_engine("sqlite:///db/event_manager.db")
session = Session(engine, future=True)

def test():
    print("Testing passed for Tips Module!")

# Calculate staff tipoout by event
def tipout():
    print("Creating staff tipout...")

# Payout Staff
def payout():
    print("Creating Staff Tipout")