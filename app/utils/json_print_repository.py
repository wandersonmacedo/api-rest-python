
class JsonPrintRepository(object):

    def __init__(self, resp):
        self.url = resp.url
        self.name = resp.name
        self.access_type = resp.access_type
        self.created_at = resp.created_at
        self.updated_at = resp.updated_at
        self.size = resp.size
        self.stars = resp.stars
        self.watchers = resp.watchers
