import csv
import os

def load_projects(filename):
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print('No customers found. Please create a customer first.')
        return []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        records = list(reader)
    return records

def write_projects(filename, records):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Kunde', 'Projekt'])
        for record in records:
            writer.writerow([record['Kunde'], record['Projekt']])

def print_customers(records):
    print('Current customers:')
    customers = sorted(set(record['Kunde'] for record in records), key=str.lower)
    for i, customer in enumerate(customers, start=1):
        print(f"{i}. {customer}")
    print('-----------------------------')

def print_projects(records):
    print('Current customers and projects:')
    records_sorted = sorted(records, key=lambda record: (record['Kunde'].lower(), record['Projekt'].lower()))
    for i, record in enumerate(records_sorted, start=1):
        print(f"{i}. {record['Kunde']} / {record['Projekt']}")
    print('-----------------------------')

def delete_customer(records):
    print_customers(records)
    delete_index = input('Input the number of the customer you want to delete or type "back" to go back: ')
    if delete_index.lower() == 'back' or not delete_index:
        return records
    delete_customer = sorted(set(record['Kunde'] for record in records), key=str.lower)[int(delete_index) - 1]
    records = [record for record in records if record['Kunde'] != delete_customer]
    return records

def delete_project(records):
    records_sorted = sorted(records, key=lambda record: (record['Kunde'].lower(), record['Projekt'].lower()))
    print_projects(records_sorted)
    delete_index = input('Input the number of the project you want to delete or type "back" to go back: ')
    if delete_index.lower() == 'back' or not delete_index:
        return records
    records_sorted.pop(int(delete_index) - 1)
    return records_sorted

def add_customer(records):
    new_customer = input('Input the name of the new customer or type "back" to go back: ')
    if new_customer.lower() == 'back':
        return records
    while not new_customer.strip():
        new_customer = input('Input is empty. Please input the name of the new customer: ')
    new_project = input('Input the name of the first project for this customer: ')
    while not new_project.strip():
        new_project = input('Input is empty. Please input the name of the first project for this customer: ')
    records.append({'Kunde': new_customer, 'Projekt': new_project})
    while input('Do you want to add another project for this customer? (y/n) ') == 'y':
        new_project = input('Input the name of the new project: ')
        while not new_project.strip():
            new_project = input('Input is empty. Please input the name of the new project: ')
        records.append({'Kunde': new_customer, 'Projekt': new_project})
    return records

def add_project(records):
    print_customers(records)
    customer_index = input('Input the number of the customer for the new project or type "back" to go back: ')
    if customer_index.lower() == 'back' or not customer_index:
        return records
    new_customer = sorted(set(record['Kunde'] for record in records), key=str.lower)[int(customer_index) - 1]
    new_project = input('Input the name of the new project: ')
    while not new_project.strip():
        new_project = input('Input is empty. Please input the name of the new project: ')
    records.append({'Kunde': new_customer, 'Projekt': new_project})
    while input('Do you want to add another project for this customer? (y/n) ') == 'y':
        new_project = input('Input the name of the new project: ')
        while not new_project.strip():
            new_project = input('Input is empty. Please input the name of the new project: ')
        records.append({'Kunde': new_customer, 'Projekt': new_project})
    return records

if __name__ == "__main__":
    print('Welcome to the project maintenance app.')

    csv_file = 'projects.csv'
    records = load_projects(csv_file)

    while True:
        print('1. Add customer')
        print('2. Add project')
        if records:
            print('3. Delete customer')
            print('4. Delete project')
            print('5. Show customers')
            print('6. Show projects')
        print('7. Exit')
        try:
            choice = int(input('What do you want to do? Input the number of your selection: '))
        except ValueError:
            print('Invalid input. Please enter a number from 1 to 7.')
            continue

        if choice == 1:
            records = add_customer(records)
            write_projects(csv_file, records)
        elif choice == 2:
            records = add_project(records)
            write_projects(csv_file, records)
        elif choice == 3 and records:
            records = delete_customer(records)
            write_projects(csv_file, records)
        elif choice == 4 and records:
            records = delete_project(records)
            write_projects(csv_file, records)
        elif choice == 5 and records:
            print_customers(records)
        elif choice == 6 and records:
            print_projects(records)
        elif choice == 7:
            break

    print('Thank you for using the project maintenance app.')
