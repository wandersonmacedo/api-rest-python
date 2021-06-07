import unittest
from ..service.repository import Repository as ServiceRepo
from ..service.user import User as UserService
from ..model.user import User as UserModel
from ..model.repository import Repository as RepositoryModel
from ..utils.json_print_repository import JsonPrintRepository
import json

class TestServiceRepository(unittest.TestCase):

    def test_service_instance(self):
        service = ServiceRepo()
        self.assertEqual(service.user, None)
        self.assertEqual(service.user_repos, None)
        self.assertIsInstance(service.user_service, UserService)

    async def test_get_user_repos_real(self):
        service = ServiceRepo()
        result = await service.get_user_repos("wandersonmacedo", False)
        self.assertIsNotNone(service.user)
        self.assertIsNotNone(service.user_repos)
        self.assertIsInstance(service.user_repos, list)
        self.assertEqual(service.user.username, "wandersonmacedo")

    async def test_get_repository_by_name(self):
        service = ServiceRepo()
        result = await service.get_repository_by_name("SJAFIBSAKJBFEEEIASKFB", False)
        self.assertEqual(result[0], False)


    async def test_get_user_repos(self):
        service = ServiceRepo()
        self.assertEqual(await service.get_user_repos("SJAFIBSAKJBFIASKFB", True), False)

    def test_json_encode(self):
        service = ServiceRepo()
        self.assertEqual(service.json_parse(False,'{"teste":True}'), False)
        param = [1, "username"]
        user_object = UserModel(param)
        self.assertIsNot(service.json_parse(user_object, [{"name":"teste"}]), False)
        self.assertEqual(service.json_parse(user_object, [{"name":"teste"}]), "{\"id\": 1, \"username\": \"username\", \"repositories\": [\"teste\"]}")

    def test_json_repository_encode(self):
        service = ServiceRepo()
        self.assertEqual(service.json_parse_repository(None), False)
        param = {"name":"teste","url":"google.com","private":"false","created_at":"date","updated_at":"date","size":"333","stargazers_count":"3","watchers":0}
        user_object = RepositoryModel(param, 1)
        self.assertIsNot(service.json_parse_repository(user_object), False)
        self.assertEqual(service.json_parse_repository(user_object),json.dumps(vars(JsonPrintRepository(user_object))))


if __name__ == '__main__':
    unittest.main()
