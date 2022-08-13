#This python project was made by Souptik Sinha ENG19CS0318,Tanmayee Sharma, Sohan Somya


from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QAction
from pygame import mixer
from tkinter import filedialog
mixer.init()
mixer.music.load('song1.mp3')
mixer.music.play()
mixer.music.pause()
mixer.music.unpause()
mixer.music.stop()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Music Player")
        MainWindow.resize(792, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-90, 570, 851, 601))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, -20, 791, 641))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("fashionmeetsmusic.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 240, 111, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 280, 93, 28))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 280, 93, 28))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_4.setAutoFillBackground(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 280, 93, 28))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_3.setAutoFillBackground(True)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp_About = QtWidgets.QAction(MainWindow)
        self.actionHelp_About.setObjectName("actionHelp_About")
        self.menuMenu.addAction(self.actionExit)
        self.menuMenu.addAction(self.actionHelp_About)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.music_file = False
        self.playing_state = False
        self.pushButton.clicked.connect(self.load)
        self.pushButton_2.clicked.connect(self.pause)
        self.pushButton_4.clicked.connect(self.stop)
        self.pushButton_3.clicked.connect(self.play)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Music Player", "Music Player"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "LOAD MUSIC"))
        self.pushButton_2.setText(_translate("MainWindow", "PAUSE"))
        self.pushButton_4.setText(_translate("MainWindow", "STOP"))
        self.pushButton_3.setText(_translate("MainWindow", "PLAY"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu "))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut('Alt+F4')
        self.actionExit.setStatusTip('Exit application')
        self.actionExit.triggered.connect(self.stop)
        self.actionHelp_About.setText(_translate("MainWindow", "Help/About"))





    # asks the user to open the file he wants
    def load(self):
        self.music_file = filedialog.askopenfile()

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        if self.playing_state:
            mixer.music.pause()
            self.playing_state = False
        else:
            mixer.music.unpause()
            self.playing_state = True

    def stop(self):
        mixer.music.stop()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
