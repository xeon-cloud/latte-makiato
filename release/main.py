import io
import sys
import os

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt
import sqlite3

import UI.add_ui
import UI.main_ui

dbPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'coffee.sqlite')

class AddWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(io.StringIO(UI.add_ui.getUi()), self)
        self.pushButton.clicked.connect(self.act)

    def act(self):
        conn = sqlite3.connect(dbPath)
        cursor = conn.cursor()

        query = '''INSERT INTO table_for_coffee (class_name, step_objarki, ground_in_grains,
        taste_description, price, volume) VALUES (?, ?, ?, ?, ?, ?)'''
        values = (
            self.l1.text(), self.l2.text(), self.l3.text(),
            self.l4.text(), self.l5.text(), self.l6.text())
        cursor.execute(query, values)

        conn.commit()

        self.hide()
        self.mywidget = MyWidget()
        self.mywidget.show()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(io.StringIO(UI.main_ui.getUi()), self)

        connection = sqlite3.connect(dbPath)
        cursor = connection.cursor()

        query = '''SELECT * FROM table_for_coffee'''
        result = cursor.execute(query).fetchall()[::-1]

        self.table.setRowCount(len(result))
        self.table.setColumnCount(7)

        self.table.horizontalHeader().setStyleSheet(
            "QHeaderView::section { background-color: rgb(255, 170, 127);}")

        self.table.verticalHeader().setStyleSheet(
            "QHeaderView::section { background-color: rgb(255, 170, 127);}")

        header_labels = ['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах', 'Описание вкуса', 'Цена', 'Объём упаковки']
        self.table.setHorizontalHeaderLabels(header_labels)

        self.table.horizontalHeader().setStretchLastSection(True)

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                item = QTableWidgetItem(str(val))
                item.setBackground(QColor(85, 255, 255))
                self.table.setItem(i, j, item)
                if j == 0:
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)

        connection.close()

        self.table.itemChanged.connect(self.update_database)
        self.pushButton.clicked.connect(self.act)

    def act(self):
        self.hide()
        self.addwidget = AddWidget()
        self.addwidget.show()

    def update_database(self, item):
        row = item.row()
        column = item.column()
        value = item.text()

        connection = sqlite3.connect(dbPath)
        cursor = connection.cursor()
        if column == 1:
            cursor.execute("UPDATE table_for_coffee SET class_name = ? WHERE ID = ?",
                           (value, self.table.item(row, 0).text()))
        elif column == 2:
            cursor.execute("UPDATE table_for_coffee SET step_objarki = ? WHERE ID = ?",
                           (value, self.table.item(row, 0).text()))
        elif column == 3:
            cursor.execute("UPDATE table_for_coffee SET ground_in_grains = ? WHERE ID = ?",
                           (value, self.table.item(row, 0).text()))
        elif column == 4:
            cursor.execute("UPDATE table_for_coffee SET taste_description = ? WHERE ID = ?",
                           (value, self.table.item(row, 0).text()))
        elif column == 5:
            cursor.execute("UPDATE table_for_coffee SET price = ? WHERE ID = ?",
                           (value, self.table.item(row, 0).text()))
        else:
            cursor.execute("UPDATE table_for_coffee SET volume = ? WHERE ID = ?",
                           (value, self.table.item(row, 0).text()))
        connection.commit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
