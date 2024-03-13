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
            print("Use a valid number format, without characters or commas.")


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
        id = str(input("Enter ID: ")).strip()
        try:
            id = int(id)
            if id < 0:
                id = None
                print("Invalid ID. ID should be greater than 0")
        except e:
            id = None
            print("Please enter a valid ID")

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
    Searches for employee data based on ID and prints the row if found
    """
    # Prompt user to input ID for searching
    id = None
    while id is None:
        id = str(input("Enter ID: ")).strip()
        try:
            id = int(id)
            if id < 1:
                id = None
                print("Invalid ID")
        except e:
            id = None
            print("Please enter a valid ID")

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
            break  # ID is valid, exit the loop
        except ValueError:
            print("Please enter a valid ID")

    # Get the worksheet 'Sheet1'
    sheet = SHEET.worksheet('Sheet1')
    # Get all the data from the worksheet
    data = sheet.get_all_values()

    editing_row = -1
    # Find the row to be edited
    for i in range(1, len(data)):
        row = data[i]
        if row[0] == str(id):
            editing_row = i
            break
    if editing_row == -1:
        # If no matching data is found
        print("No matching data found")
    else:
        # If a matching data is found
        # Get the details to be updated from the user
        employee_data = []
        employee_data.append(id)

        print("If no data edited, leave it empty by pressing enter key")

        # Prompt the user for updated forename
        while True:
            forename = input("Enter updated forename: ").strip()
            if not forename:
                # No input was given, forename remains unchanged
                print("No changes made to forename.")
                break
            # Validate forename (only letters allowed)
            if not re.match(r'^[a-zA-Z]+$', forename):
                print("Invalid forename. Only letters are allowed.")
                continue
            # Forename is valid, append it to the list
            employee_data.append(forename)
            break

        # Prompt the user for updated surname
        while True:
            surname = input("Enter updated surname: ").strip()
            if not surname:
                # No input was given, surname remains unchanged
                print("No changes made to surname.")
                break
            # Validate surname (only letters allowed)
            if not re.match(r'^[a-zA-Z]+$', surname):
                print("Invalid surname. Only letters are allowed.")
                continue
            # Surname is valid, append it to the list
            employee_data.append(surname)
            break

        # Prompt the user for updated email
        while True:
            email = input("Enter updated email address: ").strip()
            if not email:
                # No input was given, email remains unchanged
                print("No changes made to email.")
                break
            # Validate email format
            if not re.match(
                r'^(?!.*\.\.)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                    email):
                print(
                    "Invalid email format. Please enter a valid email address."
                    )
                continue
            # Email is valid, append it to the list
            employee_data.append(email)
            break

        # Prompt the user for updated phone number
        while True:
            number = input("Enter updated phone number: ").strip()
            if not number:
                # No input was given, phone number remains unchanged
                print("No changes made to phone number.")
                break
            # Validate phone number (only digits and at least 7 characters)
            number_stripped = number.replace(" ", "")
            if not number_stripped.isdigit():
                print("Phone number must contain only digits.")
                continue
            if len(number_stripped) < 7:
                print("Phone number must be at least 7 digits.")
                continue
            # Phone number is valid, append it to the list
            employee_data.append(number)
            break

        # Prompt for valid department until correct input
        while True:
            department = str(input("Enter updated department: ")).strip()
            if not department:
                # No input was given, department remains unchanged
                print("No changes made to department.")
                break
            elif contains_invalid_characters(department):
                # Department contains invalid characters
                print("Department cannot contain special characters.")
            else:
                # Department is valid, append it to the list
                employee_data.append(department)
                break

        # Request updated position until valid input
        while True:
            position = str(input("Enter updated position: ")).strip()
            if not position:
                # No input was given, position remains unchanged
                print("No changes made to position.")
                break
            elif contains_invalid_characters(position):
                # Position contains invalid characters
                print("Position cannot contain special characters.")
            else:
                # Position is valid, append it to the list
                employee_data.append(position)
                break

        salary = None
        while True:
            # Prompt the user to enter the updated annual salary
            salary_input = input("Enter updated annual salary: ").strip()
            if not salary_input:
                # No input was given, salary remains unchanged
                print("No changes made to salary.")
                break
            # Validate salary
            try:
                salary = float(salary_input.replace(',', '.'))
                if salary <= 0:
                    print("Salary must be greater than 0.")
                    continue
                # Salary is valid, append it to the list
                employee_data.append(salary)
                break
            except ValueError:
                print(
                    "Use a valid number format, without characters or commas."
                     )

        # Request valid start date input
        while True:
            start_date = input(
                "Enter updated start date [dd/mm/yyyy]: ").strip()
            if not start_date:
                # No input was given, start date remains unchanged
                print("No changes made to start date.")
                break
            elif not valid_date("Start Date", start_date):
                # Invalid start date format
                continue
            else:
                # Start date is valid, append it to the list
                employee_data.append(start_date)
                break

        # Calculate the monthly salary of the employee
        updated_monthly_salary = ""
        if salary != "":
            updated_monthly_salary = salary / 12
            # Append the monthly salary value to the employee data list
        if updated_monthly_salary == "":
            employee_data.append(updated_monthly_salary)
        else:
            employee_data.append(round(updated_monthly_salary, 2))

        # Update the data in the worksheet
        sheet = SHEET.worksheet('Sheet1')
        editing_row = editing_row + 1
        for i in range(1, len(employee_data)):
            if employee_data[i] != "":
                sheet.update_cell(editing_row, (i + 1), employee_data[i])

        print("Editing success")


def delete_employee():
    """
    code to delete an employee from the sheet
    """
    # Ask user for the employee ID to be deleted
    id = None
    while id is None:
        id = str(input("Enter ID to delete: ")).strip()
        try:
            id = int(id)
            if id < 1:
                id = None
                print("Invalid ID")
        except e:
            id = None
            print("Please enter a valid ID")

    # Get the sheet
    sheet = SHEET.worksheet('Sheet1')
    # Get all the data in the sheet
    data = sheet.get_all_values()

    # Loop through the data rows and check if the ID matches
    for i in range(1, len(data)):
        row = data[i]
        if row[0] == str(id):
            # If match found, delete the row and print message
            sheet.delete_rows(i + 1)
            print("Data deleted")
            return
    # If no match found, print message
    print("No matching row found")


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
