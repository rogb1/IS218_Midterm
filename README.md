# My Caluclator Project
Hello, this is my calculator that uses basic arithmetic operations add, subtract, multiply, divide and advanced history management save_history, load_history, and clear_history functionalities. This is all done using a command-line interface
## Table of Contents
1. [Introduction](#how-to-get-started)
2. [Setup Instructions](#usage-instructions)
3. [Architectural Decisions](#architectural-decisions)
   - [Design Patterns](#design-patterns)
   - [Logging Strategy](#logging)
4. [Environment Variables](#Environment Variables)
5. [Exception-Handling](#Exception-Handling)
## How to get started 
You can watch my video here or read the steps below
link to video 
[Watch the demonstration video here](https://youtu.be/eXutjHNnJW4)

Open your terminal and type:
mkdir <folder_name>
Navigate to Your Folder:

Move into the folder you just created:
cd <folder_name>
Set Up a Virtual Environment:

Create a virtual environment by typing:
python3 -m venv venv
Activate the Virtual Environment:

For Linux or Ubuntu, activate it with:
source venv/bin/activate
Initialize Git:

Start a new Git repository:
git init

When you have done all of those steps 
Clone the Repository:
git clone https://github.com/rogb1/IS218_Midterm.git

Install:
pip install -r requirements.txt


## Usage Instructions
Run the application by executing python main.py in your terminal
``` python main.py ``` 
Available Commands:
Once the app starts, you can enter one of the following commands:
Add: Use add <number1> <number2> to add.
Subtract: Use subtract <number1> <number2> to subtract.
Multiply: Use multiply <number1> <number2> to multiply.
Divide: Use divide <number1> <number2> to divide (division by zero is not allowed).
Load_History: Type load_history to see previously calculated operations.
Clear_History: Type clear_history to remove all stored history.
Save_History: Type save_history to save the  calculation history to a file.
Menu: Type menu to view all available commands.
Exit: Type exit to close the application.
``` add 4 7 add [num1] [num2] | to add```
```subtract 4 2 subtract [num1] [num2]  to subtract ```
```multiply 4 9 multiply [num1] [num2]  to multiply ```
```divide 2 3  divide [num1] [num2] to divide ```
``` menu to display all available commands ```
``` exit to exit the calculator ```
## History commands
```save_history to save a calculation to your history```
```load_history to load any saved calculation history```
```clear_history to clear all saved calculation history```





Error Handling:

If you enter an invalid command or input, the app will display an error message guiding you to enter valid numbers or commands.
Check Logs:

You can review the app.log file in the logs folder to see recorded activities and any errors that occurred during your session.

## Architectural decisions

## Initial Setup
1. **Establish Directory Structure**  
   Created the main directory structure by creating an `app` folder, organizing it for functionality with necessary subdirectories to support the command-line interface (CLI) application.

## Core Functionality
2. 
   Implemented fundamental operations (Add, Subtract, Multiply, Divide) along with initial logging configurations for each operation to track execution.

## Command Registration and Execution
3. 
   Introduced `Command` and `CommandHandler` classes to facilitate the registration and management of calculator commands, enabling a more modular command execution process.

## Menu and History Commands
4.  
   Created a `history` folder containing 3 files history_handler, history_manager, and history_facade.

## Plugin Development and Enhanced Logging
5. **Integrate Logging**  
   Integrated logging into each command, enhancing visibility into user input during command execution and refining the main command menu for improved user experience.

## History Management Features
6.  
   Enhanced logging configurations across various files, improved the `save_history.py` functionality to ensure correct operation, and ensured that history commands were properly invoked through the main command-line interface.


## Error Handling and Environment Variable Integration
8.
   Updated error messages to add on to the user experience and incorporated an environment variable loader.

## Final Test and Coverage Assurance
9.   
   Made sure all fo my test passed with 90% or higher



## Design Patterns

**Description**:  
In my calculator project, I used the Command Pattern to turn command requests into objects. Each operation, such as addition or subtraction,etc, is defined by its own command class that follows a standard interface. This design makes the code neater and improves the application's flexibility and scalability. I can add new commands without having to change the existing ones, and these commands can be executed based on what the user inputs. A command handler takes care of registering and running these commands, which simplifies expanding the calculator's features.

**Link to Implementation**:  
[CommandHandler Implementation](app/commands/__init__.py)

---

## Environment Variables

**Description**:  
Environment variables are key to handling settings in this app. With the dotenv package, I can pull in settings from a .env file, which helps keep things like database passwords and logging levels safe and out of the code. This makes the app more secure and easier to use in different settings—whether in development, testing, or production—without needing to change the code. The app grabs these variables while it runs, so it always works right for the environment it's in.
**Link to Implementation**:  
[Loading Environment Variables](.env)

---

## Logging



Logging Strategy
I created a logging system that stores  information on what happens in the app. They are saved in a file called app.log in a special logs folder that only I can see. Each part of the app records important actions like what commands users enter, any errors, and menu choices. 

[Logging Configuration](logging.conf)

---

## Exception Handling
  
The application allows for exception handling to implement the principles of "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP). I wrapped operations in `try/catch` blocks, the application checks for the existence of commands before executing them. If an error occurs (e.g., a command is not found or an invalid operation is attempted), it takes care of it by logging the error and informing the user. This also helps the user expereience as it does not crash whenever an error like that occurs. 

**Link to Implementation**:  
[Exception Handling Code](main.py)

---
