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
        # data validation here
        # check whether the user has entered 9 data points
        data_list = data.split(',')
        data_col_length = len(data_list)
        if data_col_length != 9:
            raise Exception('Insufficient columns entered')

        # check for integer values in ID, phone number, annual salary columns
        data_id = data_list[0]
        data_phone = data_list[4]
        data_asalary = data_list[7]
        print('data_id: ', data_id, ' data_phone:', data_phone, ' data_asalary: ', data_asalary)
        print('checking int conversion: ', int(data_id))
        print('checking int conversion: ', int(data_phone))
        print('checking int conversion: ', int(data_asalary))
    except Exception:
        return False
    return True


def get_employee_data():
    """
     getting employee data from user
    """
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


def delete_employee(sheet_name, employee_id):
    """
    code to delete an employee from the sheet
    """
    sheet = SHEET.worksheet(sheet_name)
    data = sheet.get_all_values()
    headers = data[0]
    id_index = headers.index('ID')
# find the row corresponding to the given employee ID
    for row in data[1:]:
        if row[id_index] == employee_id:
            # delete the row and return True to indicate success
            sheet.delete_rows(data.index(row) + 1)  # add 1 to account for header row
            return True
# if no employee with the given ID was found, return False to indicate failure
    return False


def main():
    """
    main function which has all business logic
    """
    # accessing sheet 1 for employee data
    sheet = SHEET.worksheet('Sheet1')
    data = sheet.get_all_values()
    # print(data)

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
print("Welcome to Employee Data System")
main()