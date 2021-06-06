from ..utils.request_helper import RequestHelper
from ..model.repository import Repository as RepositoryModel
from ..model.user import User as UserModel
from ..repository.user import User as UserRepository
from ..repository.repository import Repository as RepoRepository
from ..service.user import User as UserService
from ..utils.json_print import JsonPrint
from ..utils.json_print_repository import JsonPrintRepository
import json


class Repository:

    def __init__(self):
        self.user = None
        self.user_repos = None
        self.user_service = UserService()

    async def get_repository_by_name(self, repositorie_name: str, save_data: bool):
        # if not save_data:
        repository_repo = RepoRepository()
        get_resp = repository_repo.get_repository_by_name(repositorie_name)
        if not get_resp:
            return False

        username = get_resp[0]
        endpoint = "repos/" + username + "/" + repositorie_name
        get_repo = await RequestHelper.get_request(endpoint)

        if not get_repo:
            return []

        return self.process_repository_json(get_repo, save_data)

    async def get_user_repos(self, username: str, from_local: bool = False):

        if not from_local:
            endpoint = "users/" + username + "/" + "repos"
            resp_json = await RequestHelper.get_request(endpoint)
            if not resp_json:
                return []

            self.process_json(resp_json, username)
            return self.json_parse(self.user, resp_json)

        resp = self.find_from_local(username)

        return self.json_parse(self.user, resp)

    def find_from_local(self, username):
        repos = []
        repository_repo = RepoRepository()
        user_repo = UserRepository()
        user = user_repo.get_by_username(username)
        if not user:
            return False

        self.user = UserModel(user)
        repos_from_db = repository_repo.get_repository_by_userid(self.user)

        if not repos_from_db:
            return repos

        for repository in repos_from_db:
            repos.append({"name": repository[1]})

        return repos

    def process_json(self, resp_json, username):

        if not resp_json:
            return None

        self.user = self.user_service.find_or_create(username)

        for repo in resp_json:
            repository_model = RepositoryModel(repo, self.user.id)
            repository_repo = RepoRepository()
            repository_repo.save(repository_model)

        return resp_json

    def process_repository_json(self, resp_json, save_data: bool = False):
        if not resp_json:
            return None

        self.user = self.user_service.find_or_create(resp_json["owner"]["login"])
        repository_model = RepositoryModel(resp_json, self.user.id)

        if not save_data:
            return self.json_parse_repository(repository_model)

        repository_repo = RepoRepository()
        repository_repo.update(repository_model)

        return self.json_parse_repository(repository_model)

    def json_parse(self, user, resp):
        if user == False or resp == False:
            return False
        dump_json = JsonPrint(self.user, resp)
        return json.dumps(vars(dump_json))

    def json_parse_repository(self, resp):
        if not resp:
            return False
        dump_json = JsonPrintRepository(resp)
        return json.dumps(vars(dump_json))
