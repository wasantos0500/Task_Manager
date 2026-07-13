# This code block handles the login of the user. It reads the user.txt
# file and stores the username and password in a dictionary. Then it
# prompts the user to enter their username and password and checks if
# they are correct.
def load_users():
    users = {}

    with open("user.txt", "r") as file:

        for line in file:
            username, password = line.strip().split(", ")
            users[username] = password

    return users


"""
The following function reads the tasks from the tasks.txt file and
returns a list of tasks. Each task is represented as a list of its
attributes (assigned user, title, description, date assigned, due
date, and completion status).
"""


def load_tasks():

    tasks = []

    with open("tasks.txt", "r") as file:

        for line in file:

            task = line.strip().split(", ")

            tasks.append(task)

    return tasks


"""
The save_tasks function takes a list of tasks and writes them back to
the tasks.txt file. Each task is written as a line in the file, with
its attributes separated by commas. These first two functions are used
in the view_mine function to load the tasks, allow the user to edit them,
and then save the changes back to the file.
"""


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:

        for task in tasks:

            file.write(", ".join(task) + "\n")
