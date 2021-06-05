from ..utils.request_helper import RequestHelper
from ..model.repository import Repository as RepositoryModel
from ..repository.user import User as UserRepository
from..repository.repository import Repository


class Git:

    async def get_repository_by_name(self, repositorieName: str, save_data: bool):
        # if not save_data:

        if not save_data:
            endpoint = "users/" + repositorieName + "/repos"
            get_resp = await RequestHelper.get_request(endpoint)
            if not get_resp:
                return False

            return await RequestHelper.get_request(endpoint)

    async def get_user_repos(self, username: str, from_local: bool = False):

        print(username)
        if not from_local:
            endpoint = "users/" + username + "/" + "repos"
            resp_json = await RequestHelper.get_request(endpoint)
            if not resp_json:
                return None

            if not resp_json[0]["owner"]:
                return False

            if resp_json[0]["owner"]["login"] == username:
                userRpository = UserRepository()
                user = userRpository.get_by_username(username)
                if not user:
                    user = userRpository.save(username)

            for repo in resp_json:
                repository_model = RepositoryModel(repo, user)
                repository_repo = Repository()
                repository_repo.save(repository_model)

            return resp_json

        repository_repo = Repository()
        return repository_repo.get_repository_by_userid(user)

    def validate_user(resp_json, username):
        if not resp_json[0]["owner"]:
            return False

        if resp_json[0]["owner"]["login"] == username:
            return username
