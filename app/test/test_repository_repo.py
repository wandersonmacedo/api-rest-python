import unittest

from ..repository.repository import Repository
from ..model.user import User
from ..model.repository import Repository as RepoModel


class TestRepositoryRepo(unittest.TestCase):

    def test_error_cases_getrepobyid(self):
        repo = Repository()
        with self.assertRaises(TypeError):
            repo.get_repository_by_userid()
        with self.assertRaises(AttributeError):
            repo.get_repository_by_userid(1)
        with self.assertRaises(AttributeError):
            repo.get_repository_by_userid(Repository())



    def test_error_cases_save(self):
        repo = Repository()
        with self.assertRaises(TypeError):
            self.assertIsInstance(repo.save())
        with self.assertRaises(TypeError):
            self.assertIsInstance(repo.save(User()))









if __name__ == '__main__':
    unittest.main()
