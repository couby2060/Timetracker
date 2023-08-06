import csv
import datetime
import os
from typing import Dict, Optional

TIME_RECORDS_DIR = 'time_records'

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
