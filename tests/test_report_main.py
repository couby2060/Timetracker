import sys
import pytest
import os

# Add the parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from report_main import main
from data_manager import load_time_records
from collections import defaultdict
from calculations import compute_total_time, compute_customer_time, compute_project_time, calculate_totals
from reporting import write_report_to_file, print_report, TIME_RECORDS_REPORTS_DIR
from ui import select_report_file
from time_tracker import TIME_RECORDS_DIR


def test_calculate_totals():
    records = [
        {
            "customer": "Customer 1",
            "project": "Project 1",
            "start_time": "2023-03-08T10:00:00",
            "end_time": "2023-03-08T11:00:00",
            "duration": 60,
        },
        {
            "customer": "Customer 2",
            "project": "Project 2",
            "start_time": "2023-03-09T10:00:00",
            "end_time": "2023-03-09T11:00:00",
            "duration": 60,
        },
    ]

    totals = defaultdict(lambda: defaultdict(int))
    for record in records:
        if "Duration" not in record:
            record["Duration"] = 0
        totals["Customer 1"][record["project"]] += record["duration"]
        totals["Customer 2"][record["project"]] += record["duration"]

    assert totals["Customer 1"]["Project 1"] == 60
    assert totals["Customer 2"]["Project 2"] == 60