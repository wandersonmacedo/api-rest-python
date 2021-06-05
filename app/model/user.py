
class User:

    def __init__(self, username: str):
        self.__username = username

    @property
    def username(self):
        return self.__username


