import flet as ft
from componentes import tabuleiro
from componentes.PainelControleComponents import tab_embaralhar, tab_config, tab_solver, tab_insert_position
class PainelControle:
    def __init__(self, page:ft.Page, tb:tabuleiro.Tabuleiro):
        self.tabuleiro = tb
        self.page = page

        self.tabs = {
            "embaralhar": tab_embaralhar.TabEmbaralhar(page=page, tabuleiro=tb),
            "config": tab_config.TabConfig(page=page),
            "tab_solver": tab_solver.TabSolver(page=page, tabuleiro=tb),
            "tab_insert_position": tab_insert_position.TabInsertPosition(page=page)
        }

        self.to_be_rendered = ft.Tabs(
            selected_index=0,
            animation_duration=500,
            tabs=[
                self.tabs.get("embaralhar").render(),
                self.tabs.get("tab_solver").render(),
                self.tabs.get("config").render(),
                self.tabs.get("tab_insert_position").render()
                
            ],
            expand=1
        )
    
    def render(self):
        self.page.add(self.to_be_rendered)