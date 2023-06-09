import sys
import importlib
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import (Events)

engine = create_engine("sqlite:///db/event_manager.db")
session = Session(engine, future=True)

sys.path.append('./helper_functions')

user_functions = importlib.import_module('user_functions')
position_functions = importlib.import_module('position_functions')
event_functions = importlib.import_module('event_functions')
tip_functions = importlib.import_module('tip_functions')
reporting_functions = importlib.import_module('reporting_functions')

# rerouting after user requested action has been completed
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
    # enter main menu choice options
    choice = 0
    while choice != 6:
        print("***EVENT MANAGER***")
        print("Hello...")
        print('''
                What module would you like to enter? 
                    1 - USERS 
                    2 - POSITIONS
                    3 - EVENTS
                    4 - STAFF TIPS
                    5 - REPORTS
                    6 - EXIT
        ''')

        choice = int(input()) 

        # enter users module (1)
        
        if choice == 1:
            user_choice = 0  
            while user_choice != 5:
                print("Entering Users' Module...")
                print('''
                What would you like to do?
                    1 - VIEW USERS
                    2 - ADD A USER
                    3 - EDIT A USER
                    4 - DELETE A USER
                    5 - GO BACK TO MAIN MENU
                ''')

                user_choice = int(input())

                if user_choice == 1:
                    user_functions.view() 
                    reroute()

                if user_choice == 2:
                    user_functions.add()
                    reroute()

                if user_choice == 3:
                    user_functions.edit()
                    reroute()

                if user_choice == 4:
                    user_functions.delete()
                    reroute()

        ## enter positions module (2)
        
        if choice == 2:
            position_choice = 0
            while position_choice != 5:
                print("Entering Positions' Module...")
                print('''
                What would you like to do?
                    1 - VIEW POSITIONS
                    2 - ADD A POSITION
                    3 - EDIT POSITION TIP OUT PERCENTAGE
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

        ## enter events module (3)        
        
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
                            

        ## enter staff tips module (4)
        if choice == 4:
            staff_tips_choice = 0
            while staff_tips_choice != 3:
                print("Entering Staff Tips' Module...")
                print('''
                What would you like to do?
                    1 - CALCULATE STAFF TIP PAYOUT BY EVENT
                    2 - PAY OUT STAFF
                    3 - GO BACK TO MAIN MENU
                ''')

                staff_tips_choice = int(input())

                if staff_tips_choice == 1:
                    tip_functions.tipout()
                    reroute()
                
                if staff_tips_choice == 2:
                    tip_functions.payout()
                    reroute()

        ## enter reporting module (5)
        reports_choice = 0
        if choice == 5:
            while reports_choice != 6:
                print("Entering Reporting Module...")
                print('''
                What report would you like to see?
                    1 - VIEW TIP TOTALS BY EVENT
                    2 - CALCULATE USER WAGE YTD
                    3 - CALCULATE PAYROLL COST
                    4 - VIEW OPEN EVENTS
                    5 - VIEW STAFF BY POSITIONS
                    6 - GO BACK TO MAIN MENU
                ''')

                reports_choice = int(input())

                if reports_choice == 1:
                    reporting_functions.tips_by_event()
                    reroute()
                
                if reports_choice == 2:
                    reporting_functions.wage_ytd()
                    reroute()

                if reports_choice == 3:
                    reporting_functions.payroll_cost()
                    reroute()

                if reports_choice == 4:
                    reporting_functions.view_open_events()
                    reroute()

                if reports_choice == 5:
                    reporting_functions.staff_by_position()
                    reroute()


if __name__ == "__main__":
    main()

# Helper Functions By Module Key: location = /lib/helper_functions
# User Module (Main menu choice = 1): user_functions.py
# 1 - VIEW USERS - view()
# 2 - ADD A USER - add()
# 3 - EDIT A USER - edit()
# 4 - DELETE A USER - delete()

# Position Module (Main menu choice = 2): position_functions.py
# 1 - VIEW POSITIONS - view()
# 2 - ADD A POSITION - add()
# 3 - EDIT POSITION TIP OUT PERCENTAGE - edit()
# 4 - DELETE A POSITION - delete()

# Event Module (Main menu choice = 3): event_functions.py 
# 1 - CREATE AN EVENT - add()
# 2 - CREATE AN EVENT STAFF SCHEDULE - create_schedule()
# 3 - EDIT AN EVENT STAFF SCHEDULE - edit_schedule()
# 4 - CLOSE OUT AN EVENT - closeout()
# 5 - VIEW EVENT HISTORY - view()

# Tips Module (Main menu choice = 4): tip_functions.py
# 1 - CALCULATE STAFF TIP PAYOUT BY EVENT - tipout()
# 2 - PAY OUT STAFF - payout()

# Reporting Module (Main menu choice = 5): reporting_functions.py
# 1 - VIEW TIP TOTALS BY EVENT - tips_by_event()
# 2 - CALCULATE USER WAGE YTD - wage_ytd()
# 3 - CALCULATE PAYROLL COST - payroll_cost()
# 4 - VIEW OPEN EVENTS - view_open_events()
# 5 - VIEW STAFF BY POSITIONS - staff_by_position()
