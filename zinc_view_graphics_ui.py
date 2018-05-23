# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zinc_view_graphics.ui'
#
# Created: Thu Oct 22 13:25:38 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ZincViewGraphics(object):
    def setupUi(self, ZincViewGraphics):
        ZincViewGraphics.setObjectName("ZincViewGraphics")
        ZincViewGraphics.resize(800, 600)
        self.centralwidget = QtGui.QWidget(ZincViewGraphics)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sceneviewerWidget = SceneviewerWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sceneviewerWidget.sizePolicy().hasHeightForWidth())
        self.sceneviewerWidget.setSizePolicy(sizePolicy)
        self.sceneviewerWidget.setObjectName("sceneviewerWidget")
        self.verticalLayout_3.addWidget(self.sceneviewerWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.viewAllButton = QtGui.QPushButton(self.centralwidget)
        self.viewAllButton.setObjectName("viewAllButton")
        self.horizontalLayout.addWidget(self.viewAllButton)
        self.customButton = QtGui.QPushButton(self.centralwidget)
        self.customButton.setObjectName("customButton")
        self.horizontalLayout.addWidget(self.customButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        ZincViewGraphics.setCentralWidget(self.centralwidget)

        self.retranslateUi(ZincViewGraphics)
        QtCore.QMetaObject.connectSlotsByName(ZincViewGraphics)

    def retranslateUi(self, ZincViewGraphics):
        ZincViewGraphics.setWindowTitle(QtGui.QApplication.translate("ZincViewGraphics", "Zinc View Graphics", None, QtGui.QApplication.UnicodeUTF8))
        self.viewAllButton.setText(QtGui.QApplication.translate("ZincViewGraphics", "View All", None, QtGui.QApplication.UnicodeUTF8))
        self.customButton.setText(QtGui.QApplication.translate("ZincViewGraphics", "Custom", None, QtGui.QApplication.UnicodeUTF8))

from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget
