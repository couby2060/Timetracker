import csv
import datetime
import os

def get_projects():
    with open('projects.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        projects = list(reader)
    return projects

def select_customer():
    projects = get_projects()
    customers = list(set([project['Kunde'] for project in projects]))

    print("\nPlease select a customer:")
    for i, customer in enumerate(customers, 1):
        print(f"{i}. {customer}")

    while True:
        selected = input("\nInput the number of your selection: ")
        if selected.isdigit() and 1 <= int(selected) <= len(customers):
            return customers[int(selected) - 1]
        else:
            print("Invalid selection. Please select a valid customer.")

def select_project(customer):
    projects = get_projects()
    customer_projects = [project for project in projects if project['Kunde'] == customer]

    print(f"\nPlease select a project for {customer}:")
    for i, project in enumerate(customer_projects, 1):
        print(f"{i}. {project['Projekt']}")

    while True:
        selected = input("\nInput the number of your selection: ")
        if selected.isdigit() and 1 <= int(selected) <= len(customer_projects):
            return customer_projects[int(selected) - 1]
        else:
            print("Invalid selection. Please select a valid project.")

class TimeTracker:
    def __init__(self):
        self.current_project = None
        self.start_time = None
        self.is_tracking = False

    def start_tracking(self, project):
        if self.is_tracking:
            self.stop_tracking()
        self.current_project = project
        self.start_time = datetime.datetime.now()
        self.is_tracking = True
        print(f"\nZeiterfassung läuft für {project['Kunde']} / {project['Projekt']} seit {self.start_time.strftime('%H:%M')} Uhr")

    def stop_tracking(self):
        if self.is_tracking:
            end_time = datetime.datetime.now()
            duration = (end_time - self.start_time).total_seconds() / 60
            self.write_to_file(self.start_time, end_time, duration, self.current_project)
            self.is_tracking = False
            print(f"Stopped tracking {self.current_project['Kunde']} / {self.current_project['Projekt']} at {end_time.strftime('%H:%M')}, duration: {duration} minutes")
        else:
            print("No project is currently being tracked.")

    def write_to_file(self, start_time, end_time, duration, project):
        date_str = datetime.datetime.now().strftime('%Y-%m-%d')
        filename = f'{date_str}_times.csv'
        if not os.path.isfile(filename):
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(['Starttime', 'Endtime', 'Duration', 'Kunde', 'Projekt'])
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([start_time.strftime('%H:%M'), end_time.strftime('%H:%M'), round(duration, 2), project['Kunde'], project['Projekt']])

tracker = TimeTracker()

if __name__ == "__main__":
    while True:
        print("\nSelect an action:")
        print("1. Start a new project")
        print("2. Stop the current project")
        print("3. Quit the program")
        action = input("\nInput the number of your selection: ")
        if action == '1':
            selected_customer = select_customer()
            selected_project = select_project(selected_customer)
            tracker.start_tracking(selected_project)
        elif action == '2':
            tracker.stop_tracking()
        elif action == '3':
            break
        else:
            print("Invalid selection. Please select a valid action.")
