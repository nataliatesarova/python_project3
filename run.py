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


def validate_data(data):
    """
     Validation check of input data
    """
    try:
        data_list = data.split(',')
        data_col_length = len(data_list)
        if data_col_length != 9:
            raise Exception('Insufficient columns entered')

        data_id = data_list[0]
        data_phone = data_list[4]
        data_asalary = data_list[7]
    except Exception:
        return False
    return True


def get_employee_data():
    """
    function to get employee data from user input
    """
    # Prompt user to enter employee data
    print("Please enter employee data.")
    # Provide instructions on how to enter data
    print("Enter data separated by comma in order of: ID,Forename,Surname,Email,Telephone number,Department,Position,Annual salary,Start date.")
    print("Example: 10,Julian,Jones,julianjones@gmail.com,721878900,Marketing,Marketing Agent,38400,1.9.2020\n")

    # Get user input for employee data
    data = input("Enter your data\n")
    print('data is: ', data)

    # Validate user input data
    if (not validate_data(data)):
        print('data validation failed')
        return

    # Split the data by commas and store in list
    employee_data = data.split(",")
    # Extract the annual salary value from the list
    value = employee_data[7]
    # Convert annual salary value to float
    annual_salary = float(value)
    # Calculate monthly salary by dividing annual salary by 12
    monthly_salary = annual_salary / 12
    # Append the monthly salary value to the employee data list
    employee_data.append(round(monthly_salary, 2))
    # Call the add_employee function to add the employee data to the spredsheet
    add_employee('Sheet1', employee_data)
    # print confirmation message to user that employee data has been added
    print("Employee data added successfully")


def add_employee(sheet_name, data):
    """
    code to add a new employee into the sheet
    """
    # Get the worksheet with the specified name
    sheet = SHEET.worksheet(sheet_name)
    # Append a new row to the worksheet with the employee data
    sheet.append_row(data)


def delete_employee():
    """
    code to delete an employee from the sheet
    """
    # Ask user for the employee ID to be deleted
    id = input("Enter the ID to be deleted: ")

    # Get the sheet
    sheet = SHEET.worksheet('Sheet1')
    # Get all the data in the sheet
    data = sheet.get_all_values()

    # Loop through the data rows and check if the ID matches
    for i in range(1, len(data) - 1):
        row = data[i]
        if row[0] == id:
            # If match found, delete the row and print message
            sheet.delete_rows(i + 1)
            print("Row deleted")
            return
    # If no match found, print message
    print("No matching row found")


def search_employee_data():
    """
    Searches for employee data based on ID and prints the row if found
    """
    # Prompt user to input ID to search for
    id = input("Enter the ID: ")

    # Open the Sheet1 worksheet and get all data
    sheet = SHEET.worksheet('Sheet1')
    data = sheet.get_all_values()

    # Iterate through each row in data and check if ID matches
    for row in data[1:]:
        if row[0] == id:
            # print row data if ID matches
            print(row)
            return
    # If no match found, print message
    print("No matching was found for the ID")

def edit_employee_data():
    """
    Code to edit the details of an existing employee
    """
    # Get the ID of the employee to be edited
    id = input("Enter the ID to be edited: ")

    # Get the worksheet 'Sheet1'
    sheet = SHEET.worksheet('Sheet1')
    # Get all the data from the worksheet
    data = sheet.get_all_values()

    editing_row = -1
    # Find the row to be edited
    
    
    

        # Calculate the monthly salary of the employee
        value = employee_data[6]
        annual_salary = float(value)
        monthly_salary = annual_salary / 12
        employee_data.append(round(monthly_salary, 2))

       







def main():
    # """
    # Main function which has all business logic to control the difference options.
    # Based on the option user selected, appropriate function will be called.
    # """
  


# Executions starts from the main function here
main()