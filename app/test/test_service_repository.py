import unittest
from ..service.repository import Repository as ServiceRepo
from ..service.user import User as UserService


class TestServiceRepository(unittest.TestCase):

    def test_service_instance(self):
        service = ServiceRepo()
        self.assertEqual(service.user, None)
        self.assertEqual(service.user_repos, None)
        self.assertIsInstance(service.user_service, UserService)

    def test_get_user_repos_real(self):
        service = ServiceRepo()
        result = service.get_user_repos("wandersonmacedo", False)
        self.assertIsNotNone(service.user)
        self.assertIsNotNone(service.user_repos)
        self.assertIsInstance(service.user_repos, list)
        self.assertEqual(service.user.username, "wandersonmacedo")

    def test_get_repository_by_name(self):
        service = ServiceRepo()
        result = service.get_repository_by_name("SJAFIBSAKJBFEEEIASKFB", True)
        self.assertEqual(result, [])


    def test_get_user_repos(self):
        service = ServiceRepo()
        self.assertEqual(service.get_user_repos("SJAFIBSAKJBFIASKFB", True), False)


if __name__ == '__main__':
    unittest.main()
