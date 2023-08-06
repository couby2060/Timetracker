from data_manager import load_time_records
from calculations import compute_total_time, compute_customer_time, compute_project_time, calculate_totals
from reporting import write_report_to_file, print_report, TIME_RECORDS_REPORTS_DIR

import sys
import os

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

