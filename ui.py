import os
import datetime

from typing import List, Dict, Optional

TIME_RECORDS_DIR = "time_records"


def select_customer(records: List[Dict[str, str]]) -> Optional[str]:
    """Ask the user to select a customer."""
    customers = sorted(
        list(set(record["Kunde"] for record in records)), key=str.lower
    )  # Get sorted list of unique customers
    print("Please select a customer.")
    for i, customer in enumerate(customers):
        print(f"{i+1}. {customer}")
    try:
        choice = int(input("Input the number of your selection: "))
    except ValueError:
        print("Invalid input. Please input a number.")
        return None
    if choice < 1 or choice > len(customers):
        print(f"Invalid input. Please input a number between 1 and {len(customers)}.")
        return None
    return customers[choice - 1]


def select_project(records: List[Dict[str, str]], customer: str) -> Optional[str]:
    """Ask the user to select a project."""
    projects = sorted(
        [record["Projekt"] for record in records if record["Kunde"] == customer],
        key=str.lower,
    )  # Get sorted list of projects for the selected customer
    print("Please select a project.")
    for i, project in enumerate(projects):
        print(f"{i+1}. {project}")
    try:
        choice = int(input("Input the number of your selection: "))
    except ValueError:
        print("Invalid input. Please input a number.")
        return None
    if choice < 1 or choice > len(projects):
        print(f"Invalid input. Please input a number between 1 and {len(projects)}.")
        return None
    return projects[choice - 1]


def display_customers(records: List[Dict[str, str]]) -> None:
    """Print a list of unique customers."""
    print("Current customers:")
    customers = sorted(set(record["Kunde"] for record in records), key=str.lower)
    for i, customer in enumerate(customers, start=1):
        print(f"{i}. {customer}")
    print("-----------------------------")


def display_projects(records: List[Dict[str, str]]) -> None:
    """Print a list of customers and their projects."""
    print("Current customers and projects:")
    records_sorted = sorted(
        records, key=lambda record: (record["Kunde"].lower(), record["Projekt"].lower())
    )
    for i, record in enumerate(records_sorted, start=1):
        print(f"{i}. {record['Kunde']} / {record['Projekt']}")
    print("-----------------------------")


def select_report_file() -> str:
    files = [f for f in os.listdir(TIME_RECORDS_DIR) if f.endswith(".csv")]
    files.sort(
        key=lambda x: os.path.getmtime(os.path.join(TIME_RECORDS_DIR, x)), reverse=True
    )
    latest_files = files[:5]

    print("Select a file to generate report:")
    for i, file in enumerate(latest_files, 1):
        print(f"{i}. {file}")
    print("c. Current date")
    print("m. Manually enter filename")

    choice = input("Enter your choice: ")

    if choice.isdigit() and 1 <= int(choice) <= 5:
        return latest_files[int(choice) - 1]
    elif choice == "c":
        today = datetime.date.today()
        return f"{today:%Y_%m_%d}.csv"
    elif choice == "m":
        return input("Enter the filename: ")
    else:
        print("Invalid choice.")
        return select_report_file()
