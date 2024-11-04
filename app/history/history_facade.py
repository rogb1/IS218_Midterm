from app.history.history_handler import HistoryHandler

class HistoryFacade:
    def __init__(self):
        self.handler = HistoryHandler()

    def load_history(self):
        """Load history and print it."""
        self.handler.load_history()
        if self.handler.manager.history.empty:
            print("No history found.")
        else:
            print(self.handler.manager.history)

    def clear_history(self):
        self.handler.clear_history()
        print("History cleared.")

    def save_history(self, command: str, args: tuple, result):
        self.handler.manager.add_record(command, args, result)  # Add the record to the manager
        self.handler.save_history(command, args, result)  # Save the history to file
        print("History saved successfully.")  # Confirm save operation
