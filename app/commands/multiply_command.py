from . import Command  
import logging
class MultCommand(Command):
    def execute(self, a, b):
        """Multiply a and b and return the result."""
        result = float(a) * float(b)
        logging.info(f'Menu command activated.')
        return result  