

import logging
from app.commands import Command
from calculator.operations import divide
from calculator.calculation import Calculation
from decimal import Decimal, InvalidOperation

class DivCommand(Command):
    def __init__(self,):
        pass

    def execute(self, *args):
        try:
            if len(args) != 2:
                raise ValueError("You must provide 2 arguments.")
            a = Decimal(args[0])
            b = Decimal(args[1])
            
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")

            calculation = Calculation.create(a, b, divide)
            result = calculation.perform()
            print(f"Result: {result}")
            logging.info(f"Performed division on [{a}, {b}]: Result = {result}")

        except ZeroDivisionError as e:
            logging.error(f"Error performing division on [{args}]: {e}")
            print("Cannot divide by zero.")
        except (ValueError, IndexError, InvalidOperation) as e:
            logging.error(f"Invalid input in division command with args {args}: {e}")
            print("Invalid input, provide two valid numbers.")
