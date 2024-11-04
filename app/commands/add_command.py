from . import Command 
import logging
class AddCommand(Command):
    def execute(self, a, b):
        result = float(a) + float(b)
        logging.info(f'Adding command activated[{a}, {b}]: Result = {result} ')
        return result
