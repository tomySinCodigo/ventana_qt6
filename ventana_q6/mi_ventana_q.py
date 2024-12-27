from PyQt6.QtWidgets import (QWidget, QPushButton, QLabel, QFrame,
QMenu, QSizeGrip, QApplication, QVBoxLayout, QMainWindow)
from PyQt6.QtGui import QIcon, QPixmap, QMouseEvent, QGuiApplication
from PyQt6.QtCore import Qt, QSize, QByteArray, QPoint
from ventana_q6.skin import Ui_Skin

class MiVentanaQ(QMainWindow, Ui_Skin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._configs_MiVentanaQ()

    def _configs_MiVentanaQ(self):
        self.aplica_estilo()
        self.te_editor.setStyleSheet("background-color:#303026;")

    def aplica_estilo(self):
        with open("ventana_q6/estilo.css", "r", encoding="utf-8") as txt:
            QApplication.instance().setStyleSheet(txt.read())