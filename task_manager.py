# M06T08 CAPSTONE PROJECT
# Auto-Graded Task 1+2+3 - Task Manager RE-FACTORISED
# ===== Importing external modules ===========
import os
from datetime import datetime
import repository
import services

# ==== Defining functions ========
"""
The reg_user function allows the admin to register a new user. It prompts
the admin to enter a new username and password, checks if the username
already exists, and if not, it writes the new user to the user.txt file
and updates the users dictionary.
"""


def reg_user(new_username=None, new_password=None, confirm_password=None):
    os.system("cls")
    while True:

        if new_username is None:
            new_username = input("New username: ")

        if not services.can_register_user(repository.load_users(),
                                          new_username):
            print("Username already exists.")
            return False

        if new_password is None:
            new_password = input("New password: ")

        if confirm_password is None:
            confirm_password = input("Confirm password: ")

        if new_password == confirm_password:

            with open("user.txt", "a") as file:
                file.write(f"\n{new_username}, {new_password}")

            users[new_username] = new_password

            print("User added successfully")
            return True
            break

        else:
            print("Passwords do not match.")
            return False


"""
The add_task function allows the user to add a new task. It prompts the
user to enter the details of the task, including the assigned user, title,
description, and due date. It then writes the task to the tasks.txt file
with the current date and a completion status of "No". The function also
includes validation to ensure that the assigned user exists in the users
dictionary.
"""


def add_task(assigned_user=None, task_title=None, task_description=None,
             due_date=None):
    os.system("cls")
    while True:

        if assigned_user is None:
            assigned_user = input("Assigned to: ")

        if assigned_user in repository.load_users():
            break
        else:
            print("User not found. Please enter a valid username.")
            return False

    if task_title is None:
        task_title = input("Task title: ")

    if task_description is None:
        task_description = input("Task description: ")

    if due_date is None:
        due_date = input("Due date (dd Mmm yyyy): ")

    # The current date is obtained using the datetime module and formatted
    # as "day month year".
    current_date = datetime.today().strftime("%d %b %Y")

    completed = "No"

    with open("tasks.txt", "a") as file:
        file.write(
            f"\n{assigned_user}, "
            f"{task_title}, "
            f"{task_description}, "
            f"{current_date}, "
            f"{due_date}, "
            f"{completed}"
        )
    os.system("cls")
    print("Task added successfully")
    return True


"""
The view_all function reads the tasks from the tasks.txt file and prints
the details of each task in a formatted manner. It displays the task title,
assigned user, date assigned, due date, completion status, and description.
"""


def view_all():
    os.system("cls")
    print("All Tasks:")
    with open("tasks.txt", "r") as file:

        for line in file:

            task = line.strip().split(", ")

            print("\n------------------------")
            print(f"Task:               {task[1]}")
            print(f"Assigned to:        {task[0]}")
            print(f"Date assigned:      {task[3]}")
            print(f"Due date:           {task[4]}")
            print(f"Task Completed?     {task[5]}")
            print(" Description:                 ")
            print(f" {task[2]}                  ")
            print("------------------------")


"""
The view_mine function allows the user to view and manage their assigned
tasks. It reads the tasks from the tasks.txt file, filters the tasks that
are assigned to the logged-in user, and displays them with corresponding
numbers. The user can then select a task by its number to either mark it
as complete or edit it. If the user chooses to edit a task, it changes
the assigned user and due date,  but only if the task is not already
marked as complete. After making changes, the function saves the updated
list of tasks back to the tasks.txt file.
"""


def view_mine():

    os.system("cls")
    # Create an empty list to store tasks
    tasks = []

    # Read all tasks from tasks.txt
    with open("tasks.txt", "r") as file:

        for line in file:

            task = line.strip().split(", ")
            # Append each task (as a list) to the tasks list
            tasks.append(task)

    # Create another empty list to store only current user's tasks
    user_tasks = []

    for task in tasks:

        if task[0] == username:
            # If the assigned user of the task matches the logged-in
            # username, it appends that task to the user_tasks list.
            user_tasks.append(task)

    # Check if user has tasks
    if len(user_tasks) == 0:
        print("You have no assigned tasks.")
        return

    # Display user's tasks with numbers
    print(f"Tasks assigned to {username}:\n")

    for index, task in enumerate(user_tasks, start=1):

        print(f"""
Task Number:       {index}
Task:              {task[1]}
Date assigned:     {task[3]}
Due date:          {task[4]}
Task complete?     {task[5]}
Description:
 {task[2]}
--------------------------------------------------
""")

    # Recursive function to get valid task number input from user when
    # receiving the task number input from the user, allowing them to
    # return to the menu by entering -1 or to select a valid task number
    # for editing.
    def get_valid_task_number():

        try:
            task_number = int(
                input(
                    "Enter task number to edit or -1 to return to menu:"
                    )
            )

            # Base case - return to menu
            if task_number == -1:
                return -1

            # Valid task number
            elif 1 <= task_number <= len(user_tasks):
                return task_number

            else:
                # If the user enters a number that is not within the
                # valid range of task numbers, it prints an error
                # message and calls itself recursively to prompt the
                # user again.
                print("Invalid task number.")
                return get_valid_task_number()

        except ValueError:
            # If the user enters a non-integer value, it catches the
            # ValueError, prints an error message, and calls itself
            # recursively to prompt the user again.
            print("Please enter a valid number.")
            return get_valid_task_number()

    # Call recursive function
    task_number = get_valid_task_number()

    # Return to menu
    if task_number == -1:
        return

    # Get selected task
    selected_task = user_tasks[task_number - 1]

    # Task options
    print("""
Select an option:
1 - Mark task as complete
2 - Edit task
""")

    option = input("Option: ")

    # MARK TASK COMPLETE
    if option == "1":

        selected_task[5] = "Yes"

        print("Task marked as complete.")

    # EDIT TASK
    elif option == "2":

        # Prevent editing completed tasks
        if selected_task[5] == "Yes":

            print("Completed tasks cannot be edited.")
            return

        # Edit username
        while True:
            new_user = input(
                "Enter new username " "(or press Enter to keep current):")

            if new_user != "":
                if new_user in repository.load_users():
                    selected_task[0] = new_user
                    break
                else:
                    print("User does not exist.")
            else:
                break

        # Edit due date
        new_due_date = input(
            "Enter new due date " "(or press Enter to keep current): ")

        if new_due_date != "":
            selected_task[4] = new_due_date

        print("Task updated successfully.")

    else:
        print("Invalid option.")
        return

    # Rewrite ALL tasks back to tasks.txt
    repository.save_tasks(tasks)
    print("Changes saved successfully.")


"""
The view_completed function reads the tasks from the tasks.txt file and
prints the details of the tasks that are marked as completed. It filters
the tasks based on their completion status and displays them in a format-
ted manner similar to the view_all function, but only for tasks that have
"Yes" in the completion status field. This function is only accessible to
the admin user, as indicated in the menu options.
"""


def view_completed():
    os.system("cls")
    print("Completed Tasks:")

    with open("tasks.txt", "r") as file:

        for line in file:

            task = line.strip().split(", ")

            if task[5] == "Yes":

                print("\n------------------------")
                print(f"Task:               {task[1]}")
                print(f"Assigned to:        {task[0]}")
                print(f"Date assigned:      {task[3]}")
                print(f"Due date:           {task[4]}")
                print(f"Task Completed?     {task[5]}")
                print("Description:")
                print(f"{task[2]}")
                print("------------------------")


"""
The delete_task function allows the admin to delete a task. It reads the
tasks from the tasks.txt file, displays them with corresponding numbers,
and prompts the admin to enter the number of the task they want to delete.
If the entered number is valid, it removes that task from the list and
writes the updated list back to the tasks.txt file. The function also
includes error handling for invalid task numbers and non-integer inputs,
allowing the admin to try again if they enter an invalid input.
"""


def delete_task():
    os.system("cls")

    tasks = []

    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    print("Tasks:\n")

    for index, task in enumerate(tasks, start=1):

        task_data = task.strip().split(", ")

        print(f"{index}. {task_data[1]} assigned to {task_data[0]}")

    try:

        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(tasks):

            del tasks[task_number - 1]
            # After deleting the task from the list, it writes the updated
            # list back to the tasks.txt file, clears the screen.
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            os.system("cls")
            print("Task deleted successfully.")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


"""
The generate_reports function reads the tasks from the tasks.txt file
and generates two reports: task_overview.txt and user_overview.txt. The
task_overview.txt report contains statistics about the total number of
tasks, completed tasks, uncompleted tasks, overdue tasks, and their
respective percentages. The user_overview.txt report contains statistics
for each user, including the number of tasks assigned to them,
the percentage of total tasks they have, and the percentages of their
completed, uncompleted, and overdue tasks. In the function we use the
datetime module to compare due dates with the current date to determine
if tasks are overdue.
"""


def generate_reports():

    tasks = repository.load_tasks()

    total_tasks = len(tasks)
    # Initialize counters for completed, uncompleted, and overdue tasks.
    # These counters will be used to calculate the statistics for the
    # task overview report.
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0
    # Get the current date to compare with task due dates for overdue
    # calculations
    current_date = datetime.today()

    # TASK OVERVIEW CALCULATIONS

    for task in tasks:
        # Convert due date string to datetime object for comparison
        due_date = datetime.strptime(task[4], "%d %b %Y")

        completed = task[5]

        # Count completed tasks
        if completed == "Yes":
            completed_tasks += 1

        # Count uncompleted tasks
        else:
            uncompleted_tasks += 1

            # Count overdue tasks
            if due_date < current_date:
                overdue_tasks += 1

    # Avoid division by zero when calculating percentages. If there are
    # no tasks, we set the percentages to 0 to prevent a division by
    # zero error.
    if total_tasks > 0:

        incomplete_percentage = (uncompleted_tasks / total_tasks) * 100

        overdue_percentage = (overdue_tasks / total_tasks) * 100

    else:

        incomplete_percentage = 0
        overdue_percentage = 0

    # WRITE task_overview.txt

    with open("task_overview.txt", "w") as file:

        file.write(f"Total tasks: {total_tasks}\n")
        file.write(f"Completed tasks: {completed_tasks}\n")
        file.write(f"Uncompleted tasks: {uncompleted_tasks}\n")
        file.write(f"Overdue tasks: {overdue_tasks}\n")
        file.write(" Percentage incomplete: ")
        file.write(f"{incomplete_percentage:.2f}%\n")
        file.write(" Percentage overdue: ")
        file.write(f"{overdue_percentage:.2f}%\n")

    # USER OVERVIEW CALCULATIONS

    with open("user_overview.txt", "w") as file:

        # Total users
        total_users = len(users)
        file.write(f"Total users: {total_users}\n")
        file.write(f"Total tasks: {total_tasks}\n\n")

        # Loop through each user
        for user in users:
            """
            Initialize counters for each user to calculate their
            statistics. These counters will be used to calculate the
            number of tasks assigned to the user, the percentage of
            total tasks they have, and the percentages of their
            completed, uncompleted, and overdue tasks.
            """
            user_task_total = 0
            user_completed = 0
            user_uncompleted = 0
            user_overdue = 0

            # Check every task
            for task in tasks:

                if task[0] == user:

                    user_task_total += 1
                    # Convert due date string to datetime object for
                    # comparison
                    due_date = datetime.strptime(task[4], "%d %b %Y")

                    if task[5] == "Yes":
                        user_completed += 1

                    else:
                        user_uncompleted += 1

                        if due_date < current_date:
                            user_overdue += 1

            # Avoid division by zero
            if total_tasks > 0:

                assigned_percentage = (
                    user_task_total / total_tasks) * 100

            else:
                assigned_percentage = 0

            if user_task_total > 0:

                completed_percentage = (
                    user_completed / user_task_total) * 100
                uncompleted_percentage = (
                    user_uncompleted / user_task_total) * 100
                overdue_percentage = (
                    user_overdue / user_task_total) * 100

            else:

                completed_percentage = 0
                uncompleted_percentage = 0
                overdue_percentage = 0

            # WRITE USER DATA

            file.write(f"User: {user}\n")
            file.write(" Tasks assigned: ")
            file.write(f"{user_task_total}\n")
            file.write(" Percentage of total tasks: ")
            file.write(f"{assigned_percentage:.2f}%\n")
            file.write(" Completed tasks percentage: ")
            file.write(f"{completed_percentage:.2f}%\n")
            file.write(" Uncompleted tasks percentage: ")
            file.write(f"{uncompleted_percentage:.2f}%\n")
            file.write(" Overdue tasks percentage: ")
            file.write(f"{overdue_percentage:.2f}%\n")
            file.write("\n")

    print("Reports generated successfully.")


"""
The display_statistics function reads the generated reports from
task_overview.txt and user_overview.txt and prints their contents
to the console. If the reports do not exist, it calls the
generate_reports function to create them before displaying. The
function formats the output with headers and separators for better
readability. This function is only accessible to the admin.
"""


def display_statistics():

    os.system("cls")

    # Generate reports if they do not exist
    if not os.path.exists("task_overview.txt"):

        generate_reports()

    if not os.path.exists("user_overview.txt"):

        generate_reports()

    print("\t TASK OVERVIEW")
    print("-----------------------------------")

    # Read and display task overview report
    with open("task_overview.txt", "r") as file:
        print(file.read())
    print("-----------------------------------")

    print("\t USER OVERVIEW")
    print("-----------------------------------")

    # Read and display user overview report
    with open("user_overview.txt", "r") as file:
        print(file.read())
    print("-----------------------------------")
    print(
        "\n("
        "To ensure that the statistics are up to date, please select "
        "the 'Generate Reports' option from the menu first.)"
    )


# ================ End of function definitions ===================


# ==== Login Section ====
def login(users_dict):

    while True:

        print("\t\t Welcome to the Task Manager!")
        print("\t\t Please log in to continue.")

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if services.validate_login(repository.load_users(),
                                   username, password):
            print("Login successful")
            return username

        elif username in repository.load_users():
            os.system("cls")
            print("Incorrect password")

        else:
            os.system("cls")
            print("Username does not exist")


def main():

    global users
    global username

    users = repository.load_users()

    username = login(users)

    os.system("cls")
    while True:
        # Present the menu to the user and
        # make sure that the user input is converted to lower case.
        print(f"Welcome {username}!")
        # Admin Menu
        if username == "admin":

            menu = input("""Please select one of the following options:
        r - register user
        a - add task
        va - view all tasks
        vm - view my tasks
        vc - view completed tasks
        del - delete tasks
        ds - display statistics
        gr - generate reports
        e - exit

        : """).lower()

        # Normal User Menu
        else:

            menu = input("""Please select one of the following options:
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit

        : """).lower()

        if menu == "r" and username == "admin":
            reg_user()

        elif menu == "a":
            add_task()

        elif menu == "va":
            view_all()

        elif menu == "vm":
            view_mine()

        elif menu == "vc" and username == "admin":
            view_completed()

        elif menu == "del" and username == "admin":
            delete_task()

        elif menu == "gr" and username == "admin":
            generate_reports()

        elif menu == "ds" and username == "admin":
            display_statistics()

        # If the user selects the option to exit, it prints a goodbye
        # message and exits the program.
        elif menu == "e":
            print("Goodbye!!!")
            exit()

        # If the user enters an invalid option, it clears the screen
        # and prints an error message.
        else:
            os.system("cls")
            print("You have entered an invalid input. Please try again")


if __name__ == "__main__":
    main()
