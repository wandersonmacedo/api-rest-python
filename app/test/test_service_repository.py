import unittest
from ..service.repository import Repository as ServiceRepo

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_get_repository_by_name(self):
        service = ServiceRepo()



if __name__ == '__main__':
    unittest.main()
