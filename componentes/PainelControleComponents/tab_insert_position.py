import flet as ft
from componentes.tabuleiro import Tabuleiro

class TabInsertPosition: 
    def __init__(self, page:ft.Page):
        self.page = page
        #initial_value = int(self.page.session.get("config_refresh_time"))
        #self.slider = ft.Slider(value=initial_value, min=10,scale=1.2, max=1000, on_change=self.on_change )
        #self.text_slider = ft.Text(f"{self.slider.value} milissegundos")
        self.save_button = ft.TextButton(content=ft.Text("Inserir Posição"), on_click=self.save_changes, disabled=True)
        self.error_message = ft.Text(color=ft.colors.RED_500, visible=False)
        self.first_row = ft.Row([
            ft.TextField(value=1, width=100, on_change=self.on_change),
            ft.TextField(value=2, width=100, on_change=self.on_change),
            ft.TextField(value=3, width=100, on_change=self.on_change)
        ],alignment=ft.MainAxisAlignment.CENTER)
        
        self.second_row = ft.Row([
            ft.TextField(value=4, width=100, on_change=self.on_change),
            ft.TextField(value=5, width=100, on_change=self.on_change),
            ft.TextField(value=6, width=100, on_change=self.on_change)
        ], alignment=ft.MainAxisAlignment.CENTER)

        self.third_row = ft.Row([
            ft.TextField(value=7, width=100, on_change=self.on_change),
            ft.TextField(value=8, width=100, on_change=self.on_change),
            ft.TextField(value=9, width=100, on_change=self.on_change)
        ], alignment=ft.MainAxisAlignment.CENTER)

        self.content = ft.Column([
            ft.Text("Inserir Posição", size=25),
            ft.Column([
                self.first_row,
                self.second_row,
                self.third_row
            ]),
            self.error_message,
            self.save_button
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment="center")

        self.to_be_rendered = ft.Tab(
            text="Inserir Posição",
            content=self.content
        )

    def on_change(self, e):
        self.save_button.disabled = False
        self.error_message.visible = False
        self.page.update()

    def extract_position(self):
        
        first_row = []
        second_row = []
        third_row = []

        for i in self.first_row.controls:
            first_row.append(int(i.value))
        
        for i in self.second_row.controls:
            second_row.append(int(i.value))

        for i in self.third_row.controls:
            third_row.append(int(i.value))
        
        result = []

        result.append(first_row)
        result.append(second_row)
        result.append(third_row)

        #print(result)
        return result
    
    def validate_new_position(self, position:list[list[int]]) -> bool:
        
        position_counter = [0,0,0,0,0,0,0,0,0]

        for i in position:
            for j in i:
                if j < 1 or j > 9:
                    return False
                position_counter[j - 1] =+1

        for i in position_counter:
            if i != 1:
                return False
        
        return True

    def save_changes(self, e):
        try:
            position = self.extract_position()
        except:
            self.error_message.value = "Verifique se todos os valores foram preenchidos!"
            self.error_message.visible = True
            self.page.update()        
            return

        if self.validate_new_position(position):
            tabuleiro = Tabuleiro()

            tabuleiro.insertPosition(position=position)
            return
        
        self.error_message.value = "Os valores deve estar entre 1 e 9 e deve ter pelo menos um de cada!"
        self.error_message.visible = True
        self.page.update()        
        return

    
    def render(self):
        return self.to_be_rendered