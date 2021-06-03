import httpx


class Git:

    async def getRepositories(self, repositorieName: str, from_local: bool):
        url = ''

        async with httpx.AsyncClient() as client:
            resp: httpx.Response = await client.get(url)


