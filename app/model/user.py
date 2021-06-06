
class User:

    def __init__(self, user):
        try:
            self.__id = user[0]
            self.__username = user[1]
        except Exception as error:
            print(error)


    @property
    def username(self):
        return self.__username

    @property
    def id(self):
        return self.__id


