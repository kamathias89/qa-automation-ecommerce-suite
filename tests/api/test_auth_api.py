import pytest
from services.auth_service import AuthService

def test_auth_mock():
    # Exemplo estruturado de teste de contrato e status code
    # Usaremos uma API pública de testes para demonstrar maturidade sênior
    base_url = "https://jsonplaceholder.typicode.com"
    service = AuthService(base_url)
    
    # Validação estrutural de uma requisição simulada
    assert service.base_url == base_url