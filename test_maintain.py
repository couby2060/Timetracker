import pytest
from maintain import load_projects, write_projects

def test_load_projects():
    # Setup: Create a test CSV file
    with open('test_projects.csv', 'w') as file:
        file.write('Kunde;Projekt\n')
        file.write('Customer1;Project1\n')
        file.write('Customer2;Project2\n')

    # Call the function with the test CSV file
    records = load_projects('test_projects.csv')

    # Assert that the function returns the correct data
    assert records == [{'Kunde': 'Customer1', 'Projekt': 'Project1'}, {'Kunde': 'Customer2', 'Projekt': 'Project2'}]

def test_write_projects():
    # Setup: Create some test data
    records = [{'Kunde': 'Customer1', 'Projekt': 'Project1'}, {'Kunde': 'Customer2', 'Projekt': 'Project2'}]

    # Call the function with the test data and a test CSV file
    write_projects('test_projects.csv', records)

    # Assert that the function wrote the correct data to the file
    with open('test_projects.csv', 'r') as file:
        assert file.read() == 'Kunde;Projekt\nCustomer1;Project1\nCustomer2;Project2\n'


##import pytest
##from maintain import load_projects, write_projects

##def test_load_projects():
    # Test goes here

##def test_write_projects():
    # Test goes here