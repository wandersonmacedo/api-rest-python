from ..config.database import Database
from ..model.repository import Repository as RepositoryModel


class Repository(Database):

    def get_repository_by_userid(self, user):
        super().query.execute("SELECT * FROM repository WHERE user_id = %s", ([user[0]]))
        return super().query.all()

    def save(self, repository: RepositoryModel):
        super().query.execute(
            "INSERT INTO repository (name, url, access_type, size, stars, watchers, created_at, updated_at, user_id) "
            "VALUES "
            "(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            ([repository.name, repository.url, repository.access_type, repository.size, repository.stars, repository.watchers, repository.created_at, repository.updated_at, repository.user_id])
        )
        return super().connect.commit()
