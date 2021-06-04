import dotenv
import httpx
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class RequestHelper:
    github_url = os.getenv("GITHUB_ENDPOINT")

    async def getRequest(requested_endpoint: str):
        fullUrl = RequestHelper.github_url + requested_endpoint
        print(fullUrl)
        async with httpx.AsyncClient() as client:
            headers = {'Authorization': 'Bearer ' + os.getenv('GITHUB_TOKEN')}
            resp: httpx.Response = await client.get(fullUrl, headers=headers)
            resp.raise_for_status()
            print(resp.json())

            return resp.json()
