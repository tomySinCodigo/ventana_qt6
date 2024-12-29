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
        # self.te_editor.setStyleSheet("background-color:#303026;")
        self.d = {
            'mg':4,
            "pos":{
                "lateral":{
                    "i": {
                        "o": 0,
                        "n": 4,
                        "w": 2,
                        "bt": 30,
                        "add": 100
                    },
                    "d": {
                        "e": 0,
                        "n": 4,
                        "w": 2,
                        "bt": 30,
                        "add": 100
                    }
                }
            }
        }
        menu = {
            "&Restaura":self.restauraNormal,
            "Salir":self.close
        }
        self._conMenu(menu)
        self.vpos = None
        self._agregaGrips()
        self.fijar()
        self.bt_x.clicked.connect(self.cerrar)
        self.bt_fw.clicked.connect(self.maximizaRestaura)
        self.bt_min.clicked.connect(self.showMinimized)
        self.bt_lock.clicked.connect(self.fijar)
        self.bt_o.clicked.connect(self.alineaLateral)
        self.TAGS = []

    def aplica_estilo(self):
        with open("ventana_q6/estilo.css", "r", encoding="utf-8") as txt:
            QApplication.instance().setStyleSheet(txt.read())

    def onTop(self, b:bool):
        self.bt_lock.setChecked(b)

    def _conMenu(self, d:dict):
        self.menu_wg = QMenu(self)
        for nom, metodo in d.items():
            self.menu_wg.addAction(nom, metodo)
        self.bt_menu.setMenu(self.menu_wg)

    def cerrar(self):
        self.close()

    def maximizaRestaura(self):
        if self.isMaximized():
            self.showNormal()
            top = 0
        else:
            self.showMaximized()
            top = self.d.get('mg')
        self.setContentsMargins(0, top, 0, 0)

    def fijar(self):
        b = self.bt_lock.isChecked()
        std = Qt.WindowType.WindowStaysOnTopHint if b else Qt.WindowType.Window
        self.setWindowFlags(std | Qt.WindowType.FramelessWindowHint)
        self.showNormal()

    def getsize(self):
        screen = QApplication.primaryScreen()
        return screen.size()

    def restauraNormal(self):
        sz = self.getsize()
        w, h = 600, 250
        x = sz.width()//2-w//2
        y = sz.height()//2-h//2
        self.setGeometry(x, y, w, h)
        self.bt_o.setChecked(False)

    def _alineaIzquierda(self):
        gm = self.getsize()
        pos = self.d['pos']['lateral']['i']
        add = pos['add']
        h = gm.height() + pos['bt']
        w = gm.width() // pos['w'] + add
        self.setGeometry(pos['o'], pos['n'], w, h)

    def _alineaDerecha(self):
        gm = self.getsize()
        pos = self.d['pos']['lateral']['d']
        add = pos['add']
        h = gm.height() - pos['bt']
        w = gm.width() // pos['w']
        self.setGeometry(w-add, pos['n'], w+add, h)

    def alineaLateral(self):
        b = self.bt_o.isChecked()
        self._alineaIzquierda() if b else self._alineaDerecha()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

    def _agregaGrips(self):
        self._GRIPS = []
        self.grip_tam = 8
        for i in range(2):
            grip = QSizeGrip(self)
            grip.resize(self.grip_tam, self.grip_tam)
            self._GRIPS.append(grip)

    def resizeEvent(self, e):
        QWidget.resizeEvent(self, e)
        rect = self.rect()
        # top derecha
        # self._GRIPS[1].move(rect.right()-self.grip_tam, 0)
        # bot derecha
        self._GRIPS[0].move(rect.right() - self.grip_tam, rect.bottom() - self.grip_tam)
        # bot izquierda
        self._GRIPS[1].move(0, rect.bottom() - self.grip_tam)

    # para mover la ventana
    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.vpos = e.pos()
            
    def mouseReleaseEvent(self, e):
        self.vpos = None
        
    def mouseMoveEvent(self, e):
        if self.isMaximized():
            return
        if e.buttons() == Qt.MouseButton.LeftButton and self.vpos:
            pos = e.pos() - self.vpos
            self.move(self.pos() + pos)
    # para mover la ventana
    def asignaTitulo(self, texto:str):
        self.lb_titulo.setText(texto)

    # def mitag(self, texto):
    #     txt = f'<html><head/><body><p align="right"><span style=" font-size:7pt; font-weight:700; color:#ffffff; background-color:#0000ff;"> {texto} </span></p></body></html>'
    #     self.te_editor.setHtml(txt)

    def agregaTag(self, texto, bg:str='orange', fg:str='white'):
        lb = QLabel(self)
        lb.setText(texto)
        s = 'font-size:7pt;'\
        'font-weight:700;'\
        f'color:{fg};'\
        f'background-color:{bg};'

        lb.setStyleSheet(s)
        lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lb.setMargin(4)
        lb.setFixedHeight(16)
        self.TAGS.append(lb)
        self.hly_otros.addWidget(lb)