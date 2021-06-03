from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/repositories/{username}/{from_local}")
def getRepositoryFromUser(username: str, from_local: bool):
    return {"Hello": "World"}


@app.get("/repositories/{repository_name}/{save_data}")
def getRepositoryByName(repository_name: str, save_data: bool):
    return {"item_id": item_id, "q": q}