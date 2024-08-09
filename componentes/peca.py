import flet as ft


class Peca:
    def __init__(self, value : int, tabuleiro ):
        self.value = value
        if value != 9:
            self.content = str(value)
        else :
            self.content = ""
        self.tabuleiro = tabuleiro

    def isNine(self) -> bool:
        if self.value == 9:
            return True
        return False
                
    def on_click(self, e):
        self.tabuleiro.move(self.value)

    def render(self):
        
        container = ft.Container(
            content=ft.Text(self.content, color=ft.colors.BLACK),
            bgcolor=ft.colors.ORANGE_ACCENT_100,
            width=70,
            height=70,
            border_radius=20,
            alignment=ft.alignment.center,
            border=ft.Border(
                top=ft.BorderSide(width=1, color=ft.colors.BLACK),
                bottom=ft.BorderSide(width=1, color=ft.colors.BLACK),
                left=ft.BorderSide(width=1, color=ft.colors.BLACK),
                right=ft.BorderSide(width=1, color=ft.colors.BLACK)
            ),
            on_click=self.on_click
        )

        if self.isNine():
          container.visible = False  

        return container