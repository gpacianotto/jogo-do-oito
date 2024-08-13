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

        self.content = ft.Column([
            ft.Text("Embaralhe o Jogo:"),
            ft.Row([
                self.slider,
                self.text_slider,
                self.button
            ], alignment="center")
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

        for i in range(int(self.slider.value)):

            pecas = self.tabuleiro.getMovablePecas()

            peca = random.choice(pecas)
            
            print("Step " + str(i) +" - peca taken: " + str(peca.value))

            self.tabuleiro.move(peca.value)

            time.sleep(0.5)
        
        self.page.session.set("loading", False)
        self.button.disabled = False
        self.page.update()
        

    def render(self):
        return self.to_be_rendered