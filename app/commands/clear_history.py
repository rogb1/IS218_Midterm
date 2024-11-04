
from app.commands import Command
from app.history.history_facade import HistoryFacade

class ClearHistoryCommand(Command):
    def __init__(self):
        self.history_facade = HistoryFacade()

    def execute(self):
        self.history_facade.clear_history()
