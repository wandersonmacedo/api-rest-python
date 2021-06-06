

class Repository(object):

    def __init__(self, repo, user_id):
        self.__name = repo["name"]
        self.__url = repo["url"]
        self.__access_type = repo["private"]
        self.__created_at = repo["created_at"]
        self.__updated_at = repo["updated_at"]
        self.__size = repo["size"]
        self.__stars = repo["stargazers_count"]
        self.__watchers = repo["watchers"]
        self.__user_id = user_id

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def access_type(self):
        return self.__access_type

    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__updated_at

    @property
    def size(self):
        return self.__size

    @property
    def stars(self):
        return self.__stars

    @property
    def watchers(self):
        return self.__watchers

    @property
    def user_id(self):
        return self.__user_id



