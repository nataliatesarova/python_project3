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
    try:
        # data validation here
        # check whether the user has entered 9 columns
        data_list = data.split(',')
        data_col_length = len(data_list)
        if data_col_length != 9:
            raise Exception('Insufficient columns entered')

        

def get_employee_data():
    """
     getting employee data from user
    """
    # data = ['10', 'Julian','Jones','julianjones@gmail.com','721 878 900','Marketing','Marketing Agent','38400','1.9.2020']
    # take input from the user
    while True:
        print("Please enter employee data.")
        print("Enter data separated by comma in order of: ID,Forename,Surname,Email,Telephone number,Department,Position,Annual salary,Start date.")
        print("Example: 10,Julian,Jones,julianjones@gmail.com,721878900,Marketing,Marketing Agent,38400,1.9.2020\n")

        data = input("Enter your data\n")
        print('data is: ', data)

        if (validate_data(data)):
            print('data validation successful')
            break

    employee_data = data.split(",")
    print('employee data is: ', employee_data)
       
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

    # call a function, pass data, inside the function calculate size of data 
    # which gives you the number of employees in the sheet
    # get the total number of employees subtract 1 to exclude the header row
    number_employees = len(data) - 1
    # print("The number of employees is " + str(number_employees))
    # print(f"The number of employees is{number_employees}")

    # loop over the records in the data using for loop and calculate monthly salary for each employee
    first_row = data[0]
    first_row.append('Monthly Salary')
    for row in data[1:]:
        # calculate monthly salary
        value = row[7]
        annual_salary = int(value)
        monthly_salary = annual_salary / 12
        # add monthly salary to row and rounds the result to 2 decimal placed
        row.append(round(monthly_salary, 2))

    # add updated data to sheet
    sheet.update(data)

    employee_data = get_employee_data()
    # add employee to sheet
    add_employee('Sheet1', employee_data)
    
# calling main function
main()
