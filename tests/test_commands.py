import pytest
from app import App
from app import App
from app.commands import MenuCommand, CommandHandler
from app.plugins.exit import ExitCommand
from app.plugins.add import AddCommand
from app.plugins.subtract import SubCommand
from app.plugins.multiply import MultCommand
from app.plugins.divide import DivCommand
from app.history.history_facade import HistoryFacade

def test_app_add_command(capfd, monkeypatch):
    '''Add test'''
    inputs = iter(['add 10 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting calculator, have a great day!...", "The app did not exit as expected"

def test_app_greet_command(capfd, monkeypatch):
    '''Greet test'''
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting calculator, have a great day!...", "The app did not exit as expected"

def test_app_subtract_command(capfd, monkeypatch):
    '''Subtract test'''
    inputs = iter(['subtract 10 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting calculator, have a great day!...", "The app did not exit as expected"

def test_app_multiply_command(capfd, monkeypatch):
    '''Multiply test'''
    inputs = iter(['multiply 10 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting calculator, have a great day!...", "The app did not exit as expected"

def test_app_divide_command(capfd, monkeypatch):
    '''Divide test'''
    inputs = iter(['divide 10 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting calculator, have a great day!...", "The app did not exit as expected"

def test_load_history_command(capfd, monkeypatch):
    '''Load history test'''
    inputs = iter(['load_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "No history found." in captured.out or "timestamp" in captured.out, "No history available to load."

def test_clear_history_command(capfd, monkeypatch):
    '''Clear history test'''
    inputs = iter(['clear_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
         app.start()

    captured = capfd.readouterr()
    assert "History cleared." in captured.out, "No history to clear."

def test_save_history_command(capfd, monkeypatch):
    '''Save history test'''
    inputs = iter(['save_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "History saved successfully." in captured.out, "No history to save."

def test_menu_command(capfd, monkeypatch):
    '''Menu command test'''
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command_handler = CommandHandler()  # Create a CommandHandler instance
    command_handler.register_command('menu', MenuCommand(command_handler))  # Register the MenuCommand
    app = App()  # Create the App instance

    with pytest.raises(SystemExit):
        app.start()  # Start the app, which will execute the menu command

    captured = capfd.readouterr()
    assert "Available commands:" in captured.out, "Menu command did not display available commands."
