import unittest

from ..model.user import User


class TestUser(unittest.TestCase):

    def test_user_instance(self):
        userArray = [1, "tester"]
        users = User(userArray)
        self.assertEqual(users.id, 1)
        self.assertEqual(users.username, "tester")

    def test_user_failing_instance(self):
        userArray = [1]
        users = User(userArray)
        self.assertRaises(TypeError, users)




if __name__ == '__main__':
    unittest.main()
