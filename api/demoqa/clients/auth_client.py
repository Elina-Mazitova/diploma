from api.demoqa.clients.base_client import BaseClient


class AuthClient(BaseClient):

    def create_user(self, body: dict):
        return self.post("/Account/v1/User", json=body)

    def generate_token(self, body: dict):
        return self.post("/Account/v1/GenerateToken", json=body)

    def login(self, body: dict):
        return self.post("/Account/v1/Login", json=body)
