# Updated tt.py file
# Here I have updated the script to stop the time tracking for the first project and start the time tracking for the second project when you switch projects.
# Also, now you select the customer first and then the project.

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
        reader = csv.DictReader(file, delimiter=';')
        records = sorted(list(reader), key=lambda k: (k['Kunde'].lower(), k['Projekt'].lower()))  # Sort records
    return records


def select_customer(records: List[Dict[str, str]]) -> Optional[str]:
    """Ask the user to select a customer."""
    customers = sorted(list(set(record['Kunde'] for record in records)), key=str.lower)  # Get sorted list of unique customers
    print('Please select a customer.')
    for i, customer in enumerate(customers):
        print(f"{i+1}. {customer}")
    try:
        choice = int(input('Input the number of your selection: '))
    except ValueError:
        print('Invalid input. Please input a number.')
        return None
    if choice < 1 or choice > len(customers):
        print(f'Invalid input. Please input a number between 1 and {len(customers)}.')
        return None
    return customers[choice-1]


def select_project(records: List[Dict[str, str]], customer: str) -> Optional[str]:
    """Ask the user to select a project."""
    projects = sorted([record['Projekt'] for record in records if record['Kunde'] == customer], key=str.lower)  # Get sorted list of projects for the selected customer
    print('Please select a project.')
    for i, project in enumerate(projects):
        print(f"{i+1}. {project}")
    try:
        choice = int(input('Input the number of your selection: '))
    except ValueError:
        print('Invalid input. Please input a number.')
        return None
    if choice < 1 or choice > len(projects):
        print(f'Invalid input. Please input a number between 1 and {len(projects)}.')
        return None
    return projects[choice-1]


def start_time_tracking(filename: str, customer: str, project: str) -> Dict[str, str]:
    """Start time tracking and return the start record."""
    start_time = datetime.datetime.now()
    start_record = {
        'Starttime': start_time.strftime('%Y-%m-%d %H:%M:%S'),
        'Kunde': customer,
        'Projekt': project
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
        'Kunde': start_record['Kunde'],
        'Projekt': start_record['Projekt']
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

    print(f"Stopped time tracking for {time_record['Kunde']} / {time_record['Projekt']} at {stop_time.strftime('%H:%M:%S')}. Duration: {duration} minutes.")


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
