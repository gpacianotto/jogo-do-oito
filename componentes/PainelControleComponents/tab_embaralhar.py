import flet as ft
from componentes.tabuleiro import Tabuleiro
import random
import time
class TabEmbaralhar:
    def __init__(self, page:ft.Page, tabuleiro:Tabuleiro):
        self.tabuleiro = tabuleiro
        self.page = page
        self.slider = ft.Slider(value=20, min=10,scale=1.2, max=100, on_change=self.on_change )
        self.text_slider = ft.Text(f"{self.slider.value} passos")
        self.button = ft.TextButton(content=ft.Text("Embaralhar"), on_click=self.shuffle)
        self.noRepeatCheckBox = ft.Checkbox(
            "Não repetir passo anterior",
            value=False
        )

        self.content = ft.Column([
            ft.Text("Embaralhe o Jogo:"),
            ft.Row([
                self.slider,
                self.text_slider,
                
            ], alignment="center"),
            self.noRepeatCheckBox,
            self.button
        ], horizontal_alignment="center", alignment=ft.MainAxisAlignment.SPACE_AROUND)

        self.to_be_rendered = ft.Tab(
            text="Embaralhar",
            content=self.content,
        )
    
    def on_change(self, e):
        self.text_slider.value = f"{int(e.control.value)} passos"
        self.page.update()
    
    def shuffle(self, e):
        self.page.session.set("loading", True)
        self.button.disabled = True
        prevent_previous_step = self.noRepeatCheckBox.value
        previous_step = 0

        refresh_time = int(self.page.session.get("config_refresh_time")) / 1000

        for i in range(int(self.slider.value)):

            pecas = self.tabuleiro.getMovablePecas()

            peca = random.choice(pecas)

            if prevent_previous_step:
                while peca.value == previous_step:
                    peca = random.choice(pecas)
            
            print("Step " + str(i) +" - peca taken: " + str(peca.value))

            self.tabuleiro.move(peca.value)

            if prevent_previous_step:
                previous_step = peca.value

            time.sleep(refresh_time)
        
        self.page.session.set("loading", False)
        self.button.disabled = False
        self.page.update()
        

    def render(self):
        return self.to_be_rendered