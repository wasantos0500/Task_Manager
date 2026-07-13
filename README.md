# Task Manager

## Overview

Task Manager is a command-line application developed in Python that allows users to manage daily tasks through a simple menu-driven interface.

## Design Philosophy

The project was redesigned following the principle of Separation of Concerns (via a Virtual Environment), where user interaction, business logic, and file operations are handled by different modules. This approach improves readability, maintainability, and allows the business logic to be tested independently from external resources such as text files.

---

## Features

- User login and authentication
- Register new users (Administrator only)
- Add new tasks
- View all tasks
- View personal tasks
- Edit or complete existing tasks
- Generate task statistics
- Store user and task information using text files

---

## Project Structure

```
Task_Manager/
│
├── task_manager.py       # Main application and menu system
├── services.py           # Business logic
├── repository.py         # File handling functions
├── test_task_manager.py  # Unit tests
├── user.txt              # User data
├── tasks.txt             # Task data
├── requirements.txt      # Project dependencies
└── README.md
```

---

## Technologies Used

- Python 3
- unittest
- Flake8
- Black

---

## Refactoring Improvements

The original application was refactored to improve software design by:

- Separating business logic from file input/output.
- Moving file handling into a dedicated repository module.
- Creating reusable helper functions.
- Improving readability and maintainability.
- Making core functionality suitable for unit testing.

Examples of business logic extracted into reusable functions include:

- `validate_login()`
- `can_register_user()`
- `build_task()`

---

## Running the Application

Open a terminal inside the project folder and run:

```bash
python task_manager.py
```

---

## Running the Unit Tests

Execute the following command:

```bash
python -m unittest -v
```

All tests should complete successfully.

---

## Code Quality

This project follows the PEP 8 style guide.

To check code style:

```bash
flake8 .
```

To automatically format the project:

```bash
black .
```

---

## Dependencies

Install the required packages with:

```bash
pip install -r requirements.txt
```

---

## Author

William A. Santos

Developed as part of a Software Engineering assignment with emphasis on:

- Modular programming
- Refactoring
- Unit Testing
- Separation of Concerns
- Python best practices
