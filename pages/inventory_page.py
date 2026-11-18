from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        # Mapeamento de elementos da página de produtos/inventário
        self.title_locator = ".title"

    def get_title_text(self) -> str:
        """Retorna o texto do título principal da página."""
        return self.page.locator(self.title_locator).inner_text()