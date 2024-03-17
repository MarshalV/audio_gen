from PyQt5.QtGui import QCursor

import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (QApplication,
                              QLabel, QMenu )
from PyQt5.QtCore import (Qt)


class MyLabel(QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, pos):
        menu = QMenu(self)
        copy_action = menu.addAction("Копировать")
        copy_action.triggered.connect(self.copy_text)
        menu.exec_(QCursor.pos())

    def copy_text(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.text())
