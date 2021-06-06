from ..utils.request_helper import RequestHelper
from ..model.repository import Repository as RepositoryModel
from ..repository.user import User as UserRepository
from ..model.user import User as UserModel
from ..repository.repository import Repository


class User:

    def validate_user(resp_json, username):
        if not resp_json[0]["owner"]:
            return False

        if resp_json[0]["owner"]["login"] == username:
            return username

    def json_parse(self):
        pass

    def find_or_create(self, username: str):
        user_repository = UserRepository()
        user = user_repository.get_by_username(username)
        if not user:
            user_repository.save(username)
            user = user_repository.get_by_username(username)

        return UserModel(user)
