

# Password Manager

This is a simple password manager application built with Python and Tkinter. It allows you to generate secure passwords, save them, and retrieve them for different websites.

## Features

- Generate secure passwords with a mix of letters, numbers, and symbols.
- Save website login details in a JSON file.
- Retrieve saved login details for websites.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/password-manager.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd password-manager
    ```
3. **Install the required packages:**
    ```bash
    pip install pyperclip
    ```

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```
2. **Use the UI to:**
   - Generate passwords
   - Save login details
   - Search for saved passwords

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- pyperclip

## Files

- `main.py`: The main script for the password manager.
- `data.json`: The file where the login details are saved (created automatically).
- `logo.png`: The logo image used in the UI (ensure this is in the same directory as `main.py`).
