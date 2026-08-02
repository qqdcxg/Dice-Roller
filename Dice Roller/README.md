# Dice Roller

A simple Python project for simulating dice rolls and calculating the average result.

## Contents

- `roll_the_dice.py` - command-line version of the dice roller.
- `roll_the_dice_ui.py` - graphical user interface version using `tkinter`.

## Features

- Simulate rolling a six-sided die multiple times.
- Calculate and display the average face value.
- Includes both console and GUI interfaces.
- GUI now shows a die preview image that updates after each roll.

## Requirements

- Python 3.8+
- `tkinter` (usually included with Python on Windows and macOS)

## Usage

### Command-line

```bash
python roll_the_dice.py
```

Then enter the number of rolls when prompted.

### GUI

```bash
python roll_the_dice_ui.py
```

A window will open where you can enter the number of dice rolls and click `Roll Dice`.

## Notes

- The GUI version uses `tkinter` and is designed for a clean and colorful user experience.
- The core logic is implemented in `roll_dice(times)` inside `roll_the_dice.py`, so the same function can be reused in other interfaces.

## License

This project is open source. You can add a license of your choice, for example `MIT`.
