import flet as ft
from componentes import tabuleiro
from componentes.PainelControleComponents import painel_controle

def main(page: ft.Page):
    page.title = "Jogo do 8"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 700
    page.window.height = 700
    page.session.set("loading", False)
    page.session.set("config_refresh_time", 10)
    page.window.maximized = True

    tb = tabuleiro.Tabuleiro(page=page)
    pc = painel_controle.PainelControle(page=page, tb=tb)

    tb.render()
    pc.render()
    # Oi, mexendo no código

ft.app(main)