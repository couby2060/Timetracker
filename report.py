import csv
import datetime
import math
import os
import sys

def load_time_records(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        records = list(reader)
    return records

def compute_total_time(records):
    total_minutes = sum(int(float(record['Duration'])) for record in records)
    return total_minutes

def compute_customer_time(records):
    customers = set(record['Kunde'] for record in records)
    customer_times = {customer: sum(int(float(record['Duration'])) for record in records if record['Kunde'] == customer) for customer in customers}
    return customer_times

def compute_project_time(records):
    projects = set((record['Kunde'], record['Projekt']) for record in records)
    project_times = {project: sum(int(float(record['Duration'])) for record in records if (record['Kunde'], record['Projekt']) == project) for project in projects}
    return project_times

def round_up_to_nearest_quarter(time_in_minutes):
    return math.ceil(time_in_minutes / 15) * 15

def minutes_to_hhmm(time_in_minutes):
    hours, minutes = divmod(time_in_minutes, 60)
    return f'{hours:02}:{minutes:02}'

def write_report_to_file(filename, total_time, customer_times, project_times):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Type', 'Kunde', 'Projekt', 'Time'])
        writer.writerow(['Total', '', '', minutes_to_hhmm(total_time)])
        for customer, time in customer_times.items():
            writer.writerow(['Customer', customer, '', minutes_to_hhmm(time)])
        for project, time in project_times.items():
            writer.writerow(['Project', project[0], project[1], minutes_to_hhmm(time)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} path_to_csv_file')
        sys.exit(1)

    csv_file = sys.argv[1]
    records = load_time_records(csv_file)
    total_time = compute_total_time(records)  # total time is not rounded
    customer_times = {customer: round_up_to_nearest_quarter(time) for customer, time in compute_customer_time(records).items()}
    project_times = {project: round_up_to_nearest_quarter(time) for project, time in compute_project_time(records).items()}

    print('Report:')
    print(f'Total time: {minutes_to_hhmm(total_time)}')
    print('Time per customer:')
    for customer, time in customer_times.items():
        print(f'{customer}: {minutes_to_hhmm(time)}')
    print('Time per project:')
    for project, time in project_times.items():
        print(f'{project[0]} / {project[1]}: {minutes_to_hhmm(time)}')

    report_filename = csv_file.replace('.csv', '_report.csv')
    write_report_to_file(report_filename, total_time, customer_times, project_times)
    print(f'Report saved to {report_filename}')
