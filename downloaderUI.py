"""
MIT License

Copyright (c) 2017 Lohrii Alo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloaderUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(477, 543)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.url = QtGui.QLineEdit(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(10, 20, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.url.setFont(font)
        self.url.setText(_fromUtf8(""))
        self.url.setAlignment(QtCore.Qt.AlignCenter)
        self.url.setObjectName(_fromUtf8("url"))
        self.browse = QtGui.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(120, 100, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.browse.setFont(font)
        self.browse.setObjectName(_fromUtf8("browse"))
        self.save_location_label = QtGui.QLabel(self.centralwidget)
        self.save_location_label.setGeometry(QtCore.QRect(10, 190, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.save_location_label.setFont(font)
        self.save_location_label.setObjectName(_fromUtf8("save_location_label"))
        self.save_location = QtGui.QLabel(self.centralwidget)
        self.save_location.setGeometry(QtCore.QRect(90, 190, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.save_location.setFont(font)
        self.save_location.setText(_fromUtf8(""))
        self.save_location.setObjectName(_fromUtf8("save_location"))
        self.combobox = QtGui.QComboBox(self.centralwidget)
        self.combobox.setGeometry(QtCore.QRect(150, 270, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.combobox.setFont(font)
        self.combobox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.combobox.setObjectName(_fromUtf8("combobox"))
        self.combobox.addItem(_fromUtf8(""))
        self.combobox.addItem(_fromUtf8(""))
        self.combobox.addItem(_fromUtf8(""))
        self.combobox.addItem(_fromUtf8(""))
        self.combobox.addItem(_fromUtf8(""))
        self.combobox.addItem(_fromUtf8(""))
        self.combobox.addItem(_fromUtf8(""))
        self.combobox.addItem(_fromUtf8(""))
        self.combobox_label = QtGui.QLabel(self.centralwidget)
        self.combobox_label.setGeometry(QtCore.QRect(10, 270, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.combobox_label.setFont(font)
        self.combobox_label.setObjectName(_fromUtf8("combobox_label"))
        self.download = QtGui.QPushButton(self.centralwidget)
        self.download.setGeometry(QtCore.QRect(160, 380, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.download.setFont(font)
        self.download.setObjectName(_fromUtf8("download"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 477, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuToolss = QtGui.QMenu(self.menubar)
        self.menuToolss.setObjectName(_fromUtf8("menuToolss"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Download = QtGui.QAction(MainWindow)
        self.actionNew_Download.setObjectName(_fromUtf8("actionNew_Download"))
        self.actionEdit = QtGui.QAction(MainWindow)
        self.actionEdit.setObjectName(_fromUtf8("actionEdit"))
        self.actionSet_Video_Download_Preference = QtGui.QAction(MainWindow)
        self.actionSet_Video_Download_Preference.setObjectName(_fromUtf8("actionSet_Video_Download_Preference"))
        self.actionVideo_Downloader_Help = QtGui.QAction(MainWindow)
        self.actionVideo_Downloader_Help.setObjectName(_fromUtf8("actionVideo_Downloader_Help"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionNew_Download)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionEdit)
        self.menuToolss.addAction(self.actionSet_Video_Download_Preference)
        self.menuHelp.addAction(self.actionVideo_Downloader_Help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuToolss.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Video Downloader", None))
        self.url.setPlaceholderText(_translate("MainWindow", "Video or Playlist url", None))
        self.browse.setText(_translate("MainWindow", "Browse Download Location", None))
        self.save_location_label.setText(_translate("MainWindow", "Save To :", None))
        self.combobox.setItemText(0, _translate("MainWindow", "Best Quality Available", None))
        self.combobox.setItemText(1, _translate("MainWindow", "360p", None))
        self.combobox.setItemText(2, _translate("MainWindow", "480p", None))
        self.combobox.setItemText(3, _translate("MainWindow", "720p", None))
        self.combobox.setItemText(4, _translate("MainWindow", "1080p", None))
        self.combobox.setItemText(5, _translate("MainWindow", "2K", None))
        self.combobox.setItemText(6, _translate("MainWindow", "4K", None))
        self.combobox.setItemText(7, _translate("MainWindow", "8K", None))
        self.combobox_label.setText(_translate("MainWindow", "Video Quality :", None))
        self.download.setText(_translate("MainWindow", "Download", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuToolss.setTitle(_translate("MainWindow", "Preferences", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionNew_Download.setText(_translate("MainWindow", "New Download", None))
        self.actionNew_Download.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionEdit.setText(_translate("MainWindow", "Exit", None))
        self.actionSet_Video_Download_Preference.setText(_translate("MainWindow", "Set Video Download Preference", None))
        self.actionVideo_Downloader_Help.setText(_translate("MainWindow", "Video Downloader Help", None))
        self.actionVideo_Downloader_Help.setShortcut(_translate("MainWindow", "Ctrl+F5", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

