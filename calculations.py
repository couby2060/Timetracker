from typing import List, Dict
from collections import defaultdict
from time_utils import round_up_to_nearest_quarter


def compute_total_time(records: List[Dict[str, str]]) -> int:
    """Compute the total time from the time records."""
    return sum(int(float(record["Duration"])) for record in records)


def compute_customer_time(records: List[Dict[str, str]]) -> Dict[str, int]:
    """Compute the total time for each customer from the time records."""
    customer_time = {}
    for record in records:
        customer = record["Kunde"]
        if customer not in customer_time:
            customer_time[customer] = 0
        customer_time[customer] += int(float(record["Duration"]))
    return {
        customer: round_up_to_nearest_quarter(time)
        for customer, time in customer_time.items()
    }


def compute_project_time(records: List[Dict[str, str]]) -> Dict[str, int]:
    """Compute the total time for each project from the time records."""
    project_time = {}
    for record in records:
        project = record["Kunde"] + " / " + record["Projekt"]
        if project not in project_time:
            project_time[project] = 0
        project_time[project] += int(float(record["Duration"]))
    return {
        project: round_up_to_nearest_quarter(time)
        for project, time in project_time.items()
    }


def calculate_totals(records: List[Dict[str, str]]) -> Dict[str, Dict[str, int]]:
    """Calculate the total time for each customer and project."""
    totals = defaultdict(lambda: defaultdict(int))
    for record in records:
        duration = int(record["Duration"])
        totals[record["Kunde"]]["total"] += duration
        totals[record["Kunde"]][record["Projekt"]] += duration
    return totals
