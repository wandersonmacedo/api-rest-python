from ..config.database import Database
from ..model.user import User as UserModel


class User(Database):

    def save(self, user: str):
        if not user:
            return False

        super().query.execute("""INSERT INTO users (username) VALUES (%s)""", ([user]))
        return super().connect.commit()

    def get_all(self):
        super().query.execute('SELECT * FROM users')
        return super().query.fetchall()

    def get_by_id(self, user_id):
        super().query.execute('SELECT * FROM users WHERE id = %s', ([user_id]))
        return super().query.fetchone()

    def get_by_username(self, username):
        super().query.execute('SELECT * FROM users WHERE username = %s', ([username]))
        return super().query.fetchone()
