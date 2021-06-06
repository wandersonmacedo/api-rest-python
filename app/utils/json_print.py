class JsonPrint(object):
    def __init__(self, user, resp):
        self.id = user.id
        self.username = user.username
        self.repositories = self.get_respositories_names(resp)


    def get_respositories_names(self, resp):
        arrays = []
        if not resp:
            return arrays

        for repo in resp:
            arrays.append(repo["name"])

        return arrays