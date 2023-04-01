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

def get_employee_data():
    """
     getting employee data from user
    """
    # data = ['10', 'Julian','Jones','julianjones@gmail.com','721 878 900','Marketing','Marketing Agent','38400','1.9.2020']
    # take input from the user
    # while True:
        # # print('input...')
    print("Please enter employee data.")
    print("Enter data separated by comma in order of: ID,Forename,Surname,Email,Telephone number,Department,Position,Annual salary,Start date.")
    print("Example: 10,Julian,Jones,julianjones@gmail.com,721 878 900,Marketing,Marketing Agent,38400,1.9.2020\n")

    data = input("Enter your data\n")

    # employee_data = data.split(",")

       

        # add code for data validation
    return employee_data

def add_employee(sheet_name, data):
    """
    code to add a new employee into the sheet
    """
    sheet = SHEET.worksheet(sheet_name)
    sheet.append_row(data)

def main():
    """
    main function which has all business logic
    """
    # accessing sheet 1 for employee data
    sheet = SHEET.worksheet('Sheet1')
    data = sheet.get_all_values()
    print(data)

    # call a function, pass data, inside the function calculate size of data which gives you the number of employees in the sheet
    # get the total number of employees subtract 1 to exclude the header row
    number_employees = len(data) - 1
    # loop over the records in the data using for loop and calculate monthly salary for each employee

    employee_data = get_employee_data()
    # add employee to sheet
    add_employee('Sheet1', employee_data)

# calling main function
main()
