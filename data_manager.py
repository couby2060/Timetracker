import csv
import os
from typing import List, Dict

PROJECTS_FILE = 'projects.csv'

def load_projects(filename: str) -> List[Dict[str, str]]:
    """Load projects from the CSV file."""
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print('No customers found. Please create a customer first.')
        return []
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        records = sorted(list(reader), key=lambda k: (k['Kunde'].lower(), k['Projekt'].lower()))  # Sort records
    
    return records

def write_projects(filename: str, records: List[Dict[str, str]]) -> None:
    """Write projects to the CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Kunde', 'Projekt'])
        for record in records:
            writer.writerow([record['Kunde'], record['Projekt']])

def load_time_records(filename: str) -> List[Dict[str, str]]:
    """Load time records from the CSV file."""
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        records = list(reader)
    return records
