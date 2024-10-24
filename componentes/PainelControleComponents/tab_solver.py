import flet as ft
from componentes import tabuleiro
from utils.heuristica_soma import HeuristicaSoma
import time
from copy import deepcopy

from utils.move_history import MoveHistory

class TabSolver:
    def __init__(self, page:ft.Page, tabuleiro:tabuleiro.Tabuleiro):

        self.page = page
        self.tabuleiro = tabuleiro

        self.movement_counter = ft.Text("QTDE de Movimentos: 0")
        self.time_marker = ft.Text("Tempo de execução: --:--:--")

        self.run_button = ft.IconButton(
            icon=ft.icons.PLAY_ARROW,
            on_click=self.on_click_run
        )

        self.reset_button = ft.IconButton(
            content=ft.Text("Resetar"),
            icon=ft.icons.CHANGE_CIRCLE,
            on_click=self.on_click_reset
        )

        self.drop_down = ft.Dropdown(
            width=200,
            label="Heurística",
            hint_text="Escolha a Heurística para resolver o jogo",
            options=[
                ft.dropdown.Option("Soma (1 Camada)"),
                ft.dropdown.Option("Soma (2 Camadas)"),
                ft.dropdown.Option("Soma (N Camadas)")
            ],
            on_change=self.on_change_select
        )
        
        self.slider = ft.Slider(value=3, min=3, max=10, scale=1.2, on_change=self.slider_on_change)
        self.text_slider = ft.Text(f"{self.slider.value} camadas")

        self.numeric_input = ft.Column([
            self.slider,
            self.text_slider
        ])


        self.select_heuristic = ft.Row([
            self.drop_down
        ])

        self.content = ft.Column([
            ft.Text("Heurísticas", size=25),
            ft.Text("Selecione a Heurística para resolver o jogo", size=17),
            ft.Row([
                self.select_heuristic,
                self.run_button,
                ft.Column([
                    self.movement_counter,
                    self.time_marker
                ]),
                self.reset_button
            ]),
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND)

        self.to_be_rendered = ft.Tab(
            text="Resolver Jogo",
            content=self.content
        )
    
    def on_click_reset(self, e):
        MoveHistory().clear_history()
        self.movement_counter.value = "QTDE de Movimentos: 0"
        self.time_marker.value = "Tempo de execução: --:--:--"
        self.page.update()
        return

    def slider_on_change(self, e): 
        self.text_slider.value = f"{int(e.control.value)} camadas"
        self.page.update()
        return

    def solve_soma(self, layers:int):
        self.page.session.set("loading", True)
        self.run_button.disabled = True
        self.reset_button.disabled = True
        self.slider.disabled = True
        self.page.update()
        refresh_time = int(self.page.session.get("config_refresh_time")) / 1000
        heuristica = HeuristicaSoma(self.tabuleiro.getRawMatrix(), layers=layers)

        start_time = time.perf_counter()

        move = heuristica.solve()
        move_qdte = 0

        while move != -1:
            time.sleep(refresh_time)
            self.tabuleiro.move(move)
            
            move_qdte += 1
            
            self.movement_counter.value = "QTDE de Movimentos: " + str(move_qdte)
            self.page.update()

            MoveHistory().registrate(deepcopy(self.tabuleiro.getCurrentPosition()))

            heuristica = HeuristicaSoma(self.tabuleiro.getRawMatrix(), layers=layers)
            move = heuristica.solve()
        
        # print("history: ", MoveHistory().history)
        MoveHistory().clear_history()

        end_time = time.perf_counter()

        elapsed_time = end_time - start_time

        # Converter duração 
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time % 1) * 1000)

        # Format the output
        formatted_time = f"{minutes:02}:{seconds:02}:{milliseconds:03}"
        
        self.time_marker.value = f"Tempo de execução: {formatted_time}"

        self.run_button.disabled = False
        self.reset_button.disabled = False
        self.slider.disabled = False
        self.page.session.set("loading", False)
        self.page.update()
    
    # Esse trecho de código foi descartado pois, no livro havia outra heuristica
    # porém ela não foi pedida nesse trabalho
    #  
    # def solve_soma_das_diferencas(self):
    #     self.page.session.set("loading", True)
    #     self.run_button.disabled = True
    #
    #
    #
    #     self.run_button.disabled = False
    #     self.page.session.set("loading", False)

    def on_click_run(self, e):
        heuristic = self.drop_down.value

        if not heuristic:
            # print("please, select an heuristic!")
            return

        if heuristic == "Soma (1 Camada)":
            self.solve_soma(layers=1)
            return
        
        if heuristic == "Soma (2 Camadas)":
            self.solve_soma(layers=2)
            return
        
        if heuristic == "Soma (N Camadas)":
            self.solve_soma(layers=int(self.slider.value))
            return
        
        return


    def on_change_select(self, e):
        if(self.drop_down.value == "Soma (N Camadas)"):
            self.select_heuristic.controls.append(self.numeric_input)
            self.page.update()
            return
        else:
            self.select_heuristic.controls = [self.drop_down]
            self.page.update()
            return
        # print(self.select_heuristic.value)

    def render(self):
        return self.to_be_rendered