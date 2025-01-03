import sys
from ventana_q6.mi_ventana_q import MiVentanaQ
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.ApplicationAttribute.AA_Use96Dpi)
    app.setStyle("Fusion")
    vn = MiVentanaQ()
    vn.asignaTitulo("PROGRAMA")
    vn.agregaTag("AUDIO", bg='red')
    vn.agregaTag("VIDEO", bg='green')
    # vn.fm_barra.setFixedHeight(16)

    vn.show()
    sys.exit(app.exec())