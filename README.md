# Employee Management System
The Employee Management System is a software tool that enables users to manage employee data using a Google Sheet. 

![start page ?different devices](assets/images/.png)

## Features
There are 4 main features of the Employee Management System 

![start page close up](assets/images/.png)

### Add new employee data
Option 1 allows the user to enter new employee forename, surname, email, telephone number, department, position, annual salary, and start date.

![option 1 selected](assets/images/.png)

### Search for employee data
Option 2 allows the user to search for a current employee by entering the employees ID

![option 2 selected](assets/images/.png)

### Edit employee data
Option 3 allows the user to edit the data of a current employee after entering the employees ID

![option 3 selected](assets/images/.png)

### Delete employee data
Option 4 allows the user to delete the data of a current employee after entering the employees ID

![option 4 selected](assets/images/.png)

### Delete employee data
Option 5 allows the user to exit the program.

![option 5 selected](assets/images/.png)

## User Experience (UX)
The software tool aims to allow users to simply and efficiently:  
* Add a new employee to the Google Sheet
* Delete an employee from the Google Sheet
* Search for employee data based on ID
* Edit the details of an existing employee

-The validate data function can help prevent errors and improve UX by providing clear feedback to the user on how to enter data correctly.
-The get employee data function can help users understand what information is required and how to enter it correctly.
-Confirmation messages can help users understand that their actions were successful and reduce uncertainty.
-Error messages can help users understand why their request was not successful and how to correct it.


##Features 
Input validation: The validate_data() function checks that the user's input contains the correct number of columns, and raises an exception if it doesn't. 

Instructions for data entry: The get_employee_data() function provides instructions for how to enter data, including an example. 

Confirmation messages: The code provides confirmation messages to the user after certain actions are taken (e.g. adding an employee). 

Error messages: The code provides error messages (e.g. "No matching data found") when user input does not match any data in the sheet. 