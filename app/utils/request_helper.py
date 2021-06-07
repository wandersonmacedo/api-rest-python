import httpx
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()


class RequestHelper:

    github_url = os.getenv("GITHUB_ENDPOINT")

    async def get_request(requested_endpoint: str):

        full_url = RequestHelper.github_url + requested_endpoint
        try:
            async with httpx.AsyncClient() as client:
                resp: httpx.Response = await client.get(full_url, headers=RequestHelper.get_headers())
                resp.raise_for_status()
                return resp.json()
        except Exception as error:
            print(error)
            return None

    def get_headers():
        headers = {'Authorization': 'Bearer ' + os.getenv('GITHUB_TOKEN')}
        return headers
