# Updated tt.py file
# Here I have updated the start_time_tracking and stop_time_tracking functions to write the time records to a file in the 'time_records' directory and to use only the date as the filename.

import csv
import datetime
import os
from typing import List, Dict, Optional, Tuple

PROJECTS_FILE = 'projects.csv'
TIME_RECORDS_DIR = 'time_records'


def load_projects(filename: str) -> List[Dict[str, str]]:
    """Load projects from the CSV file."""
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        records = list(reader)
    return records


def select_customer_and_project(records: List[Dict[str, str]]) -> Optional[Tuple[str, str]]:
    """Ask the user to select a customer and a project."""
    print('Please select a customer and a project.')
    for i, record in enumerate(records):
        print(f"{i+1}. {record['Customer']} / {record['Project']}")
    try:
        choice = int(input('Input the number of your selection: '))
    except ValueError:
        print('Invalid input. Please input a number.')
        return None
    if choice < 1 or choice > len(records):
        print(f'Invalid input. Please input a number between 1 and {len(records)}.')
        return None
    return records[choice-1]['Customer'], records[choice-1]['Project']


def start_time_tracking(filename: str, customer: str, project: str) -> Dict[str, str]:
    """Start time tracking and return the start record."""
    start_time = datetime.datetime.now()
    start_record = {
        'Starttime': start_time.strftime('%Y-%m-%d %H:%M:%S'),
        'Customer': customer,
        'Project': project
    }
    print(f"Started time tracking for {customer} / {project} at {start_time.strftime('%H:%M:%S')}.")
    return start_record


def stop_time_tracking(filename: str, start_record: Dict[str, str]) -> None:
    """Stop time tracking and write the time record to a file."""
    stop_time = datetime.datetime.now()
    duration = (stop_time - datetime.datetime.strptime(start_record['Starttime'], '%Y-%m-%d %H:%M:%S')).seconds // 60
    time_record = {
        'Starttime': start_record['Starttime'],
        'Endtime': stop_time.strftime('%Y-%m-%d %H:%M:%S'),
        'Duration': str(duration),
        'Customer': start_record['Customer'],
        'Project': start_record['Project']
    }

    os.makedirs(TIME_RECORDS_DIR, exist_ok=True)
    file_path = os.path.join(TIME_RECORDS_DIR, filename)
    if os.path.exists(file_path):
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(list(time_record.values()))
    else:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(time_record.keys())
            writer.writerow(time_record.values())

    print(f"Stopped time tracking for {time_record['Customer']} / {time_record['Project']} at {stop_time.strftime('%H:%M:%S')}. Duration: {duration} minutes.")


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
            customer_project = select_customer_and_project(records)
            if customer_project is not None:
                start_record = start_time_tracking(datetime.datetime.now().strftime("%Y_%m_%d.csv"), *customer_project)
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

