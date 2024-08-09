import flet as ft
from componentes import tabuleiro

def main(page: ft.Page):
    page.title = "Jogo do 8"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    tb = tabuleiro.Tabuleiro(page=page)

    tb.render()

ft.app(main)