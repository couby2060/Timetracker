from typing import List, Dict
from ui import display_projects, display_customers


def delete_customer(records: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Delete a customer and all their projects."""
    display_customers(records)
    delete_index = input(
        'Input the number of the customer you want to delete or type "back" to go back: '
    )
    if delete_index.lower() == "back" or not delete_index:
        return records

    delete_customer = sorted(set(record["Kunde"] for record in records), key=str.lower)[
        int(delete_index) - 1
    ]
    records = [record for record in records if record["Kunde"] != delete_customer]

    return records


def delete_project(records: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Delete a specific project."""
    records_sorted = sorted(
        records, key=lambda record: (record["Kunde"].lower(), record["Projekt"].lower())
    )
    display_projects(records_sorted)
    delete_index = input(
        'Input the number of the project you want to delete or type "back" to go back: '
    )
    if delete_index.lower() == "back" or not delete_index:
        return records
    records_sorted.pop(int(delete_index) - 1)

    return records_sorted


def add_customer(records: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Add a new customer and their first project."""
    new_customer = input(
        'Input the name of the new customer or type "back" to go back: '
    )
    if new_customer.lower() == "back":
        return records
    while not new_customer.strip():
        new_customer = input(
            "Input is empty. Please input the name of the new customer: "
        )

    new_project = input("Input the name of the first project for this customer: ")
    while not new_project.strip():
        new_project = input(
            "Input is empty. Please input the name of the first project for this customer: "
        )

    records.append({"Kunde": new_customer, "Projekt": new_project})
    while input("Do you want to add another project for this customer? (y/n) ") == "y":
        new_project = input("Input the name of the new project: ")
        while not new_project.strip():
            new_project = input(
                "Input is empty. Please input the name of the new project: "
            )
        records.append({"Kunde": new_customer, "Projekt": new_project})

    return records


def add_project(records: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Add a new project for an existing customer."""
    display_customers(records)
    customer_index = input(
        'Input the number of the customer for the new project or type "back" to go back: '
    )
    if customer_index.lower() == "back" or not customer_index:
        return records

    new_customer = sorted(set(record["Kunde"] for record in records), key=str.lower)[
        int(customer_index) - 1
    ]
    new_project = input("Input the name of the new project: ")
    while not new_project.strip():
        new_project = input(
            "Input is empty. Please input the name of the new project: "
        )
    records.append({"Kunde": new_customer, "Projekt": new_project})
    while input("Do you want to add another project for this customer? (y/n) ") == "y":
        new_project = input("Input the name of the new project: ")
        while not new_project.strip():
            new_project = input(
                "Input is empty. Please input the name of the new project: "
            )
        records.append({"Kunde": new_customer, "Projekt": new_project})

    return records
