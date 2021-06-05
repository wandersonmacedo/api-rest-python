from typing import Optional

from .service.git import Git
from fastapi import FastAPI

app = FastAPI()


@app.get("/repositories/{username}")
async def get_repositories_by_username(username: str, from_local: Optional[bool] = False):
    git = Git()
    return await git.get_user_repos(username, from_local)


@app.get("/repositories/{repository_name}")
async def get_repository_by_name(repository_name: str, save_data: Optional[bool] = False):
    git = Git()
    return await git.get_repository_by_name(repository_name, save_data)
