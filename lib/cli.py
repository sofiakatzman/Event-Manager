import sys
import importlib
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///db/event_manager.db")
session = Session(engine, future=True)

sys.path.append('./helper_functions')

staff_functions = importlib.import_module('staff_functions')
position_functions = importlib.import_module('position_functions')
event_functions = importlib.import_module('event_functions')
reporting_functions = importlib.import_module('reporting_functions')

# rerouting after staff requested action has been completed
def reroute():
    reroute_choice = 0
    while reroute_choice !=1:  
        print(f'''
        Would you like to stay in this module?
        1 - YES
        2 - NO - MAIN MENU 
        ''')

        reroute_choice = int(input())

        if reroute_choice == 1:
            print("Rerouting back to Previous Module Homescreen...")

        if reroute_choice == 2:
            print("Rerouting back to Main Menu...")
            main()

def main():
#=> enter main menu choice options
    choice = 0
    while choice != 5:
        print("***EVENT MANAGER***")
        print("Hello...")
        print('''
                What module would you like to enter? 
                    1 - USERS 
                    2 - POSITIONS
                    3 - EVENTS
                    4 - REPORTS
                    5 - EXIT
        ''')

        choice = int(input()) 

#=> 1 - enter staffs module
        if choice == 1:
            staff_choice = 0  
            while staff_choice != 5:
                print("Entering Staffs' Module...")
                print('''
                What would you like to do?
                    1 - VIEW USERS
                    2 - ADD A USER
                    3 - EDIT A USER
                    4 - DELETE A USER
                    5 - GO BACK TO MAIN MENU
                ''')

                staff_choice = int(input())

                if staff_choice == 1:
                    staff_functions.view() 
                    reroute()

                if staff_choice == 2:
                    staff_functions.add()
                    reroute()

                if staff_choice == 3:
                    staff_functions.edit()
                    reroute()

                if staff_choice == 4:
                    staff_functions.delete()
                    reroute()

##+> 2 - enter positions module      
        if choice == 2:
            position_choice = 0
            while position_choice != 5:
                print("Entering Positions' Module...")
                print('''
                What would you like to do?
                    1 - VIEW POSITIONS
                    2 - ADD A POSITION
                    3 - EDIT POSITION NAME
                    4 - DELETE A POSITION
                    5 - GO BACK TO MAIN MENU
                ''')

                position_choice = int(input())

                if position_choice == 1:
                    position_functions.view()
                    reroute()
                    
                if position_choice == 2:
                    position_functions.add()
                    reroute()

                if position_choice == 3:
                    position_functions.edit()
                    reroute()

                if position_choice == 4:
                    position_functions.delete()
                    reroute()

##=> 3 - enter events module     
        if choice == 3:
            events_choice = 0
            while events_choice != 6:
                print("Entering Events' Module...")
                print('''
                What would you like to do?
                    1 - CREATE AN EVENT
                    2 - CREATE AN EVENT STAFF SCHEDULE
                    3 - EDIT AN EVENT STAFF SCHEDULE
                    4 - CLOSE OUT AN EVENT
                    5 - VIEW EVENT HISTORY
                    6 - GO BACK TO MAIN MENU
                ''')

                events_choice = int(input())

                if events_choice == 1:
                    event_functions.add_event() 
                    reroute()
                
                if events_choice == 2:
                    event_functions.create_schedule()
                    reroute()

                if events_choice == 3:
                    event_functions.edit_schedule()
                    reroute()

                if events_choice == 4:
                    event_functions.closeout()
                    reroute()

                if events_choice == 5:
                    event_functions.view() 
                    reroute()
                            
##=> 4-  enter reporting module
        reports_choice = 0
        if choice == 4:
            while reports_choice != 3:
                print("Entering Reporting Module...")
                print('''
                What report would you like to see?
                    1 - VIEW OPEN EVENTS
                    2 - VIEW STAFF BY POSITIONS
                    3 - GO BACK TO MAIN MENU
                ''')

                reports_choice = int(input())


                if reports_choice == 1:
                    reporting_functions.view_open_events()
                    reroute()

                if reports_choice == 2:
                    reporting_functions.staff_by_position()
                    reroute()


if __name__ == "__main__":
    main()
