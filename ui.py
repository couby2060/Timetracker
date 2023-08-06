from typing import List, Dict, Optional

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

def print_customers(records: List[Dict[str, str]]) -> None:
    """Print a list of unique customers."""
    print('Current customers:')
    customers = sorted(set(record['Kunde'] for record in records), key=str.lower)
    for i, customer in enumerate(customers, start=1):
        print(f"{i}. {customer}")
    print('-----------------------------')

def print_projects(records: List[Dict[str, str]]) -> None:
    """Print a list of customers and their projects."""
    print('Current customers and projects:')
    records_sorted = sorted(records, key=lambda record: (record['Kunde'].lower(), record['Projekt'].lower()))
    for i, record in enumerate(records_sorted, start=1):
        print(f"{i}. {record['Kunde']} / {record['Projekt']}")
    print('-----------------------------')

