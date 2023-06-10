# Staff: 
# add staff input validation to all of theese: 
#     1 - VIEW USERS - print() 
#     2 - ADD A USER - add()
#     3 - EDIT A USER - edit()
#     4 - DELETE A USER - delete() 
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import (Staff, Position)

engine = create_engine("sqlite:///db/event_manager.db")
session = Session(engine, future=True)

def test():
    print("Testing passed for User Module!")

# view staff 
def view():
    print("Printing all of your staff...")    
    print(session.query(Staff).all())

# add a staff
def add():
    print("Let's add new staff!")
    print("What is your staff member's first name?")
    staff_first_name = str(input())
    print("What is your staff member's last name?")
    staff_last_name = str(input())
    print("What position will they be working?")
    print("PLEASE ENTER A NUMBER BASED ON POSITION:")
    print(session.query(Position).all())
    staff_position = int(input())
    new_staff = Staff(first_name=staff_first_name, last_name=staff_last_name, position_id=staff_position)
    session.add(new_staff)
    session.commit()
    print("User added!")

# edit a staff
def edit():
    print("Let's edit a staff!")
    print("This is your current staff data:")
    print(session.query(Staff).all())
    print("Please enter the ID of the staff you want to edit:")
    staff_id = int(input())
    staff_data = session.query(Staff).get(staff_id)
    if staff_data != None: 
        print(staff_data)
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

            #=> edit staff first name
            if edit_choice == 1:
                print("You've selected: Edit User First Name")
                print(f"What would you like '{staff_data.first_name}' to be changed to?")
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
                        staff_data.first_name = new_first_name
                        session.commit()
                        print("Change made!")
                        check = 3            

                    if check == 2:
                        print("Oh no! Let's try that again...")
                        edit()
                edit_choice = 4

            #=> edit staff last name
            if edit_choice == 2:
                print("You've selected: Edit User Last Name")
                print(f'What would you like "{staff_data.last_name}" to be changed to?')
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
                        staff_data.last_name = new_last_name
                        print("Change made!")
                        check = 3
            

                    if check == 2:
                        print("Oh no! Let's try that again...")
                        edit()
                edit_choice = 4
            
            #=> edit staff position
            if edit_choice == 3:
                print("You've selected: Edit User Position")
                print(f'What would you like "{staff_data.position_id}" to be changed to?')
                print(session.query(Position).all())
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
                        staff_data.position_id = new_position
                        print("Change made!")
                        session.commit()
                        check = 3
                        
                    if check == 2:
                        print("Oh no! Let's try that again...")
                        edit()
                edit_choice = 4

# delete a staff 
def delete():
    print("You've selected : Delete User!")
    print("This is your current staff data:")
    print(session.query(Staff).all())
    print("Please enter the ID of the staff you want to delete.")
    print("NOTE: THIS CANNOT BE UNDONE.")
    staff_id = int(input())
    staff_data = session.query(Staff).get(staff_id)
    if staff_data != None: 
        print(staff_data)
        delete_choice = 0
        print(f'''
                Are you sure you want to permanently delete {staff_data.first_name} {staff_data.last_name}?
                You will not be able to access their records if you continue with this change.  
                    1 - YES
                    2 - NO
                ''')
        #=> would like to add a query and check that blocks this activity if staff is scheduled to work an open event 
        delete_choice = int(input())
        while delete_choice !=3:
            if delete_choice == 1:
                session.delete(staff_data)
                print(f"{staff_data.first_name} {staff_data.last_name} has been permanently deleted.")
                session.commit()
                delete_choice = 3
                
                
            if delete_choice == 2:
                print("Oh no! Let's try that again...")
                delete()
    
        delete_choice = 3
            
        