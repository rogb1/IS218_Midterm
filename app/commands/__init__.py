from abc import ABC, abstractmethod
import logging
class Command(ABC):
   
    @abstractmethod
    def execute(self, *args):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
    
    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str, *args):
        try:
            return self.commands[command_name].execute(*args)
        
        except KeyError:
            logging.warning(f'You have entered an unknown command: {command_name}')
            print(f"No such command: {command_name}")

from app.commands.menu_command import MenuCommand
from app.commands.add_command import AddCommand
from app.commands.subtract_command import SubCommand
from app.commands.multiply_command import MultCommand
from app.commands.divide_command import DivCommand
from app.commands.load_history import LoadHistoryCommand
from app.commands.clear_history import ClearHistoryCommand
from app.commands.save_history import SaveHistoryCommand
def register_commands(handler: CommandHandler):
    handler.register_command('add', AddCommand())
    handler.register_command('subtract', SubCommand())
    handler.register_command('multiply', MultCommand())
    handler.register_command('divide', DivCommand())
    handler.register_command("load_history", LoadHistoryCommand())
    handler.register_command("clear_history", ClearHistoryCommand())
    handler.register_command("save_history", SaveHistoryCommand())
    handler.register_command("menu", MenuCommand(handler))