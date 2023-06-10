# Position: 
#     1 - VIEW POSITIONS - print()
#     2 - ADD A POSITION - add()
#     3 - EDIT POSITION TIP OUT PERCENTAGE - edit()
#     4 - DELETE A POSITION - delete()
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from db.models import (Position)


engine = create_engine("sqlite:///db/event_manager.db")
session = Session(engine, future=True)

def test():
    print("Testing passed for Position Module!")

# view positions 
def view():
    print("These are your saved positions & their tip percentages")
    print(session.query(Position).all())

# add a position
def add():
    print("Let's add a new position!")
    print("What is your position's title?")
    new_title = str(input())
    new_id = session.query(func.max(Position.id))
    new_position = Position(name=new_title, id=new_id.scalar()+1)
    session.add(new_position)
    session.commit()
    print(f"Congrat's! Position : {new_title} was added!")

# edit position tip out percentage
def edit():
    print("Let's edit a Tip Out Percentag!")
    print("This is your current tipout data:")
    print(session.query(Position).all())
    print("Please enter the ID of the position who's tip distribution percentage you want to edit:")
    tip_id = int(input())
    edit_tip = session.query(Position).get(tip_id)
    if edit_tip != None: 
        print(edit_tip)
        print(f"What would you like the new value of the {edit_tip.name}?")
        new_tip = int(input())
        print(f'''
        OLD TIP FOR {edit_tip.name} : {edit_tip.tipout_percent}
        NEW TIP FOR {edit_tip.name} : {new_tip}

            Is this correct?
            1 - YES
            2 - NO
        ''')
        check = int(input())
        while check != 3:
            if check == 1:
                print("Your changes have been saved!")
                edit_tip.tipout_percent = new_tip
                session.commit()
                check = 3
    
            if check == 2:
                print("Oh no! Let's try that again...")
                edit()

# delete position based on id 
def delete():
    print("Let's delete a position!")    
    print("This is your current position data:")
    print(session.query(Position).all())
    print("Please enter the ID of the position you want to delete:")
    delete_id = int(input())
    delete_position = session.query(Position).get(delete_id)
    session.delete(delete_position)
    print("Your deletion has been complete!")