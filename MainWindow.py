# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(878, 531)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txtHeroSearch = QLineEdit(self.centralwidget)
        self.txtHeroSearch.setObjectName(u"txtHeroSearch")

        self.horizontalLayout_2.addWidget(self.txtHeroSearch)

        self.btnCancelAllSelect = QPushButton(self.centralwidget)
        self.btnCancelAllSelect.setObjectName(u"btnCancelAllSelect")

        self.horizontalLayout_2.addWidget(self.btnCancelAllSelect)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lstHeros = QListWidget(self.centralwidget)
        self.lstHeros.setObjectName(u"lstHeros")

        self.verticalLayout.addWidget(self.lstHeros)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.tblHeros = QTableWidget(self.centralwidget)
        self.tblHeros.setObjectName(u"tblHeros")

        self.verticalLayout_2.addWidget(self.tblHeros)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.commandLinkButton = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.verticalLayout_3.addWidget(self.commandLinkButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 878, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.commandLinkButton.clicked.connect(MainWindow.linkMyShop)
        self.btnCancelAllSelect.clicked.connect(MainWindow.cancelAllSelected)
        self.txtHeroSearch.textChanged.connect(MainWindow.heroSearchChanged)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u82f1\u96c4\u8054\u76df\u4e4b\u82f1\u96c4\u7c7b\u578b\u8868-\u4e13\u4e1a\u8f6f\u4ef6\u5b9a\u5236\u5f00\u53d1 https://xinyiya.taobao.com/", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u82f1\u96c4", None))
        self.btnCancelAllSelect.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88\u5168\u9009", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u82f1\u96c4\u7c7b\u578b", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"\u946b\u610f\u96c5\u6dd8\u5b9d\u5e97: https://xinyiya.taobao.com/", None))
    # retranslateUi

