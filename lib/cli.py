def main():
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

        choice = int(input())  # Move the input statement inside the loop
        user_choice = 0  # Move the initialization outside the outer loop
        position_choice = 0
        events_choice = 0
        staff_tips_choice = 0
        reports_choice = 0
    ## enter users module (1)
        if choice == 1:
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
                    pass
                
                if user_choice == 2:
                    pass

                if user_choice == 3:
                    pass

                if user_choice == 4:
                    pass


    ## enter positions module (2)
        if choice == 2:
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
                    pass
                
                if position_choice == 2:
                    pass

                if position_choice == 3:
                    pass

                if position_choice == 4:
                    pass
        

    ## enter events module (3)
        if choice == 3:
            while events_choice != 5:
                print("Entering Events' Module...")
                print('''
                What would you like to do?
                    1 - CREATE AN EVENT
                    2 - CREATE AN EVENT STAFF SCHEDULE
                    3 - EDIT AN EVENT STAFF SCHEDULE
                    4 - CLOSE OUT AN EVENT
                    5 - GO BACK TO MAIN MENU
                ''')

                events_choice = int(input())

                if events_choice == 1:
                    pass
                
                if events_choice == 2:
                    pass

                if events_choice == 3:
                    pass

                if events_choice == 4:
                    pass


    ## enter staff tips module (4)
        if choice == 4:
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
                    pass
                
                if staff_tips_choice == 2:
                    pass


    ## enter reporting module (5)
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
                    pass
                
                if reports_choice == 2:
                    pass

                if reports_choice == 3:
                    pass

                if reports_choice == 4:
                    pass

                if reports_choice == 4:
                    pass


if __name__ == "__main__":
    main()