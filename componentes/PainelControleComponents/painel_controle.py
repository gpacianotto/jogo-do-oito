import flet as ft
from componentes import tabuleiro
from componentes.PainelControleComponents import tab_embaralhar

class PainelControle:
    def __init__(self, page:ft.Page, tb:tabuleiro.Tabuleiro):
        self.tabuleiro = tb
        self.page = page

        self.tabs = {
            "embaralhar": tab_embaralhar.TabEmbaralhar(page=page, tabuleiro=tb)
        }

        self.to_be_rendered = ft.Tabs(
            selected_index=1,
            animation_duration=500,
            tabs=[
                self.tabs.get("embaralhar").render()
            ],
            expand=1
        )
    
    def render(self):
        self.page.add(self.to_be_rendered)