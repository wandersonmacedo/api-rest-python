from ..config.database import Database
from ..model.repository import Repository as RepositoryModel
from ..model.user import User as UserModel


class Repository(Database):

    def get_repository_by_userid(self, user: UserModel):
        super().query.execute("SELECT * FROM repository WHERE user_id = %s", ([user.id]))
        return super().query.fetchall()

    def save(self, repository: RepositoryModel):
        try:
            super().query.execute(
                "INSERT INTO repository (name, url, access_type, size, stars, watchers, "
                "created_at, updated_at, user_id) "
                "VALUES "
                "(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    [
                        repository.name, repository.url, repository.access_type, repository.size, repository.stars,
                        repository.watchers, repository.created_at, repository.updated_at, repository.user_id
                    ]
                )
            )
            return super().connect.commit()
        except Exception as error:
            print(error)

    def get_repositories_by_user_name(self, user: UserModel):
        super().query.execute("SELECT name FROM repository WHERE user_id = %s", ([user.id]))
        return super().query.fetchall()

    def get_repository_by_name(self, repository_name: str):
        super().query.execute("SELECT users.username, repository.name "
                              "FROM repository "
                              "JOIN users ON users.id = repository.user_id "
                              "WHERE repository.name = %s",
                              ([repository_name]))
        return super().query.fetchone()

    def update(self, repository: RepositoryModel):
        try:
            super().query.execute(
                "UPDATE repository SET url = %s, SET access_type = %s, SET size = %s, SET stars = %s, "
                "SET watchers = %s, SET created_at = %s, SET updated_at = %s ",
                (
                    [
                        repository.url, repository.access_type, repository.size, repository.stars,
                        repository.watchers, repository.created_at, repository.updated_at
                    ]
                )
            )
            return super().connect.commit()
        except Exception as error:
            print(error)
