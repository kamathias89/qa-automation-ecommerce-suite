from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Mapeamento dos seletores da página de login
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"

    def navigate(self, url: str):
        """Acessa a URL da página de login."""
        self.page.goto(url)

    def login(self, username: str, password: str):
        """Preenche as credenciais e executa o login."""
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)