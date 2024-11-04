import logging
import pandas as pd
import os
from datetime import datetime

class HistoryManager:
    def __init__(self, history_file='history.csv'):
        self.history_file = history_file
        self.history = self.load_history()  # Load history when initializing

    def load_history(self):
        if os.path.exists(self.history_file):
            self.history = pd.read_csv(self.history_file)
            if self.history.empty:
                print("No history found.")
                logging.info("No history available to load.")
        else:
            # Create an empty DataFrame if the file doesn't exist
            self.history = pd.DataFrame(columns=["timestamp", "operation", "args", "result"])


    def save_history(self):
        if not self.history.empty:
            self.history.to_csv(self.history_file, index=False)
        else:
            print("No history to save.")

    def clear_history(self):
        self.history = pd.DataFrame(columns=['timestamp', 'operation', 'args', 'result'])
        self.save_history() # Save the cleared state

    def add_record(self, command: str, args: tuple, result):
        """Add a new record to the history DataFrame."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_record = pd.DataFrame({
            'timestamp': [timestamp],
            'operation': [command],
            'args': [args],
            'result': [result]
        })
        self.history = pd.concat([self.history, new_record], ignore_index=True)