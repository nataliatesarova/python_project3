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

   

    # loop over the records in the data using for loop and calculate monthly salary for each employee
    first_row = data[0]
    first_row.append('Monthly Salary')
    for row in data[1:]:
        # calculate monthly salary
        value = row[7]
        annual_salary = int(value)
        monthly_salary = annual_salary / 12
        # add monthly salary to row and round the result to 2 decimal places
        row.append(round(monthly_salary, 2))

    # add updated data to sheet
    sheet.update(data)

    employee_data = get_employee_data()
    # add employee to sheet
    add_employee('Sheet1', employee_data)


   

# calling main function
main()
