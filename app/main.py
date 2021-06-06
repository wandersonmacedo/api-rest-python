from typing import Optional

from .service.repository import Repository as RepositoryService
from fastapi import FastAPI

app = FastAPI()


@app.get("/repositories/username/{username}")
async def get_repositories_by_username(username: str, from_local: Optional[bool] = False):
    repo_service = RepositoryService()
    return await repo_service.get_user_repos(username, from_local)


@app.get("/repositories/repository_name/{repository_name}")
async def get_repository_by_name(repository_name: str, save_data: Optional[bool] = False):
    repo_service = RepositoryService()
    return await repo_service.get_repository_by_name(repository_name, save_data)
