from . import Command  
import logging
class SubCommand(Command):
    def execute(self, a, b):
        """Subtract b from a and return the result."""
        result = float(a) - float(b)

        logging.info(f'Subtracting command activated[{a}, {b}]: Result = {result} ')
        return result  