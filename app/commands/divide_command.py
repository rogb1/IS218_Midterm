from . import Command 
import logging
class DivCommand(Command):
    def execute(self, a, b):
        """Divide a by b and return the result."""
        if float(b) == 0: 
            print("Error: Cannot divide by zero.")
            logging.error(f'ERROR Cannot divide by zero:[{a}, {b}]')
            return None
        result = float(a) / float(b)

        logging.info(f'Division command activated[{a}, {b}]: Result = {result} ')
        return result  