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

def valid_id(id):
    if id == None:
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

def empty_value(field_name, value):
    if value == None:
        return False
    
    if len(value) == 0:
        print(field_name + " cannot be empty")
        return False
    
    return True

def is_valid_email(email):
    if "@" not in email or "." not in email:
        return False
    
    return True

def valid_date(field_name, date):
    if date == None:
        return False
    
    if len(date) == 0:
        print(field_name + " cannot be empty")
        return False
    
    try:
        date = date.split("/")
        if len(date) != 3 or int(date[0]) < 1 or int(date[0]) > 31 or int(date[1]) < 1 or int(date[1]) > 12 or int(date[2]) < 1920 or int(date[2]) > 2023:
            print("Invalid date. Please try again")
            return False
    except:
        print("Invalid date. Please try again")
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

def add_employee_data():
    """
    function to add employee data from user input
    """
    # Prompt user to enter employee data
    employee_data = []

    print("Please enter employee data.")
    # Provide instructions on how to enter data
    id = None
    while not valid_id(id):
        id = str(input("Enter ID: ")).strip()
        try:
            id = int(id)
            if id < 1:
                id = None
                print("Invalid ID")
        except:
            id = None
            print("Please enter a valid ID")
    
    employee_data.append(id)

    forename = None
    while not empty_value("Forename", forename):
        forename = str(input("Enter forename: ")).strip()
    
    employee_data.append(forename)

    surname = None
    while not empty_value("Surname", surname):
        surname = str(input("Enter surname: ")).strip()

    employee_data.append(surname)

    email = None
    while not empty_value("Email address", email):
        email = str(input("Enter email address: ")).strip()
        if not is_valid_email(email):
            email = None
            print("Invalid email")

    employee_data.append(email)

    number = None
    while number == None:
        number = str(input("Enter phone number: ")).strip()
        try:
            number = int(number)
        except:
            number = None
            print("Please enter a valid phone number")
    
    employee_data.append(number)
    
    department = None
    while not empty_value("Department", department):
        department = str(input("Enter department: ")).strip()
    
    employee_data.append(department)
        
    position = None
    while not empty_value("Position", position):
        position = str(input("Enter position: ")).strip()
    
    employee_data.append(position)

    salary = None
    while salary == None:
        salary = str(input("Enter annual salary: ")).strip()
        try:
            salary = float(salary)
        except:
            salary = None
            print("Please enter a valid salary")
    
    employee_data.append(salary)
    
    start_date = None
    while not valid_date("Start Date", start_date):
        start_date = str(input("Enter start date [format dd/mm/yyyy]: ")).strip()
    
    employee_data.append(start_date)

    # Calculate monthly salary by dividing annual salary by 12
    monthly_salary = salary / 12
    # Append the monthly salary value to the employee data list
    employee_data.append(round(monthly_salary, 2))
    # Call the add_employee function to add the employee data to the spredsheet
    add_employee('Sheet1', employee_data)

    print("Employee data added successfully")

def print_employee_data(row):
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
    while id == None:
        id = str(input("Enter ID: ")).strip()
        try:
            id = int(id)
            if id < 1:
                id = None
                print("Invalid ID")
        except:
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
    while id == None:
        id = str(input("Enter ID to edit: ")).strip()
        try:
            id = int(id)
            if id < 1:
                id = None
                print("Invalid ID")
        except:
            id = None
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

        print("If you don't want to edit a data, please leave it empty by pressing enter key")

        forename = str(input("Enter updated forename: ")).strip()        
        employee_data.append(forename)

        surname = str(input("Enter updated surname: ")).strip()
        employee_data.append(surname)

        email = str(input("Enter updated email address: ")).strip()
        while email != "" and not is_valid_email(email):
            email = str(input("Enter updated email address: ")).strip()
        employee_data.append(email)

        number = ""
        valid_number = False
        while not valid_number:
            number = str(input("Enter updated phone number: ")).strip()
            valid_number = True
            if number != "":
                try:
                    number = int(number)
                except:
                    valid_number = False
                    print("Please enter a valid phone number")
        
        employee_data.append(number)
        
        department = str(input("Enter updated department: ")).strip()
        employee_data.append(department)

        position = str(input("Enter updated position: ")).strip()
        employee_data.append(position)

        salary = ""
        valid_salary = False
        while not valid_salary:
            salary = str(input("Enter updated annual salary: ")).strip()
            valid_salary = True
            if salary != "":
                try:
                    salary = float(salary)
                except:
                    valid_salary = False
                    print("Please enter a valid salary")
        
        employee_data.append(salary)
        
        start_date = str(input("Enter updated start date [format dd/mm/yyyy]: ")).strip()
        while start_date != "" and not valid_date("Start Date", start_date):
            start_date = str(input("Enter updated start date [format dd/mm/yyyy]: ")).strip()
        employee_data.append(start_date)

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
    while id == None:
        id = str(input("Enter ID to delete: ")).strip()
        try:
            id = int(id)
            if id < 1:
                id = None
                print("Invalid ID")
        except:
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
        # print("5. Exit")

        try:
            option = int(input("Please select one option: "))
        except:
            print("Invalid character. Please try again")
            continue
        
        if option == 1:
            add_employee_data()
        elif option == 2:
            search_employee_data()
        elif option == 3:
            edit_employee_data()
        elif option == 4:
            delete_employee()
        # elif option == 5:
            # break
        else:
            print("Invalid option selected. Please try again.")


main()
