from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_successful_login(page):
    # Inicializa as páginas do Page Object
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # Acessa a aplicação de testes (SauceDemo é a massa padrão excelente para portfólios)
    login_page.navigate("https://www.saucedemo.com/")

    # Executa o login com credenciais válidas
    login_page.login("standard_user", "secret_sauce")

    # Valida se fomos direcionados para a página de inventário com sucesso
    assert "inventory.html" in page.url
    assert inventory_page.get_title_text() == "Products"