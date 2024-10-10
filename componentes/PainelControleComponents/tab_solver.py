import flet as ft
from componentes import tabuleiro
from utils.heuristica_soma import HeuristicaSoma
import time

class TabSolver:
    def __init__(self, page:ft.Page, tabuleiro:tabuleiro.Tabuleiro):

        self.page = page
        self.tabuleiro = tabuleiro

        self.run_button = ft.IconButton(
            icon=ft.icons.PLAY_ARROW,
            on_click=self.on_click_run
        )
        self.select_heuristic = ft.Dropdown(
            width=200,
            label="Heurística",
            hint_text="Escolha a Heurística para resolver o jogo",
            options=[
                ft.dropdown.Option("Soma"),
                ft.dropdown.Option("Soma das Diferenças")
            ],
            on_change=self.on_change_select
        )

        self.content = ft.Column([
            ft.Text("Heurísticas", size=25),
            ft.Text("Selecione a Heurística para resolver o jogo", size=17),
            ft.Row([
                self.select_heuristic,
                self.run_button
            ]),
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND)

        self.to_be_rendered = ft.Tab(
            text="Resolver Jogo",
            content=self.content
        )
    
    def solve_soma(self):
        self.page.session.set("loading", True)
        self.run_button.disabled = True
        self.page.update()
        refresh_time = int(self.page.session.get("config_refresh_time")) / 1000
        heuristica = HeuristicaSoma(self.tabuleiro.getRawMatrix(), 1)

        move = heuristica.solve()

        while move != -1:
            time.sleep(refresh_time)
            self.tabuleiro.move(move)
            heuristica = HeuristicaSoma(self.tabuleiro.getRawMatrix(), 1)
            move = heuristica.solve()
        
        self.run_button.disabled = False
        self.page.session.set("loading", False)
        self.page.update()

    def solve_soma_das_diferencas(self):
        self.page.session.set("loading", True)
        self.run_button.disabled = True



        self.run_button.disabled = False
        self.page.session.set("loading", False)

    def on_click_run(self, e):
        heuristic = self.select_heuristic.value

        if not heuristic:
            print("please, select an heuristic!")
            return

        if heuristic == "Soma":
            self.solve_soma()
            return
        
        if heuristic == "Soma das Diferenças":
            self.solve_soma_das_diferencas()
            return
        
        return


    def on_change_select(self, e):
        print(self.select_heuristic.value)

    def render(self):
        return self.to_be_rendered