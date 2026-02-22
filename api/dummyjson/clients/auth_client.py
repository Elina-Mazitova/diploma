from api.dummyjson.clients.base_client import BaseClient


class AuthClient(BaseClient):

    def login(self, username: str, password: str):
        body = {
            "username": username,
            "password": password,
            "expiresInMins": 30
        }
        return self.post("/auth/login", json=body)

    def login_negative(self, **kwargs):
        return self.post("/auth/login", json=kwargs)
