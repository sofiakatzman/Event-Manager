# User: 
# add user input validation to all of theese: 
#     1 - VIEW USERS - print() 
#     2 - ADD A USER - add()
#     3 - EDIT A USER - edit()
#     4 - DELETE A USER - delete() 
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import (Users, Positions)
from cli import main

engine = create_engine("sqlite:///db/event_manager.db")
session = Session(engine, future=True)

def test():
    print("Testing passed for User Module!")

# view users 
def view():
    print("Printing all of your staff...")    
    print(session.query(Users).all())

# add a user
def add():
    print("Let's add new staff!")
    print("What is your staff member's first name?")
    user_first_name = str(input())
    print("What is your staff member's last name?")
    user_last_name = str(input())
    print("What position will they be working?")
    print("PLEASE ENTER A NUMBER BASED ON POSITION:")
    print(session.query(Positions).all())
    user_position = int(input())
    new_user = Users(user_first_name, user_last_name, user_position)
    session.add(new_user)
    session.commit()
    print("User added!")

# edit a user
def edit():
    print("Let's edit a user!")
    print("This is your current user data:")
    print(session.query(Users).all())
    print("Please enter the ID of the user you want to edit:")
    user_id = int(input())
    user_data = session.query(Users).get(user_id)
    if user_data != None: 
        print(user_data)
        edit_choice = 0
        print(f'''
              What would you like to edit?
              1 - USER FIRST NAME
              2 - USER LAST NAME
              3 - USER POSITION
              4 - NEVERMIND
              ''')
        edit_choice = int(input())
        while edit_choice !=4:

            #=> edit user first name
            if edit_choice == 1:
                print("You've selected: Edit User First Name")
                print(f"What would you like '{user_data.first_name}' to be changed to?")
                new_first_name = str(input())
                check = 0
                print(f'''
                    Is '{new_first_name}' correct?
                    1 - YES
                    2 - NO
                ''')
                check = int(input())
                while check != 3:
                    if check == 1:
                        user_data.first_name = new_first_name
                        session.commit()
                        print("Change made! Navigating back to main menu....")
                        main()

                    if check == 2:
                        print("Oh no! Let's try that again...")
                        edit()

            #=> edit user last name
            if edit_choice == 2:
                print("You've selected: Edit User Last Name")
                print(f'What would you like "{user_data.last_name}" to be changed to?')
                new_last_name = str(input())
                check = 0
                print(f'''
                    Is '{new_last_name}' correct?
                    1 - YES
                    2 - NO
                ''')
                check = int(input())
                while check != 3:
                    if check == 1:
                        user_data.last_name = new_last_name
                        print("Change made!")
                        main()
                        
                    if check == 2:
                        print("Oh no! Let's try that again...")
                        edit()
            
            #=> edit user position
            if edit_choice == 3:
                print("You've selected: Edit User Position")
                print(f'What would you like "{user_data.position_id}" to be changed to?')
                print(session.query(Positions).all())
                new_position = int(input())
                check = 0
                print(f'''
                    Is '{new_position}' correct?
                    1 - YES
                    2 - NO
                ''')
                check = int(input())
                while check != 3:
                    if check == 1:
                        user_data.position_id = new_position
                        print("Change made!")
                        session.commit()
                        main()
                        
                    if check == 2:
                        print("Oh no! Let's try that again...")
                        edit()

# delete a user 
def delete():
    print("You've selected : Delete User!")
    print("This is your current user data:")
    print(session.query(Users).all())
    print("Please enter the ID of the user you want to delete.")
    print("NOTE: THIS CANNOT BE UNDONE.")
    user_id = int(input())
    user_data = session.query(Users).get(user_id)
    if user_data != None: 
        print(user_data)
        delete_choice = 0
        print(f'''
                Are you sure you want to permanently delete {user_data.first_name} {user_data.last_name}?
                You will not be able to access their records if you continue with this change.  
                    1 - YES
                    2 - NO
                ''')
        #=> would like to add a query and check that blocks this activity if staff is scheduled to work an open event 
        delete_choice = int(input())
        while delete_choice !=2:
                if delete_choice == 1:
                    session.delete(user_data)
                    print(f"{user_data.first_name} {user_data.last_name} has been permanently deleted.")
                    session.commit()
                    main()
                    
                if delete_choice == 2:
                    print("Oh no! Let's try that again...")
                    delete()
            
