#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):

        row = 0
        col = 0
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 101)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0

    def solve(self):

        maximum = find_max(self.tableWidget)
        self.label_max_el.setText("Максимальный элемент :" + str(maximum))
        max_num = maximum[0]
        row_max_number = maximum[1]
        col_max_number = maximum[2]

        row = 0
        col = 0
        f = False
        l = 0
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                number = self.tableTidget.item(row, col).text()
                if number % 2 == 0:
                    l += 1
                    col+=1
                elif float(number) == maximum[0]:
                    if  row == 0 and col == 0:
                        self.tableWidget.setItem(row,col,QTableWidgetItem(str(number)))
                    else:
                        self.tableWidget.setItem(row,col,QTableWidgetItem(str(l)))
                    self.label_num.setText("Колличество четных чисел : " + str(l))
                    f = True
                    break
                else:
                    self.label_num.setText("Колличество четных чисел : 0")
                    f = True

                    break
            if f:
                break
            row +=1
            col = 0




def find_max(table_widget):

    row_max_number = 0
    col_max_number = 0
    max_num = float(table_widget.item(row_max_number, col_max_number).text())

    row = 0
    col = 0
    while row < table_widget.rowCount():
        while col < table_widget.columnCount():
            number = float(table_widget.item(row, col).text())
            if number > max_num:
                max_num = number
                row_max_number = row
                col_max_number = col
            col += 1
        row += 1
        col = 0


    return [max_num, row_max_number, col_max_number]
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
