from data_manager import load_time_records
from calculations import compute_total_time, compute_customer_time, compute_project_time, calculate_totals
from reporting import write_report_to_file, print_report, TIME_RECORDS_REPORTS_DIR
from ui import select_report_file
from time_tracker import TIME_RECORDS_DIR

import os

def main():
    filename = select_report_file()

    records = load_time_records(filename)

    totals = calculate_totals(records)

    os.makedirs(TIME_RECORDS_REPORTS_DIR, exist_ok=True)
    report_filename = os.path.join(TIME_RECORDS_REPORTS_DIR, f'{os.path.splitext(os.path.basename(filename))[0]}-report.txt')
    write_report_to_file(report_filename, records)

if __name__ == "__main__":
    main()
