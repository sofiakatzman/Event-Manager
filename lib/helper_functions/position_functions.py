from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from db.models import (Position)

engine = create_engine("sqlite:///db/event_manager.db")
session = Session(engine, future=True)

# view positions 
def view():
    print("")
    print("                      S A V E D  P O S I T I O N S")
    print("                  ------------------------------------")
    print(session.query(Position).all())

# add a position
def add():
    print("")
    print("                  Let's add a new position!")
    print("")
    print("                  What do you want to call this position?")
    new_title = str(input())
    new_id = session.query(func.max(Position.id))
    new_position = Position(name=new_title, id=new_id.scalar()+1)
    session.add(new_position)
    session.commit()
    print(f"                  Congrat's! Position {new_title} was added!")

# edit position name
def edit():
    print("")
    print("                  Let's edit a position's name!")
    print("")
    print("                      S A V E D  P O S I T I O N S ")
    print("                  ------------------------------------")
    print(session.query(Position).all())
    print("                  Please enter the ID of the position who's name you'd like to edit: ")
    edit_id = int(input("                    > : "))
    edit_id = session.query(Position).get(edit_id)
    if edit_id != None: 
        print(edit_id)
        print(f"                  What would you like the new name of {edit_id.name} to be?")
        new_name = str(input("                    > : "))
        print(f'''
                   OLD NAME : {edit_id.name}
                   NEW NAME : {new_name}

                Is this correct?
                --------------------------------------                  
                     1 : YES
                     
                     2 : NO
        ''')
        check = int(input("                    > : "))
        while check != 3:
            if check == 1:
                print("                  Your changes have been saved!")
                session.commit()
                check = 3
    
            if check == 2:
                print("                  Oh no! Let's try that again...")
                edit()

# delete position based on id 
def delete():
    print("")
    print("                  Let's delete a position!")  
    print("")  
    print("                      S A V E D  P O S I T I O N S")
    print("                  ------------------------------------")
    print(session.query(Position).all())
    print("                  Please enter the ID of the position you want to delete: ")
    delete_id = int(input("                    > : "))
    delete_position = session.query(Position).get(delete_id)
    session.delete(delete_position)
    print("                  Your deletion has been complete!")