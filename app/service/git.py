from ..utils.request_helper import RequestHelper


class Git:

    async def get_repository_by_name(self, repositorieName: str):
        endpoint = "users/" + repositorieName + "/repos"
        return await RequestHelper.getRequest(endpoint)

    async def get_user_repos(username: str,from_local: bool):
        if not from_local:
            endpoint = "users/" + username + "/" + "repos"
            return await RequestHelper.getRequest(endpoint)


