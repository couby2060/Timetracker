import datetime
import os
from data_manager import load_projects, PROJECTS_FILE
from ui import select_customer, select_project
from time_tracker import start_time_tracking, stop_time_tracking


def main():
    """Main function to handle the command line arguments and user interaction."""
    print('Welcome to the time tracker.')
    records = load_projects(PROJECTS_FILE)

    if not records:
        run_maintain = input("Would you like to run 'maintain.py' to setup projects? (yes/no): ")
        if run_maintain.lower() == 'yes':
            os.system('python maintain.py')
            records = load_projects(PROJECTS_FILE)
        else:
            print("No projects found. Exiting...")
            return

    while True:
        print('1. Start time tracking')
        print('2. Stop time tracking')
        print('3. Exit')
        try:
            choice = int(input('What do you want to do? Input the number of your selection: '))
        except ValueError:
            print('Invalid input. Please enter a number from 1 to 3.')
            continue

        if choice == 1:
            customer = select_customer(records)
            if customer is not None:
                project = select_project(records, customer)
                if project is not None:
                    if 'start_record' in locals():
                        stop_time_tracking(datetime.datetime.now().strftime("%Y_%m_%d.csv"), start_record)
                    start_record = start_time_tracking(datetime.datetime.now().strftime("%Y_%m_%d.csv"), customer, project)
        elif choice == 2:
            if 'start_record' in locals():
                stop_time_tracking(datetime.datetime.now().strftime("%Y_%m_%d.csv"), start_record)
                del start_record
            else:
                print('Cannot stop time tracking because it has not been started.')
        elif choice == 3:
            break

    print('Thank you for using the time tracker.')


if __name__ == "__main__":
    main()