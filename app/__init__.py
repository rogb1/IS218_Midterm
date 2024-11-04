import pkgutil
import importlib
from app.history.history_handler import HistoryHandler
from app.commands.menu_command import MenuCommand
from app.commands import Command
from app.commands import CommandHandler, register_commands
import logging
class App: 
    #added 2 lines self.history and the line under and the history handler import
    def __init__(self):
        self.command_handler = CommandHandler()
        self.command_handler.register_command('menu', MenuCommand(self.command_handler))  # Register MenuCommand
        self.history_handler = HistoryHandler()  # Initialize HistoryHandler
        register_commands(self.command_handler)

    def load_plugins(self):
        logging.info("Loading plugins...")
        try:
            # The existing load_plugins logic goes here
            # For example:
            plugins_package = 'app.plugins'
            print("Loading plugins...")
            for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
                if not is_pkg:  # Skip sub-packages, only load modules
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    for item_name in dir(plugin_module):
                        item = getattr(plugin_module, item_name)
                    # Register if item is a subclass of Command, excluding Command itself
                        if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                            self.command_handler.register_command(plugin_name, item())
            register_commands(self.command_handler)
        
        except Exception as e:
            logging.error(f"Failed to load plugin: {e}")
            raise
    

    def start(self):
        self.load_plugins()
        print("Hello Professor! Type 'menu' to display all available commands and type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip()
            if user_input.lower() == 'exit':
                raise SystemExit("Exiting calculator, have a great day!...")
            parts = user_input.split()
            command_name = parts[0]
            args = parts[1:]

            try:# added result= and if result and the line under it but thats it
                result = self.command_handler.execute_command(command_name, *args)
                if result is not None:
                    self.history_handler.save_history(command_name, args, result)  # Save to history
            except Exception as e:
                logging.error(f'ERROR:{e}')
                print(f"Error: {e}")
    