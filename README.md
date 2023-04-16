# Employee Management System
The [Employee Management System](https://project3tesarova.herokuapp.com/) is a software application that provides users with an effective means of managing employee data by utilizing Google Sheets. This tool is designed to streamline the management of employee information and improve the efficiency of HR processes. 

![start page ?different devices]()

## Features
There are 4 main features of the Employee Management System 

![Four features](readme-docs/images/features.png)

### Add new employee data
Option 1 allows the user to enter new employee forename, surname, email, telephone number, department, position, annual salary, and start date.

![option 1 selected](assets/images/.png)

With correct entry of the data the Google sheet is updated with the new employee information and the user is provided with the confirmation message 'Employee data added successfully'. Monthly salary is automatically calculated from the annual salary. The main options are then once again presented. 

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
The software tool is designed to offer users a simple and efficient experience by enabling add, delete, search, and edit of employee data in a Google Sheet. To enhance user experience, the following features have been implemented:

Input validation: The validate_data() function checks that the user's input contains the correct number of columns and provides clear feedback on how to correct errors.

Instructions for data entry: The get employee data function offers instructions on how to enter data, along with an example.

Confirmation and error messages: Users receive confirmation messages when their actions are successful (e.g., adding an employee) and error messages when the ID does not match any data in the sheet. These messages provide clarity and reduce uncertainty. 

## Flow Chart

![Flow Chart](readme-docs/images/Flowchart.png)

## Google Sheet
The Python script interacts with a Google Sheet using the gspread library allowing the adding, deleting, editing and searching of employee data, in addition to calculating monthly salary. The program provides a basic user interface for interacting with the Sheet.

![Google Sheet](readme-docs/images/sheet.png)

## Future Features 
The current code only allows searching for data based on the ID column. However, a future version could potentially enhance this functionality by enabling searching based on other parameters, such as name, email address, or department.

At present the code only validates the input data for the number of columns, but it does not perform any data validation checks on the content of each column. For instance, it does not verify whether the email address entered by the user is in a valid format. In a future version, data validation checks could be added for each column to ensure that the user's input data is accurate and reliable.

A future version could include more detailed error messaging and interactive prompts to guide the user through the process.

In a future iteration, incorporating HTML and CSS could enhance the program's usability by providing a user-friendly interface for users to interact with the program's functionality.

## Technologies Used
### Language
Python

### Frameworks, Libraries & Programs
* [Google sheets](https://www.google.com/sheets/about/) - used to store and manage program data.
* [Gspread](https://docs.gspread.org/en/v5.7.1/) - a Python library that simplifies the process of programmatically interacting with Google Sheets.
* [Google Auth](https://google-auth.readthedocs.io/en/master/) - a framework that provides a secure and easy way to enable the application to access Google APIs, such as Google Sheets API.
* [Github](https://github.com/) - cloud based hosting service to save and store the files.
* Git - version control system.
* [Lucidchart](https://www.lucidchart.com/pages/tour) - Utilized to create the flow chart.
* [Heroku](https://dashboard.heroku.com/apps) - used to deploy the application.

## Testing and Validation
[Code Institute Python Linter](https://pep8ci.herokuapp.com/#) - was used for validation to ensure no Python code errors.
![CIlinter](readme-docs/images/linter.png)

## Manual Testing
Extensive manual testing was performed on the the menu-driven interface to manage an employee data system, with special emphasis placed on validating user input and performing error checking to guarantee that the user is provided with appropriate feedback at all times.

The user is welcomed to a menu of 4 options with clear instructions to choose a number, or restart the program with the run program button. If an invalid choose is inputted the user is returned with the message 'Invalid option selected. Please try again'.
![Invalid option selected. Please try again.](readme-docs/images/.png)

The get employee data function offers instructions on how to enter data, along with an example.

![](readme-docs/images/.png)

The validate data function was used to validate the data entered by the user. It checks if the number of columns entered is equal to 9. If the new employee is added or current employee edited correctly the user is returned with the confirmation message 'Employee data added successfully' and 'Editing success' respectively. 

![Employee data added successfully](readme-docs/images/.png)
![Editing success](readme-docs/images/.png)

If the data entered is not in the correct format or the ID is not matched for search and editing the user is returned the message 'data validation failed' or "No matching data found" respectively, and presented with main options.

![Data validation failed](readme-docs/images/.png)
![No matching data found](readme-docs/images/.png)
 
The application was tested on Google Chrome, Safari, Firefox and Microsoft Edge browsers without issues.

## Bugs
An error was found with the editing and deleting of the last row of the sheet. The issue was caused by the use of range(1, len(data) - 1) in the for loop, which excluded the last row of the sheet. This problem was fixed by changing the range to range(1, len(data) + 1), which allowed the loop to iterate over all rows in the data list, including the last row. 

## Heroku Deployment
The Employee Management System has been designed to be deployed and utilized on Heroku. The terminal template was specifically created by Code Institute to be compatible with the Heroku platform. It may not function properly on a local terminal due to differences in positioning and other technical aspects, even if the program's functionality remains unchanged. Therefore, it is recommended to use the system exclusively on the Heroku platform.

* Fork or clone the repository from [GitHub](https://github.com/nataliatesarova/python_project3)
* Create a new Heroku app by logging in to the Heroku account and clicking the "New" button in the dashboard.
* In the "Deploy" tab of your Heroku app's dashboard, set the buildpacks to Python and NodeJS in that order.
* Link the Heroku app to the repository by going to the "Deploy" tab and selecting the GitHub deployment method. Then search for and connect the repository to Heroku.
* Click on the "Deploy" button to start the deployment process.

## Credits and Acknowledgements
I would like to thank my mentor Rory Sheridan and all the tutors, teachers and student colleagues for help and advice on the project.

Clarification on Elif Else statement [Programming with Mosh](https://www.youtube.com/watch?v=Zp5MuPOtsSY).

Instruction on While True in Python [Board Infinity](https://www.boardinfinity.com/blog/use-while-true-in-python/).

Instruction on Errors and Exceptions [Python](https://docs.python.org/3/tutorial/errors.html).
