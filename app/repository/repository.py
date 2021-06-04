from ..config.database import Database


class Repository(Database):

    def get_repository_by_userid(userid:int):
        users_repo = self.cursor.execute("SELECT * FROM repository WHERE user_id = %s",(userid))
        return users_repo

