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

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui

import sys
import os
import subprocess
from subprocess import PIPE, STDOUT

import downloaderUI

class MainUIClass(QtGui.QMainWindow, downloaderUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainUIClass, self).__init__(parent)
        self.setupUi(self)

        self.setFocus()
        self.statusBar().setSizeGripEnabled(False)
        self.setFixedSize(472, 552)

        # UI buttons clicked handler
        self.browse.clicked.connect(self.browse_file)
        self.download.clicked.connect(self.downloadvideo)

        # set UI related stuffs
        self.actionAbout.triggered.connect(self.about)
        self.actionEdit.setShortcut('Ctrl+Q')
        self.actionEdit.setStatusTip('Exit application')
        self.actionSet_Video_Download_Preference.setStatusTip("Set Video Download Preference")
        self.actionAbout.setStatusTip("About this application developer")
        self.actionEdit.triggered.connect(QtGui.qApp.quit)
        self.statusbar.showMessage("Status: ")

        # threading object
        self.workerThread = WorkerThread()

        # listen for signals
        self.connect(self.workerThread, SIGNAL("THREADING_SIGNAL"), self.myThreading)
        self.connect(self, SIGNAL("DOWNLOAD_COMPLETE"), self.downloadComplete)
        self.connect(self, SIGNAL("DOWNLOAD_ERROR"), self.downloadError)
        self.connect(self, SIGNAL("INVALID_PARAM"), self.invalidParam)

    def downloadComplete(self):
        self.statusbar.showMessage("Status: Download Completed")
        self.url.setText("")
        self.save_location.setText("")
        self.combobox.setCurrentIndex(0)
        QMessageBox.information(self, "Information", "Download Complete")

    def downloadError(self):
        self.statusbar.showMessage("Status: Download Failed")
        QMessageBox.information(self, "Information", "Download Failed")

    def invalidParam(self):
        self.statusbar.showMessage("Status: Invalid Video URL")
        QMessageBox.information(self, "Information", "Invalid Video URL")

    def browse_file(self):
        save_file = QFileDialog.getExistingDirectory()
        self.save_location.setText(QDir.toNativeSeparators(save_file))

    def about(self):
        QMessageBox.information(self, "Information", "Lohrii Alo \n\nhttps://github.com/lohriialo/YouTubeVideoDownloader")

    def downloadvideo(self):
        self.videoDownloadUrl = self.url.text()
        self.selectedVideoQuality = str(self.combobox.currentText())
        if self.save_location.text() == "":
            self.videoDownloadLocation = os.getcwd() + "/%(title)s.%(ext)s"
        else:
            self.videoDownloadLocation = self.save_location.text() + "/%(title)s.%(ext)s"
        self.workerThread.start()

    def processDownload(self, quality):
        try:
            p = subprocess.Popen(["youtube-dl",
                                  "-f" "%s" % quality,
                                  "-o" "%s" % self.videoDownloadLocation,  # hack to escape (:) path correctly
                                  "--ignore-errors",
                                  self.videoDownloadUrl], shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
            for line in p.stdout:
                print(str(line.rstrip()))
                p.stdout.flush()
                QtGui.qApp.processEvents()
                self.statusbar.showMessage(str(line.rstrip()))
            self.emit(SIGNAL("DOWNLOAD_COMPLETE"))

        except Exception:
            self.emit(SIGNAL("DOWNLOAD_ERROR"))
            return

    def myThreading(self):
        if self.selectedVideoQuality == "360p" and self.videoDownloadUrl != "":
            quality = "bestvideo[ext=mp4, height=360]+bestaudio[ext=m4a]/best[ext=mp4, height=360]/best"
            self.processDownload(quality)

        if self.selectedVideoQuality == "480p" and self.videoDownloadUrl != "":
            quality = "bestvideo[ext=mp4, height=480]+bestaudio[ext=m4a]/best[ext=mp4, height=480]/best"
            self.processDownload(quality)

        if self.selectedVideoQuality == "720p" and self.videoDownloadUrl != "":
            quality = "bestvideo[ext=mp4, height=720]+bestaudio[ext=m4a]/best[ext=mp4, height=720]/best"
            self.processDownload(quality)

        if self.selectedVideoQuality == "1080p" and self.videoDownloadUrl != "":
            quality = "bestvideo[ext=mp4, height=1080]+bestaudio[ext=m4a]/best[ext=mp4, height=1080]/best"
            self.processDownload(quality)

        if self.selectedVideoQuality == "2K" and self.videoDownloadUrl != "":
            quality = "bestvideo[ext=mp4, height=1440]+bestaudio[ext=m4a]/best[ext=mp4, height=1440]/best"
            self.processDownload(quality)

        if self.selectedVideoQuality == "4K" and self.videoDownloadUrl != "":
            quality = "bestvideo[ext=mp4, height=2160]+bestaudio[ext=m4a]/best[ext=mp4, height=2160]/best"
            self.processDownload(quality)

        if self.selectedVideoQuality == "8K" and self.videoDownloadUrl != "":
            quality = "bestvideo[ext=mp4, height=4320]+bestaudio[ext=m4a]/best[ext=mp4, height=4320]/best"
            self.processDownload(quality)

        if self.selectedVideoQuality == "Best Quality Available" and self.videoDownloadUrl != "":
            quality = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
            self.processDownload(quality)

    # prompt before application exit, overidding the default closeEvent()
    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class WorkerThread(QThread):
    def __init__(self, parent=None):
        super(WorkerThread, self).__init__(parent)

    def run(self):
        self.emit(SIGNAL("THREADING_SIGNAL"))

if __name__ == '__main__':
    a = QtGui.QApplication(sys.argv)
    app = MainUIClass()
    app.show()
    a.exec_()
