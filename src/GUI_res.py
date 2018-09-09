# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'des_GUI.ui'
#
# Created: Thu Aug 09 22:38:49 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Main_Widget(object):
    def setupUi(self, Main_Widget):
        Main_Widget.setObjectName(_fromUtf8("Main_Widget"))
        Main_Widget.resize(380, 410)
        Main_Widget.setMinimumSize(QtCore.QSize(380, 410))
        Main_Widget.setWindowOpacity(1.0)
        Main_Widget.setStyleSheet(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(Main_Widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pb_Random = QtGui.QPushButton(Main_Widget)
        self.pb_Random.setObjectName(_fromUtf8("pb_Random"))
        self.gridLayout.addWidget(self.pb_Random, 0, 4, 1, 1)
        self.pb_Next = QtGui.QPushButton(Main_Widget)
        self.pb_Next.setObjectName(_fromUtf8("pb_Next"))
        self.gridLayout.addWidget(self.pb_Next, 0, 3, 1, 1)
        self.pb_Stop = QtGui.QPushButton(Main_Widget)
        self.pb_Stop.setObjectName(_fromUtf8("pb_Stop"))
        self.gridLayout.addWidget(self.pb_Stop, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Main_Widget)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setLineWidth(0)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.hs_interv = QtGui.QSlider(Main_Widget)
        self.hs_interv.setMinimum(10)
        self.hs_interv.setMaximum(2500)
        self.hs_interv.setProperty("value", 500)
        self.hs_interv.setOrientation(QtCore.Qt.Horizontal)
        self.hs_interv.setObjectName(_fromUtf8("hs_interv"))
        self.gridLayout.addWidget(self.hs_interv, 1, 1, 1, 6)
        self.pb_Start = QtGui.QPushButton(Main_Widget)
        self.pb_Start.setObjectName(_fromUtf8("pb_Start"))
        self.gridLayout.addWidget(self.pb_Start, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(Main_Widget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.sb_y = QtGui.QSpinBox(Main_Widget)
        self.sb_y.setMinimum(1)
        self.sb_y.setMaximum(1000)
        self.sb_y.setProperty("value", 5)
        self.sb_y.setObjectName(_fromUtf8("sb_y"))
        self.horizontalLayout_2.addWidget(self.sb_y)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 6, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(Main_Widget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.sb_x = QtGui.QSpinBox(Main_Widget)
        self.sb_x.setMinimum(1)
        self.sb_x.setMaximum(1000)
        self.sb_x.setProperty("value", 5)
        self.sb_x.setObjectName(_fromUtf8("sb_x"))
        self.horizontalLayout.addWidget(self.sb_x)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 5, 1, 1)
        self.label = QtGui.QLabel(Main_Widget)
        self.label.setMinimumSize(QtCore.QSize(362, 333))
        self.label.setMouseTracking(False)
        self.label.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 7)

        self.retranslateUi(Main_Widget)
        QtCore.QMetaObject.connectSlotsByName(Main_Widget)

    def retranslateUi(self, Main_Widget):
        Main_Widget.setWindowTitle(_translate("Main_Widget", "Game of Life", None))
        self.pb_Random.setText(_translate("Main_Widget", "Random", None))
        self.pb_Next.setText(_translate("Main_Widget", "Next", None))
        self.pb_Stop.setText(_translate("Main_Widget", "Stop", None))
        self.label_4.setText(_translate("Main_Widget", "Interval:", None))
        self.pb_Start.setText(_translate("Main_Widget", "Start", None))
        self.label_3.setText(_translate("Main_Widget", "y:", None))
        self.label_2.setText(_translate("Main_Widget", "x:", None))
        self.label.setText(_translate("Main_Widget", "TextLabel", None))

