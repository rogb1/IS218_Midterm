import os
import pandas as pd # type: ignore
import logging
from app.history.history_manager import HistoryManager
from datetime import datetime

class HistoryHandler:
    def __init__(self):
        self.manager = HistoryManager()
        self.history_file = 'history.csv'
        self.history = self.manager.load_history()
        #Define path for history file
        #Load any existing history from the CSV file
        if os.path.exists(self.history_file):
            self.history = pd.read_csv(self.history_file)
        else:
            self.history = pd.DataFrame(columns=["timestamp", "operation", "args", "result"])

    def load_history(self):
        if os.path.exists(self.history_file):
            self.history = pd.read_csv(self.history_file)
            if self.history.empty:
                print("No history found.")
                logging.info("No history available to load.")
                return

            print("\nCalculation History:")
            for index, row in self.history.iterrows():
                operation = row.get('operation', 'Unknown operation')
                args = row.get('args', 'Unknown args')
                result = row.get('result', 'Unknown result')
                print(f"{index + 1}. {operation}({args}) = {result}")
            logging.info('Displaying calculation history.')
        else:
            print("No history file found.")



    def clear_history(self):
        self.history = pd.DataFrame(columns=["timestamp", "operation", "args", "result"])
        if os.path.exists(self.history_file):
            os.remove(self.history_file)  # Delete the history file
        logging.info('Calculation history cleared.')
        print("History cleared.")

    def add_record(self, command: str, args: tuple, result):
        """Add a new record to the history DataFrame."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        args_str = ', '.join(map(str, args))
        new_record = pd.DataFrame({
            'timestamp': [timestamp],
            'operation': [command],
            'args': [args_str],
            'result': [result]
        })
        self.history = pd.concat([self.history, new_record], ignore_index=True)
        self.history.to_csv(self.history_file, index=False)

    def save_history(self, command: str, args: tuple, result):
        """Save the command, arguments, and result to history."""
        self.add_record(command, args, result)  # Adds the new record to self.history
        self.history.to_csv(self.history_file, index=False) 
        
         # Persist history to a CSV file
        args_display = ', '.join(map(str, args))  # Convert args to a comma-separated string
        logging.info(f'History saved successfully: ({command}, {args}, {result})')
        print(f'History saved successfully: {command}({args_display}) = {result}')

