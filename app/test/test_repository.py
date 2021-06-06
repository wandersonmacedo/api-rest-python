import unittest

from ..model.repository import Repository


class TestRepository(unittest.TestCase):

    def test_repository_instance(self):
        array = {"name":"teste","url":"http://url","private":"f","created_at":"2019-01-01 10:08:22","updated_at":"2019-01-01 10:08:22","size":"55","stargazers_count":"6" ,"watchers":"3"}
        repo = Repository(array, 1)
        self.assertEqual(repo.name, "teste")
        self.assertEqual(repo.url, "http://url")
        self.assertEqual(repo.access_type, "f")
        self.assertEqual(repo.created_at, "2019-01-01 10:08:22")
        self.assertEqual(repo.updated_at, "2019-01-01 10:08:22")
        self.assertEqual(repo.size, "55")
        self.assertEqual(repo.stars, "6")
        self.assertEqual(repo.watchers, "3")

    def test_repository_failing_instance(self):
        with self.assertRaises(KeyError):
            Repository({"name":""}, 1)

    def test_repository_type_error(self):
        with self.assertRaises(TypeError):
            Repository({"name":""})




if __name__ == '__main__':
    unittest.main()
