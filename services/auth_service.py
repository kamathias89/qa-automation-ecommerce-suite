import requests

class AuthService:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def login(self, payload: dict) -> requests.Response:
        """Executa a requisição POST de login na API."""
        url = f"{self.base_url}/login"
        response = requests.post(url, json=payload)
        return response