import flet as ft


class Peca:
    def __init__(self, value : int, onClick, page:ft.Page):
        self.value = value
        self.onClick = onClick
        self.page = page
        if value != 9:
            self.content = str(value)
        else :
            self.content = ""

    def isNine(self) -> bool:
        if self.value == 9:
            return True
        return False

    def move(self, e):
        loading = self.page.session.get("loading")
        if loading == False:
            self.onClick(self.value)

    def render(self):
        from utils import instance_manager as im
        
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
            on_click=self.move,
        )

        if self.isNine():
            return ft.Container()

        return container