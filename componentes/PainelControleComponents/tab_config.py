import flet as ft

class TabConfig:
    def __init__(self, page:ft.Page):
        self.page = page
        initial_value = int(self.page.session.get("config_refresh_time"))
        self.slider = ft.Slider(value=initial_value, min=10,scale=1.2, max=1000, on_change=self.on_change )
        self.text_slider = ft.Text(f"{self.slider.value} milissegundos")
        self.save_button = ft.TextButton(content=ft.Text("Salvar Alterações"), on_click=self.save_changes, disabled=True)
        self.content = ft.Column([
            ft.Text("Configurações", size=25),
            ft.Text("Tempo da Animação", size=17),
            ft.Row([
                self.slider,
                self.text_slider,
                self.save_button
            ], alignment="center")
        ], horizontal_alignment="right", alignment=ft.MainAxisAlignment.SPACE_AROUND)

        self.to_be_rendered = ft.Tab(
            text="Configurações",
            content=self.content
        )

    def on_change(self, e):
        self.save_button.disabled = False
        self.text_slider.value = f"{int(e.control.value)} milissegundos"
        self.page.update()

    def save_changes(self, e):
        self.page.session.set("config_refresh_time", int(self.slider.value))
        self.save_button.disabled = True
        self.page.update()

    
    def render(self):
        return self.to_be_rendered