
from app.commands import Command
from app.history.history_facade import HistoryFacade

class SaveHistoryCommand(Command):
    def __init__(self):
        self.history_facade = HistoryFacade()

    def execute(self):
        operation = "save_history"  # Define the operation name
        args = ()  # Define arguments, if any
        result = "Result of the save operation"  # Define the result
        self.history_facade.save_history(operation, args, result)
