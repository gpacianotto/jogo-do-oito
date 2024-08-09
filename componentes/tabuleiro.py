import flet as ft
import math
from componentes import peca

class Tabuleiro():

    def __init__(self, page:ft.Page):
        self.pecas = [
            [peca.Peca(1, self), peca.Peca(2, self), peca.Peca(3, self)],
            [peca.Peca(4, self), peca.Peca(5, self), peca.Peca(6, self)],
            [peca.Peca(7, self), peca.Peca(8, self), peca.Peca(9, self)],
        ]
        self.page = page
    
    def findPecaIndex(self, index:int):
        matrix = self.pecas
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j].value == index:
                    return i, j

    def isMovable(self, index:int):
        i9, j9 = self.findPecaIndex(index=9)
        i,j = self.findPecaIndex(index=index)

        print("Distance from 9 = " + str(self.calculateDistance(i=i, j=j, i2=i9, j2=j9)))

        # if i == i9 and j == j9:
        #     return False
        
        # if i == (i9 - 1) or j == (j9 - 1):
        #     return True
    
    def calculateDistance(self, i, j, i2, j2):
        return math.sqrt(((i - i2) ** 2) + ((j - j2) ** 2))
        
    def move(self, index:int):
        print("moving "+str(index))
        self.isMovable(index=index)

    def renderPecas(self):
        return [
            ft.Row([
                self.pecas[0][0].render(),
                self.pecas[0][1].render(),
                self.pecas[0][2].render(),
            ], spacing=10),
            ft.Row([
                self.pecas[1][0].render(),
                self.pecas[1][1].render(),
                self.pecas[1][2].render(),
            ], spacing=10),
            ft.Row([
                self.pecas[2][0].render(),
                self.pecas[2][1].render(),
                self.pecas[2][2].render(),
            ], spacing=10),
        ]

    def render(self):

        self.page.clean()

        self.page.add(
            ft.Row(
                [
                    ft.Container(
                        content=ft.Column(self.renderPecas(), spacing=10),
                        bgcolor=ft.colors.ORANGE_ACCENT_100,
                        border_radius=20,
                        alignment=ft.alignment.center,
                        padding=10
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

        self.page.update()
        return 