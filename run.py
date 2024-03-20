"""
Imports
"""
import re
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project3')


# Function to check ID is valid and not a duplicate
def valid_id(id):
    """Validate that an ID is not None and not already used in Sheet1."""
    if id is None:
        return False

    id_present = False

    sheet = SHEET.worksheet('Sheet1')
    # Get all the data in the sheet
    data = sheet.get_all_values()

    # Loop through the data rows and check if the ID matches
    for i in range(1, len(data)):
        row = data[i]
        if row[0] == str(id):
            # If match found
            id_present = True

    if id_present:
        print("ID already in use. Please try again")
        return False

    return True


# Function to ensure a value is not empty
def empty_value(field_name, value):
    """Return False and report if 'value' is None or empty, True otherwise."""
    if value is None:
        return False

    if len(value) == 0:
        print(field_name + " cannot be empty")
        return False

    return True


# Function to validate an email address
def is_valid_email(email):
    """Return True if 'email' is a valid email address, False otherwise."""
    # Regular expression pattern for validating an email address
    pattern = r'^(?!.*\.\.)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        print("Invalid email format. Please enter a valid email address.")
        return False


# Function to validate a date format
def valid_date(field_name, date):
    """Checks date validity in DD/MM/YYYY format and year range 1920-2024."""
    if date is None or not date.strip():
        print(f"{field_name} cannot be empty")
        return False
    try:
        date = date.split("/")
        if (

                len(date) != 3 or
                int(date[0]) < 1 or int(date[0]) > 31 or
                int(date[1]) < 1 or int(date[1]) > 12 or
                int(date[2]) < 1920 or int(date[2]) > 2024
        ):
            print("Invalid date. Please try again")
            return False
    except ValueError:
        print("Invalid date format. Please use DD/MM/YYYY")
        return False
    return True


def is_valid_phone_number(number):
    """
    Checks if the phone number is all digits and at least 7 characters long.
    Returns False if these conditions are not met.
    """
    # Strip any spaces for a cleaner validation
    number_stripped = number.replace(" ", "")

    if not number_stripped.isdigit():
        print("Phone number must contain only digits.")
        return False

    if len(number_stripped) < 7:
        print("Phone number must be at least 7 digits.")
        return False

    return True


def add_employee(sheet_name, data):
    """
    code to add a new employee into the sheet
    """
    # Get the worksheet with the specified name
    sheet = SHEET.worksheet(sheet_name)
    # Append a new row to the worksheet with the employee data
    sheet.append_row(data)


# Function to check for invalid characters
def contains_invalid_characters(input_str):
    """
    Check if the input string contains any special characters
    """
    if re.search(r'[!@#$%^&*()+=\[\]{};:\'"\\|,.<>/?]', input_str):
        return True
    else:
        return False


def contains_digits(input_str):
    """
    Check if the input string contains any digits
    """
    if re.search(r'[0123456789]', input_str):
        return True
    else:
        return False


# Function for getting validated input
def get_valid_input(prompt, field_name):
    """
    Repeatedly ask for input until it does not contain invalid characters
    """
    while True:
        user_input = input(prompt).strip()
        try:
            if user_input == "":
                raise ValueError(f"{field_name} cannot be empty.")
            if contains_invalid_characters(user_input):
                raise ValueError("Special characters are not allowed.")
            condition = field_name != 'Department' and field_name != 'Position'
            if contains_digits(user_input) and condition:
                raise ValueError(f"The {field_name} cannot contain digits.")
            return user_input
        except ValueError as e:
            print(e)


# Function for validated salary input
def get_valid_salary(prompt):
    """
    Prompt for and return a valid, positive salary amount.

    Converts input commas to dots and checks for positive float value.
    """
    while True:
        salary_input = input(prompt).strip().replace(',', '.')
        try:
            salary = float(salary_input)
            if salary <= 0:
                raise ValueError("Salary must be greater than 0.")
            return salary
        except ValueError:
            print("Use valid number format.")


def add_employee_data():
    """
    function to add employee data from user input
    """
    # Prompt user to enter employee data
    employee_data = []

    print("Please enter employee data.")
    # Provide instructions on how to enter data.
    # ID must be unique, positive integer greater than 0
    id = None
    while not valid_id(id):
        input_str = input("Enter ID: ").strip()
        if input_str.isdigit():
            id = int(input_str)
            if id <= 0:
                print("Invalid ID. ID should be greater than 0")
                id = None
            else:

                pass
        else:
            print("Please enter a valid ID. ID must be a positive integer.")
    employee_data.append(id)

    forename = get_valid_input("Enter forename: ", "Forename")
    employee_data.append(forename)

    surname = get_valid_input("Enter surname: ", "Surname")
    employee_data.append(surname)

    email = None
    while not empty_value("Email address", email):
        email = str(input("Enter email address: ")).strip()
        if not is_valid_email(email):
            email = None
            print("Invalid email")

    employee_data.append(email)

    number = None
    while number is None:
        number_input = input("Enter phone number: ").strip()
        if is_valid_phone_number(number_input):
            number = number_input  # Validated phone number
        else:
            number = None  # Keep asking if the validation fails

    employee_data.append(number)

    department = get_valid_input("Enter department: ", "Department")
    employee_data.append(department)

    position = get_valid_input("Enter position: ", "Position")
    employee_data.append(position)

    salary = get_valid_salary("Enter annual salary: ")
    employee_data.append(salary)

    start_date = None
    while not valid_date("Start Date", start_date):
        start_date = str(input("Enter start date [dd/mm/yyyy]: ")).strip()

    employee_data.append(start_date)

    # Calculate monthly salary by dividing annual salary by 12
    monthly_salary = salary / 12
    # Append the monthly salary value to the employee data list
    employee_data.append(round(monthly_salary, 2))
    # Call the add_employee function to add the employee data to the spredsheet
    add_employee('Sheet1', employee_data)

    print("Employee data added successfully")


def print_employee_data(row):
    """
    Display formatted employee data.
    """
    print("\n")
    print("ID: " + row[0])
    print("Forename: " + row[1])
    print("Surname: " + row[2])
    print("Email address: " + row[3])
    print("Telephone Number: " + row[4])
    print("Department: " + row[5])
    print("Position: " + row[6])
    print("Annual Salary: " + row[7])
    print("Start date: " + row[8])
    print("Monthly Salary: " + row[9])


def search_employee_data():
    """
    Searches for employee data based on ID and prints the row if found.
    """
    id = None
    while id is None:
        id_input = input("Enter ID: ").strip()
        if id_input.isdigit():
            id = int(id_input)
            sheet = SHEET.worksheet('Sheet1')
            data = sheet.get_all_values()
            found = False
            for row in data[1:]:
                if row[0] == str(id):
                    print_employee_data(row)
                    found = True
                    break
            if not found:
                print("No matching data was found for the ID.")
        else:
            print("Invalid ID. Please enter a numeric ID.")
            id = None
    # Open the Sheet1 worksheet and get all data
    sheet = SHEET.worksheet('Sheet1')

    data = sheet.get_all_values()

    # Iterate through each row in data and check if ID matches
    for row in data[1:]:
        if row[0] == str(id):
            # print row data if ID matches
            print_employee_data(row)
            return
    # If no match found, print message
    print("No matching data was found for the ID")


def edit_employee_data():
    """
    Code to edit the details of an existing employee
    """
    while True:
        # Get the ID of the employee to be edited
        id = None
        while id is None:
            id_input = input("Enter ID to edit: ").strip()
            if not id_input:
                print("ID cannot be empty.")
                continue
            try:
                id = int(id_input)
                if id < 1:
                    print("Invalid ID.")
                    continue
            except ValueError:
                print("Please enter a valid ID")

        # Get the worksheet 'Sheet1'
        sheet = SHEET.worksheet('Sheet1')
        # Get all the data from the worksheet
        data = sheet.get_all_values()

        # Find the row to be edited
        editing_row = None
        for i, row in enumerate(data):
            if row[0] == str(id):
                editing_row = i
                break

        if editing_row is None:
            # If no matching data is found
            print("No matching data found. Please try again.")
            continue  # Continue to prompt for ID input

        # Retrieve current data for the row to be edited
        current_data = data[editing_row]

        # Function to prompt for field update
        def prompt_field_update(field_name):
            value = None
            while value is None:
                input_value = input(f"Enter updated {field_name} or press enter to skip: ").strip()
                if not input_value:
                    break  # Break the loop if input is empty

                if field_name == 'Forename' or field_name == 'Surname':
                    # Allow letters and hyphens only. Disallow digits and other special characters.
                    if not re.match("^[A-Za-z-]+$", input_value):
                        print(f"{field_name} can only contain letters and hyphens.")
                        continue

                if field_name == 'Email address':
                    if not is_valid_email(input_value):
                        print("Invalid email format. Please enter a valid email address.")
                        continue

                if field_name == 'Phone number':
                    if not is_valid_phone_number(input_value):
                        print("Invalid phone number format. Please enter a valid phone number.")
                        continue

                if field_name == 'Department':
                    if not re.match("^[A-Za-z0-9 \-]+$", input_value):
                        print(f"{field_name} cannot contain special characters.")
                        continue

                if field_name == 'Position':
                    if not re.match("^[A-Za-z0-9 \-]+$", input_value):
                        print(f"{field_name} cannot contain special characters.")
                        continue

                if field_name == 'Annual salary':
                    try:
                        salary = float(input_value.replace(',', '.'))
                        if salary <= 0:
                            print("Salary must be greater than 0.")
                            continue
                    except ValueError:
                        print("Invalid number format for salary.")
                        continue

                if field_name == 'Start date':
                    if not valid_date(field_name, input_value):
                        print("Invalid date format. Please use DD/MM/YYYY.")
                        continue

                value = input_value

            return value

        # Prompt for updates, only if input is provided
        fields_to_update = ["Forename", "Surname", "Email address", "Phone number",
                            "Department", "Position", "Annual salary", "Start date"]

        updated_values = []
        for field in fields_to_update:
            updated_value = prompt_field_update(field)
            updated_values.append(updated_value)

        # Update fields if new values were entered
        for i, updated_value in enumerate(updated_values):
            if updated_value:
                sheet.update_cell(editing_row + 1, i + 2, updated_value)

        # Update monthly salary if annual salary was updated
        if updated_values[6]:
            salary = float(updated_values[6].replace(',', '.'))
            updated_monthly_salary = round(salary / 12, 2)
            sheet.update_cell(editing_row + 1, 10, updated_monthly_salary)

        print("Editing complete.")
        break


def delete_employee():
    """
    Code to delete an employee from the sheet.
    """
    # Ask user for the employee ID to be deleted
    while True:
        id_input = input("Enter ID to delete: ").strip()
        if not id_input:
            print("ID cannot be empty.")
            continue
        try:
            id = int(id_input)
            if id < 1:
                print("Invalid ID. ID should be greater than 0.")
                continue
        except ValueError:
            print("Invalid ID. Please enter a numeric ID.")
            continue

        # Get the sheet
        sheet = SHEET.worksheet('Sheet1')
        # Get all the data in the sheet
        data = sheet.get_all_values()

        # Check if the ID exists in the sheet
        id_exists = False
        for row in data[1:]:
            if row[0] == str(id):
                id_exists = True
                break

        if id_exists:
            # Loop through the data rows and check if the ID matches
            for i in range(1, len(data)):
                row = data[i]
                if row[0] == str(id):
                    # If match found, delete the row and print message
                    sheet.delete_rows(i + 1)
                    print("Data deleted.")
                    return
        else:
            print("ID does not exist in the sheet. Please enter a valid ID.")


def main():
    """
    Main function with all business logic to control the difference options.
    Based on the option user selected, appropriate function will be called.
    """
    print("Welcome to Employee Management System.")
    print("Choose a number from the menu and press enter.")
    print("To restart press RUN PROGRAM.")
    while True:
        print("\n\n1. Add new employee data")
        print("2. Search for employee data")
        print("3. Edit employee data")
        print("4. Delete employee data")

        try:
            option = input("Please select one option: ")
            if not option.isdigit():
                raise ValueError("Please enter a number.")
            option = int(option)
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue

        if option == 1:
            add_employee_data()
        elif option == 2:
            search_employee_data()
        elif option == 3:
            edit_employee_data()
        elif option == 4:
            delete_employee()
        else:
            print("Invalid option selected. Please try again.")


main()
