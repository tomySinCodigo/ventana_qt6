# Form implementation generated from reading ui file 'skin.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Skin(object):
    def setupUi(self, Skin):
        Skin.setObjectName("Skin")
        Skin.resize(592, 438)
        Skin.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(parent=Skin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.vly_principal = QtWidgets.QVBoxLayout()
        self.vly_principal.setSpacing(0)
        self.vly_principal.setObjectName("vly_principal")
        self.fm_barra = QtWidgets.QFrame(parent=self.centralwidget)
        self.fm_barra.setMaximumSize(QtCore.QSize(16777215, 18))
        self.fm_barra.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fm_barra.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fm_barra.setObjectName("fm_barra")
        self.vly_barra = QtWidgets.QVBoxLayout(self.fm_barra)
        self.vly_barra.setContentsMargins(0, 0, 0, 0)
        self.vly_barra.setSpacing(0)
        self.vly_barra.setObjectName("vly_barra")
        self.hly_barra = QtWidgets.QHBoxLayout()
        self.hly_barra.setSpacing(2)
        self.hly_barra.setObjectName("hly_barra")
        self.bt_menu = QtWidgets.QPushButton(parent=self.fm_barra)
        self.bt_menu.setMinimumSize(QtCore.QSize(20, 18))
        self.bt_menu.setMaximumSize(QtCore.QSize(20, 18))
        self.bt_menu.setText("")
        self.bt_menu.setCheckable(True)
        self.bt_menu.setObjectName("bt_menu")
        self.hly_barra.addWidget(self.bt_menu)
        self.lb_titulo = QtWidgets.QLabel(parent=self.fm_barra)
        self.lb_titulo.setMinimumSize(QtCore.QSize(0, 18))
        self.lb_titulo.setMaximumSize(QtCore.QSize(16777215, 18))
        self.lb_titulo.setText("")
        self.lb_titulo.setObjectName("lb_titulo")
        self.hly_barra.addWidget(self.lb_titulo)
        self.fm_otros = QtWidgets.QFrame(parent=self.fm_barra)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fm_otros.sizePolicy().hasHeightForWidth())
        self.fm_otros.setSizePolicy(sizePolicy)
        self.fm_otros.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fm_otros.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fm_otros.setObjectName("fm_otros")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fm_otros)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hly_otros = QtWidgets.QHBoxLayout()
        self.hly_otros.setObjectName("hly_otros")
        self.horizontalLayout.addLayout(self.hly_otros)
        self.hly_barra.addWidget(self.fm_otros)
        self.fm_bts = QtWidgets.QFrame(parent=self.fm_barra)
        self.fm_bts.setMaximumSize(QtCore.QSize(110, 16777215))
        self.fm_bts.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fm_bts.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fm_bts.setObjectName("fm_bts")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.fm_bts)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.hly_bts = QtWidgets.QHBoxLayout()
        self.hly_bts.setSpacing(2)
        self.hly_bts.setObjectName("hly_bts")
        self.bt_o = QtWidgets.QPushButton(parent=self.fm_bts)
        self.bt_o.setMinimumSize(QtCore.QSize(20, 18))
        self.bt_o.setMaximumSize(QtCore.QSize(20, 18))
        self.bt_o.setText("")
        self.bt_o.setCheckable(True)
        self.bt_o.setObjectName("bt_o")
        self.hly_bts.addWidget(self.bt_o)
        self.bt_lock = QtWidgets.QPushButton(parent=self.fm_bts)
        self.bt_lock.setMinimumSize(QtCore.QSize(20, 18))
        self.bt_lock.setMaximumSize(QtCore.QSize(20, 18))
        self.bt_lock.setText("")
        self.bt_lock.setCheckable(True)
        self.bt_lock.setObjectName("bt_lock")
        self.hly_bts.addWidget(self.bt_lock)
        self.bt_min = QtWidgets.QPushButton(parent=self.fm_bts)
        self.bt_min.setMinimumSize(QtCore.QSize(20, 18))
        self.bt_min.setMaximumSize(QtCore.QSize(20, 18))
        self.bt_min.setText("")
        self.bt_min.setObjectName("bt_min")
        self.hly_bts.addWidget(self.bt_min)
        self.bt_fw = QtWidgets.QPushButton(parent=self.fm_bts)
        self.bt_fw.setMinimumSize(QtCore.QSize(20, 18))
        self.bt_fw.setMaximumSize(QtCore.QSize(20, 18))
        self.bt_fw.setText("")
        self.bt_fw.setCheckable(True)
        self.bt_fw.setObjectName("bt_fw")
        self.hly_bts.addWidget(self.bt_fw)
        self.bt_x = QtWidgets.QPushButton(parent=self.fm_bts)
        self.bt_x.setMinimumSize(QtCore.QSize(20, 18))
        self.bt_x.setMaximumSize(QtCore.QSize(20, 18))
        self.bt_x.setText("")
        self.bt_x.setObjectName("bt_x")
        self.hly_bts.addWidget(self.bt_x)
        self.horizontalLayout_4.addLayout(self.hly_bts)
        self.hly_barra.addWidget(self.fm_bts)
        self.hly_barra.setStretch(1, 4)
        self.hly_barra.setStretch(2, 1)
        self.vly_barra.addLayout(self.hly_barra)
        self.vly_principal.addWidget(self.fm_barra)
        self.fm_main = QtWidgets.QFrame(parent=self.centralwidget)
        self.fm_main.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fm_main.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fm_main.setObjectName("fm_main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fm_main)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.vly_main = QtWidgets.QVBoxLayout()
        self.vly_main.setObjectName("vly_main")
        self.verticalLayout_2.addLayout(self.vly_main)
        self.vly_principal.addWidget(self.fm_main)
        self.verticalLayout_4.addLayout(self.vly_principal)
        Skin.setCentralWidget(self.centralwidget)

        self.retranslateUi(Skin)
        QtCore.QMetaObject.connectSlotsByName(Skin)

    def retranslateUi(self, Skin):
        _translate = QtCore.QCoreApplication.translate
        Skin.setWindowTitle(_translate("Skin", "MainWindow"))
