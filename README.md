# Employee Management System
The Employee Management System is a software tool that enables users to manage employee data using a Google Sheet. 

![start page ?different devices](assets/images/.png)

## Features
There are 4 main features of the Employee Management System 

![start page close up](assets/images/.png)

### Add new employee data
Option 1 allows the user to enter new employee forename, surname, email, telephone number, department, position, annual salary, and start date.

![option 1 selected](assets/images/.png)

With correct entry of the data the Google sheet is updated with the new employee information and the user is provided with the confirmation message 'Employee data added successfully'. The main options are then once again presented. 

![Employee data added successfully](assets/images/.png)

If all the data points required are not entered in the correct format the user is informed with the message 'Data validation failed' and the main options are presented.

![data validation failed](assets/images/.png)

### Search for employee data
Option 2 allows the user to search for a current employee by entering the employees ID.

![option 2 selected](assets/images/.png)

If an ID is not matched the user is informed with the message 'No matching was found for the ID' and the main options are presented.

![No matching ID](assets/images/.png)

### Edit employee data
Option 3 allows the user to edit the data of a current employee after entering the employees ID.

![option 3 selected](assets/images/.png)

### Delete employee data
Option 4 allows the user to delete the data of a current employee after entering the employees ID. The Google sheet is updated with the edited information.

![option 4 selected](assets/images/.png)

### Exit
Option 5 allows the user to exit the program.

## User Experience (UX)

The software tool is designed to offer users a simple and efficient experience by enabling them to add, delete, search, and edit employee data in a Google Sheet. To enhance user experience, the following features have been implemented:

Input validation: The validate_data() function checks that the user's input contains the correct number of columns and provides clear feedback on how to correct errors.

Instructions for data entry: The get_employee_data() function offers instructions on how to enter data, along with an example.

Confirmation and error messages: Users receive confirmation messages when their actions are successful (e.g., adding an employee) and error messages when their input does not match any data in the sheet. These messages provide clarity and reduce uncertainty. 
 
## Future Features 
-The current code only allows searching for data based on the ID column. However, a future version could potentially enhance this functionality by enabling searching based on other parameters, such as name, email address, or department.

-The current code only validates the input data for the number of columns, but it does not perform any data validation checks on the content of each column. For instance, it does not verify whether the email address entered by the user is in a valid format. In a future version, data validation checks could be added for each column to ensure that the user's input data is accurate and reliable.

-A future version could include more detailed error messaging and interactive prompts to guide the user through the process.

-In a future iteration, incorporating HTML and CSS could enhance the program's usability by providing a user-friendly interface for users to interact with the program's functionality.

## Technologies Used
# Language used 
Python

# Frameworks, Libraries & Programs Used
Google sheets - used to store and manage program data.
Gspread - a python library that provides an interface to interact with Google. Sheets API.
Google Auth - utilized to grant the app permission to interact with Google Sheets.
Gitpod - employed to develop, modify, and compile the code for the program.
Lucidchart - utilized for creating flow charts.
Heroku -  used to deploy the application.

