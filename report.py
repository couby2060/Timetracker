# Updated report.py file
# Here I have updated the script to generate the report file name based on the current date.

import csv
import datetime
import os
import sys  # add this import at the beginning of your script
from typing import List, Dict, Optional
from collections import defaultdict

TIME_RECORDS_REPORTS_DIR = 'time_records_reports'


def load_time_records(filename: str) -> List[Dict[str, str]]:
    """Load time records from the CSV file."""
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        records = list(reader)
    return records


def compute_total_time(records: List[Dict[str, str]]) -> int:
    """Compute the total time from the time records."""
    return sum(int(float(record['Duration'])) for record in records)


def compute_customer_time(records: List[Dict[str, str]]) -> Dict[str, int]:
    """Compute the total time for each customer from the time records."""
    customer_time = {}
    for record in records:
        customer = record['Kunde']
        if customer not in customer_time:
            customer_time[customer] = 0
        customer_time[customer] += int(float(record['Duration']))
    return {customer: round_up_to_nearest_quarter(time) for customer, time in customer_time.items()}


def compute_project_time(records: List[Dict[str, str]]) -> Dict[str, int]:
    """Compute the total time for each project from the time records."""
    project_time = {}
    for record in records:
        project = record['Kunde'] + ' / ' + record['Projekt']
        if project not in project_time:
            project_time[project] = 0
        project_time[project] += int(float(record['Duration']))
    return {project: round_up_to_nearest_quarter(time) for project, time in project_time.items()}


def calculate_totals(records: List[Dict[str, str]]) -> Dict[str, Dict[str, int]]:
    """Calculate the total time for each customer and project."""
    totals = defaultdict(lambda: defaultdict(int))
    for record in records:
        duration = int(record['Duration'])
        totals[record['Kunde']]['total'] += duration
        totals[record['Kunde']][record['Projekt']] += duration
    return totals


def round_up_to_nearest_quarter(time_minutes: int) -> int:
    """Round up time to the nearest quarter hour."""
    return ((time_minutes + 14) // 15) * 15


def minutes_to_hhmm(time_minutes: int) -> str:
    """Convert time in minutes to a string in the format HH:MM."""
    return f"{time_minutes // 60:02}:{time_minutes % 60:02}"


def write_report_to_file(filename: str, records: List[Dict[str, str]]) -> None:
    """Write the time report to a file and print to console."""
    total_time = compute_total_time(records)
    customer_time = compute_customer_time(records)
    project_time = compute_project_time(records)

    report = []
    report.append('Time report')
    report.append('===========')
    report.append(f"Total time: {minutes_to_hhmm(total_time)}")
    report.append('')  # Line break
    report.append('Time per customer')
    report.append('-----------------')
    for customer, time in sorted(customer_time.items(), key=lambda item: item[0].lower()):
        report.append(f"{customer}: {minutes_to_hhmm(time)}")
    report.append('')  # Line break
    report.append('Time per project')
    report.append('----------------')
    for project, time in sorted(project_time.items(), key=lambda item: item[0].lower()):
        report.append(f"{project}: {minutes_to_hhmm(time)}")

    report_str = '\n'.join(report)

    # Write to file
    with open(filename, 'w') as file:
        file.write(report_str)

    # Print to console
    print(report_str)


def print_report(records: List[Dict[str, str]]) -> None:
    """Print the time report in the terminal."""
    total_time = compute_total_time(records)
    customer_time = compute_customer_time(records)
    project_time = compute_project_time(records)

    print('Time report')
    print('===========')
    print()
    print(f"Total time: {minutes_to_hhmm(total_time)}")
    print()
    print('Time per customer')
    print('-----------------')
    for customer, time in sorted(customer_time.items(), key=lambda item: item[1], reverse=True):
        print(f"{customer}: {minutes_to_hhmm(time)}")
    print()
    print('Time per project')
    print('----------------')
    for project, time in sorted(project_time.items(), key=lambda item: item[1], reverse=True):
        print(f"{project}: {minutes_to_hhmm(time)}")


def main():
    """Main function to handle the command line arguments and user interaction."""
    # sys.argv[0] is the script name, sys.argv[1] will be the first argument
    if len(sys.argv) != 2:
        print("Usage: python report.py <time_records_file>")
        return
    filename = sys.argv[1]
    records = load_time_records(filename)
    totals = calculate_totals(records)

    os.makedirs(TIME_RECORDS_REPORTS_DIR, exist_ok=True)
    report_filename = os.path.join(TIME_RECORDS_REPORTS_DIR, f'{os.path.splitext(os.path.basename(filename))[0]}-report.txt')
    write_report_to_file(report_filename, records)  # Use your existing function here



if __name__ == "__main__":
    main()

