import logging
import logging.config
import os
from dotenv import load_dotenv
from app import App
from app.history.history_handler import HistoryHandler  
from app.commands import add_command, subtract_command, multiply_command, divide_command


load_dotenv()
LOG_CONFIG_FILE = 'logging.conf'
logging.config.fileConfig(LOG_CONFIG_FILE)

# Ensure the logs directory exists
os.makedirs('logs', exist_ok=True)

def main():
    # Initializes app
    app = App()

    print("Hello Professor! Type 'menu' to display all available commands or 'exit' to quit.")
    last_command = None
    last_result = None
    while True:
        command = input("Enter a command: ")

    
        if command.startswith("add"):
            try:
                args = list(map(float, command.split()[1:]))  # Extract and convert args to float
                last_result = app.command_handler.execute_command("add", *args)  # Use app's command handler
                print(f"Result: {last_result}")
                last_command = "add"
            except ValueError:
                print("Error: Please provide valid numbers for addition.")
                logging.error('Please provide valid numbers.')

        elif command.startswith("subtract"):
            try:
                last_args = list(map(float, command.split()[1:]))
                last_result = app.command_handler.execute_command("subtract", *last_args)
                print(f"Result: {last_result}")
                last_command = "subtract"
            except ValueError:
                print("Error: Please provide valid numbers for subtraction")
                logging.error('Please provide valid numbers.')
        elif command.startswith("multiply"):
            try:
                last_args = list(map(float, command.split()[1:]))
                last_result = app.command_handler.execute_command("multiply", *last_args)
                print(f"Result: {last_result}")
                last_command = "multiply"
            except ValueError:
                print("Error: Please provide valid numbers for multiplication.")
                logging.error('Please provide valid numbers.')
        elif command.startswith("divide"):
            try:
                last_args = list(map(float, command.split()[1:]))
                last_result = app.command_handler.execute_command("divide", *last_args)
                print(f"Result: {last_result}")
                last_command = "divide"
            except ValueError:
                print("Error: Please provide valid numbers for division")
                logging.error('Please provide valid numbers.')
        # Handles history-related commands
        elif command == "load_history":
            app.history_handler.load_history()  # Load and display history

        elif command == "clear_history":
            app.history_handler.clear_history()  # Clear the history
        
        elif command == "save_history":
            if last_command and last_result is not None:
                # Save the last command and its result to history
                app.history_handler.save_history(last_command, args, last_result)
                
            else:
                print("No command has been executed to save history.")
        elif command == "exit":
            print("Exiting the calculator, have a great day!")
            logging.info('Leaving calculator')
            break

        elif command == "menu":
            app.command_handler.execute_command("menu")  # Uses apps command handler

        else:
            print("Unknown command. Please try again.")
            logging.warning('you have entered an unkown command.')
if __name__ == "__main__":
    logging.getLogger().info("Starting the application.")
    main()
