# Event Manager

## Description
Event Manager is a user-friendly command-line interface that allows Event Managers to efficiently manage their staff, events, and event schedules. The inspiration behind Event Manager comes from my own experience as an event director, where I had to store records of staff data and event history.

This CLI app utilizes an SQLAlchemy database to store records, making it easier for users to view, edit, and delete staff, event, and job position data. In the future, Event Manager will incorporate event tip-out based on staff position tip-out percentage and introduce a new set of reporting capabilities.

## File Structure
- All program files, except for the README.md and Pipfile, are located inside the `/lib` folder.
- The `/lib/db` directory contains the database seed `seed.py` and the database structure `models.py`.
- The command line program itself is in `lib/cli.py`, and it can be executed by following the installation steps provided below.
- The four main functional components of Event Manager are stored in the `/lib/helper_functions/...` directory:
  - `/staff_functions.py`: Contains functions related to the staff module (selection 1 on the main menu). It allows event managers to perform basic CRUD actions on staff, such as adding, deleting, and editing staff records.
  - `/position_functions.py`: Contains functions related to the position module (selection 2 on the main menu). It provides CRUD actions for managing positions.
  - `/event_functions.py`: Contains functions related to the events module (selection 3 on the main menu). In addition to CRUD actions, this module offers advanced options such as creating event schedules and closing out events.
  - `/reporting_functions.py`: Contains functions for generating reports within the events module (selection 3 on the main menu). Event managers can easily access useful reports, including open or closed events, staff lists based on position, and active event staff schedules.

- The `/lib/db/seed.py` file contains the Python seed script responsible for populating the database with mock data. This script should be run before executing `cli.py`, as specified in the instructions below.

## Command Line Interface Structure & Functionality:
User Module (Main menu choice = 1): `user_functions.py`
  - VIEW STAFF USERS - `view()`: Displays all staff members' first and last names, staff ID number, and position ID.
  - ADD A STAFF MEMBER - `add()`: Adds a user to the database. Requires the user's first and last name, along with their position designation.
  - EDIT A STAFF MEMBER - `edit()`: Allows you to select a staff member based on their staff ID and choose which attributes to edit, such as their first name, last name, or position ID.
  - DELETE A STAFF MEMBER - `delete()`: Allows you to select a staff member based on their staff ID and permanently delete them from the database.

Position Module (Main menu choice = 2): `position_functions.py`
  - VIEW POSITIONS - `view()`: Displays all position information from the database, including each position's name and ID number.
  - ADD A POSITION - `add()`: Adds a position using a name, with the position ID number automatically generated.
  - EDIT POSITION NAME - `edit()`: Changes a position's name based on its ID number.
  - DELETE A POSITION - `delete()`: Deletes a position based on its ID number.

Event Module (Main menu choice = 3): `event_functions.py`
  - CREATE AN EVENT - `add()`: Adds an event based on the event type, event description, and date. All events are automatically set to active and must be closed out to become inactive.
  - CREATE AN EVENT STAFF SCHEDULE - `create_schedule()`: Creates an event staff schedule for any active event. You can specify the number of staff positions needed, their position-specific arrival times, and select staff members based on their current position attributes.
  - CLOSE OUT AN EVENT - `closeout()`: Closes out an event with an existing schedule. Closing out an event marks it as inactive.
  - VIEW EVENT HISTORY - `view()`: Displays the event history, including all events from the database regardless of their status.

Reporting Module (Main menu choice = 5): `reporting_functions.py`
  - VIEW OPEN EVENTS - `view_open_events()`: Shows a list of all active events.
  - VIEW CLOSED EVENTS - `view_closed_events()`: Displays a list of all closed events.
  - VIEW EVENT STAFF SCHEDULES - `view_event_schedule()`: Views the event staff schedule based on the inputted event ID.
  - VIEW STAFF BY POSITION - `staff_by_position()`: Provides a staff list categorized by position.

## Installation
To install and run Event Manager, ensure that you have Python 3 and pip installed on your system.

1. Clone this repository to your local machine and navigate to its directory.
2. Run `pipenv install` to install all the necessary package dependencies.
3. Run `pipenv shell` to enter the virtual environment.
4. Navigate to the `lib/db` directory and run `python seed.py` to populate the database with mock data.
5. Return to the `lib` directory by running `cd ..`.
6. Run `python cli.py` to start using Event Manager.

## Usage Visuals
![sample user path - main menu to positions](https://imgur.com/farRGDD.png)
![sample user path - event schedule reporting](https://imgur.com/4MVv2W3.png)

## Contributing
Pull requests for review are welcome. However, major changes are not allowed.
If you have any questions, please reach out to our support team.

## License
At the moment, licensing is not being offered for Event Manager. For any questions, please contact our support team.

## References
- [Faker](https://faker.readthedocs.io/en/master/): A library for generating fake data used for testing database functionality.
- [PyFiglet](https://pypi.org/project/pyfiglet/0.7/): A library for rendering ASCII art fonts.

## Support
For any questions or support, please reach out to katzmansof@gmail.com.

## Resources
- [Project Notes](https://docs.google.com/spreadsheets/d/1Td6hpmT3lyrD08tp3itemhTKWiJ7K3rUSjn-c6M-dqg/edit#gid=0)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
