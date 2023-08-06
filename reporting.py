from typing import List, Dict
from calculations import compute_total_time, compute_customer_time, compute_project_time
from time_utils import minutes_to_hhmm


TIME_RECORDS_REPORTS_DIR = 'time_records_reports'

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
