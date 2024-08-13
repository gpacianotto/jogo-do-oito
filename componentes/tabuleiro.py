import flet as ft
import math
from componentes import peca
from utils import instance_manager as im

class Tabuleiro():

    def __init__(self, page:ft.Page):
        self.pecas = [
            [peca.Peca(1, self.move), peca.Peca(2, self.move), peca.Peca(3, self.move)],
            [peca.Peca(4, self.move), peca.Peca(5, self.move), peca.Peca(6, self.move)],
            [peca.Peca(7, self.move), peca.Peca(8, self.move), peca.Peca(9, self.move)],
        ]
        self.page = page
        self.container = ft.Container(
            content=ft.Column(self.renderPecas(), spacing=10),
            bgcolor=ft.colors.ORANGE_ACCENT_100,
            border_radius=20,
            alignment=ft.alignment.center,
            padding=10
        )
    
    def findPecaIndex(self, index:int):
        matrix = self.pecas
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j].value == index:
                    print("value = " + str(index) + " i: "+ str(i) + " j: "+str(j))
                    return i, j
    
    def printPecasValue(self):
        pecasValue = [
            [self.pecas[0][0].value, self.pecas[0][1].value, self.pecas[0][2].value],
            [self.pecas[1][0].value, self.pecas[1][1].value, self.pecas[1][2].value],
            [self.pecas[2][0].value, self.pecas[2][1].value, self.pecas[2][2].value],
        ]
        print(pecasValue)
        return

    def findPecaIndexAndNine(self, index):
        i9, j9 = self.findPecaIndex(index=9)
        i,j = self.findPecaIndex(index=index)

        return i, j, i9, j9

    def isMovable(self, index:int):
        i, j, i9, j9 = self.findPecaIndexAndNine(index)

        distance_to_nine = self.calculateDistance(i=i, j=j, i2=i9, j2=j9)

        print("distance to nine = " + str(distance_to_nine))

        if distance_to_nine > 1 :
            return False
        
        return True
    
    def calculateDistance(self, i, j, i2, j2):
        return math.sqrt(((i - i2) ** 2) + ((j - j2) ** 2))
        
    def swapPecas(self, i, j, i9, j9):

        pecas = self.pecas

        aux = pecas[i][j]
        aux2 = pecas[i9][j9]

        pecas[i][j] = aux2
        pecas[i9][j9] = aux

        self.pecas = pecas
        return

    def move(self, index:int):
        
        if self.isMovable(index=index) :
            print("moving "+str(index))
            i, j, i9, j9 = self.findPecaIndexAndNine(index)
            self.swapPecas(i=i, j=j, i9=i9, j9=j9)
            print(str(index) + " swapped, rendering...")
            # self.printPecasValue()
            # self.reRender()
        return

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
    

    def reRender(self, e):
        self.printPecasValue()
        print(self.__class__.__text_signature__)
        self.container.content.clean()
        self.container.content = ft.Column(self.renderPecas(), spacing=10)
        ft.Page.update(self.page)
        return

    def render(self):
        self.page.add(
            ft.Row(
                [
                    self.container,
                    ft.TextButton("render again", on_click=self.reRender)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

        return 