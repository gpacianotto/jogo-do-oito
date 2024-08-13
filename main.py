import flet as ft
from componentes import tabuleiro
from componentes.PainelControleComponents import painel_controle

def main(page: ft.Page):
    page.title = "Jogo do 8"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 500
    page.window.height = 500
    page.session.set("loading", False)

    tb = tabuleiro.Tabuleiro(page=page)
    pc = painel_controle.PainelControle(page=page, tb=tb)

    tb.render()
    pc.render()

ft.app(main)