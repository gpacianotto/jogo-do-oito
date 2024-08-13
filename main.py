import flet as ft
from componentes import tabuleiro
from utils import instance_manager

def main(page: ft.Page):
    page.title = "Jogo do 8"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 350
    page.window.height = 350

    im = instance_manager.InstanceManager()

    im.set_state("tabuleiro", tabuleiro.Tabuleiro(page))

    tb = im.get_state("tabuleiro")

    tb.render()

ft.app(main)