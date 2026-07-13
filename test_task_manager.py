# Testing program for task_manager.py
# Unit tests (5) are included for the following functions:
# 1. & 2. validate_login (tests both successful and unsuccessful login attempts)
# 3. & 4. can_register_user (tests registration of new users and duplicate username detection)
# 5. build_task (tests task creation with correct attributes)

import unittest

import services

class TestTaskManager(unittest.TestCase):

    # -----------------------
    # LOGIN
    # -----------------------

    def test_validate_login_success(self):
        #Test a successful login.
        # Arrange
        users = {
            "admin": "adm1n"
        }

        # Act
        result = services.validate_login(
            users,
            "admin",
            "adm1n"
        )

        # Assert
        self.assertTrue(result)

    def test_validate_login_failure(self):
        # Test an incorrect password.

        users = {
            "admin": "adm1n"
        }

        result = services.validate_login(
            users,
            "admin",
            "wrongpassword"
        )

        self.assertFalse(result)

    # -----------------------
    # REGISTER USER
    # -----------------------

    def test_can_register_new_user(self):
        # Username should be available.

        users = {
            "admin": "adm1n"
        }

        result = services.can_register_user(
            users,
            "alice"
        )

        self.assertTrue(result)

    def test_duplicate_user(self):
        # Duplicate usernames should not be allowed.

        users = {
            "admin": "adm1n"
        }

        result = services.can_register_user(
            users,
            "admin"
        )

        self.assertFalse(result)

    # -----------------------
    # BUILD TASK
    # -----------------------

    def test_build_task(self):
        # Test task creation.

        task = services.build_task(
            "alice",
            "Testing",
            "Write unit tests",
            "10 Jul 2026",
            "20 Jul 2026"
        )

        self.assertEqual(task["assigned_to"], "alice")
        self.assertEqual(task["title"], "Testing")
        self.assertEqual(task["description"], "Write unit tests")
        self.assertEqual(task["current_date"], "10 Jul 2026")
        self.assertEqual(task["due_date"], "20 Jul 2026")
        self.assertFalse(task["completed"])


if __name__ == "__main__":
    unittest.main()