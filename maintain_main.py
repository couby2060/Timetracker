from data_manager import load_projects, write_projects, PROJECTS_FILE
from ui import display_customers, display_projects, select_customer, select_project
from customer_project_manager import (
    add_customer,
    add_project,
    delete_customer,
    delete_project,
)


def main():
    """Main function to handle the menu and user interaction."""
    print("Welcome to the project maintenance app.")
    records = load_projects(PROJECTS_FILE)

    while True:
        print("1. Add customer")
        print("2. Add project")
        if records:
            print("3. Delete customer")
            print("4. Delete project")
            print("5. Show customers")
            print("6. Show projects")
        print("7. Exit")
        try:
            choice = int(
                input("What do you want to do? Input the number of your selection: ")
            )
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 7.")
            continue

        if choice == 1:
            records = add_customer(records)
            write_projects(PROJECTS_FILE, records)
        elif choice == 2:
            records = add_project(records)
            write_projects(PROJECTS_FILE, records)
        elif choice == 3 and records:
            records = delete_customer(records)
            write_projects(PROJECTS_FILE, records)
        elif choice == 4 and records:
            records = delete_project(records)
            write_projects(PROJECTS_FILE, records)
        elif choice == 5 and records:
            display_customers(records)
        elif choice == 6 and records:
            display_projects(records)
        elif choice == 7:
            break

    print("Thank you for using the project maintenance app.")


if __name__ == "__main__":
    main()
