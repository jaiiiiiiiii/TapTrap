# Keystroke Logger

## Description
This Python-based keylogger logs keystrokes and saves them to a file with timestamps. It is intended for educational and personal use only, such as monitoring your own system activity.

## Features
- Logs all key presses, including special keys like `space`, `enter`, `backspace`, `tab`, and `esc`
- Saves keystrokes with timestamps for better readability
- Stores logs in a specified directory (`C:\ProgramData\bdlogging` by default)
- Runs in the background and stops when `Esc` is pressed

## Installation
### Prerequisites
- Python 3.x installed
- Required dependencies: `keyboard`

### Install Dependencies
```bash
pip install keyboard
```

## Usage
1. Clone this repository or copy the script to your local system.
2. Run the script using:
```bash
python keylogger.py
```
3. The script will start logging keystrokes and save them in `keystrokes.log` inside `C:\ProgramData\bdlogging`.
4. Press `Esc` to stop the keylogger.

## Configuration
If you want to change the log file directory, modify the following line in the script:
```python
log_directory = r"C:\Your\Custom\Path"
```

## Warnings and Legal Disclaimer
- **This script is for ethical use only.** Do not use it for unauthorized monitoring or malicious activities.
- Ensure you have permission before running this script on any device you do not own.
- Unauthorized keylogging is illegal in many jurisdictions and could result in legal consequences.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## Contact
For any questions or discussions, please open an issue on GitHub.

