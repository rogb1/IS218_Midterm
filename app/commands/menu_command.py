from . import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        super().__init__()  # Call the parent class (Command) initializer
        self.command_handler = command_handler  # Store the command handler instance

    def execute(self, *args):
        commands = self.get_registered_commands()
        print("Available commands:")
        for command in commands:
            print(f"- {command}")

    def get_registered_commands(self):
        # Return the list of registered commands from the command handler
        return list(self.command_handler.commands.keys())
