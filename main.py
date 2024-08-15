import flet as ft
from componentes import tabuleiro
from componentes.PainelControleComponents import painel_controle

def main(page: ft.Page):
    page.title = "Jogo do 8"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 500
    page.window.height = 500
    page.session.set("loading", False)
    page.session.set("config_refresh_time", 500)

    tb = tabuleiro.Tabuleiro(page=page)
    pc = painel_controle.PainelControle(page=page, tb=tb)

    tb.render()
    pc.render()

ft.app(main)