import flet as ft
import math
from componentes import peca
from utils import instance_manager as im

class Tabuleiro():

    def __init__(self, page:ft.Page):
        self.pecas = [
            [peca.Peca(1, self.move, page), peca.Peca(2, self.move, page), peca.Peca(3, self.move, page)],
            [peca.Peca(4, self.move, page), peca.Peca(5, self.move, page), peca.Peca(6, self.move, page)],
            [peca.Peca(7, self.move, page), peca.Peca(8, self.move, page), peca.Peca(9, self.move, page)],
        ]
        self.page = page
        self.data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text(""))
            ],
            rows=self.render_pecas(),
            divider_thickness=0,
            horizontal_lines=ft.BorderSide(width=0),
            
        )
    
    def getMovablePecas(self) -> list[peca.Peca]:

        result = []

        for rows in self.pecas:
            for peca in rows:
                distance_to_nine = self.getDistanceToNine(peca.value)
                if distance_to_nine == 1:
                    result.append(peca)

        return result

    def getDistanceToNine(self, index:int):
        i, j, i9, j9 = self.findPecaIndexAndNine(index)

        return self.calculateDistance(i=i, j=j, i2=i9, j2=j9)

    def findPecaIndex(self, index:int):
        matrix = self.pecas
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j].value == index:
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
        

        distance_to_nine = self.getDistanceToNine(index=index)

        if distance_to_nine > 1 :
            return False
        
        return True
    
    def calculateDistance(self, i, j, i2, j2):
        return math.sqrt(((i - i2) ** 2) + ((j - j2) ** 2))
        
    def swapPecas(self, i, j, i9, j9):

        pecas = self.pecas

        aux = pecas[i][j]

        pecas[i][j] = pecas[i9][j9]
        pecas[i9][j9] = aux

        self.pecas = pecas
        return

    def move(self, index:int):
        
        if self.isMovable(index=index) :
            i, j, i9, j9 = self.findPecaIndexAndNine(index)
            self.swapPecas(i=i, j=j, i9=i9, j9=j9)
            self.reRender()
        return
    
    def render_pecas(self):
        return [
            ft.DataRow(
                cells=[
                    ft.DataCell(self.pecas[0][0].render()),
                    ft.DataCell(self.pecas[0][1].render()),
                    ft.DataCell(self.pecas[0][2].render()),
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(self.pecas[1][0].render()),
                    ft.DataCell(self.pecas[1][1].render()),
                    ft.DataCell(self.pecas[1][2].render()),
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(self.pecas[2][0].render()),
                    ft.DataCell(self.pecas[2][1].render()),
                    ft.DataCell(self.pecas[2][2].render()),
                ]
            ),
        ]
    

    def reRender(self, e=""):
        self.printPecasValue()
        self.data_table.rows = self.render_pecas()
        ft.Page.update(self.page)
        return

    def render(self):
        self.page.add(
            ft.Row(
                [
                    self.data_table
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

        return 