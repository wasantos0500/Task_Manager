"""
Login and registration validation functions for the task management
system. This module provides functions to validate user login
credentials, check if a username is available for registration, and
build task dictionaries with the necessary attributes.
"""


def validate_login(users_dict, username, password):
    return users_dict.get(username) == password


"""
The can_register_user function checks if a given username is available
for registration. It takes a dictionary of existing users and a
username as input, and returns True if the username is not already in
the dictionary, indicating that it can be registered. Otherwise, it
returns False.
"""


def can_register_user(users_dict, username):
    """
    Return True if the username is available,
    otherwise return False.
    """
    return username not in users_dict


"""
The build_task function creates and returns a task dictionary with the
provided details. It takes the assigned user, title, description,
current date, and due date as input parameters, and initializes the
task's completion status to False.
"""


def build_task(assigned_to, title, description, current_date, due_date):
    """
    Creates and returns a task dictionary.
    """

    return {
        "assigned_to": assigned_to,
        "title": title,
        "description": description,
        "current_date": current_date,
        "due_date": due_date,
        "completed": False,
    }
