from ..utils.request_helper import RequestHelper


class Git:

    async def get_repository_by_name(repositorieName: str, save_data: bool):
        if not save_data:
            endpoint = "users/" + repositorieName + "/repos"
            get_resp = RequestHelper.getRequest(endpoint)
            if not get_resp:
                return False


            return await RequestHelper.getRequest(endpoint)

        return False

    async def get_user_repos(username: str,from_local: bool):
        if not from_local:
            endpoint = "users/" + username + "/" + "repos"
            get_resp = RequestHelper.getRequest(endpoint)
            if not get_resp:
                return False

            return await RequestHelper.getRequest(endpoint)

        return False


