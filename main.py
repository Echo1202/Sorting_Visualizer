from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import QTimer, Qt
from threading import *
import sys, time, random

# Main GUI
class Ui_MainWindow(object):

    def UI_setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1182, 501)
        self.barNum = 20
        self.randList = []
        self.sleepTime = 0.01
        # empty list that will contain all bar widget
        self.barWidgets = []
        print(len(self.randList))
        # centralWidget will contain size of 1010
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.slider = QtWidgets.QSlider(self.centralWidget)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setGeometry(QtCore.QRect(1050, 340, 121, 10))
        self.slider.setMaximum(100)
        self.slider.setMinimum(2)
        self.slider.setValue(self.barNum)
        self.slider.valueChanged.connect(self.changedVal)

        self.sliderVal = QtWidgets.QLabel(self.centralWidget)
        self.sliderVal.resize(200, 20)
        self.sliderVal.move(1050, 350)
        self.sliderVal.setText("Number of values: {}".format(self.barNum))

        # create 20 bars that will initially populate the application / central widget
        self.addBars(0, self.barNum)

        # create frame that will contain sorting buttons
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 1021, 461))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setObjectName("buttom_frame")
        
        # create buttons inside frame made above
        self.button1 = QtWidgets.QPushButton(self.centralWidget)
        self.button1.setGeometry(QtCore.QRect(1050, 160, 121, 30))
        self.button1.setText("Bubble Sort")
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.bubble_sort)

        self.button2 = QtWidgets.QPushButton(self.centralWidget)
        self.button2.setGeometry(QtCore.QRect(1050, 190, 121, 30))
        self.button2.setText("Insertion Sort")
        self.button2.setObjectName("button2")
        self.button2.clicked.connect(self.insertion_sort)

        self.button3 = QtWidgets.QPushButton(self.centralWidget)
        self.button3.setGeometry(QtCore.QRect(1050, 220, 121, 30))
        self.button3.setText("Selection Sort")
        self.button3.setObjectName("button3")
        self.button3.clicked.connect(self.selection_sort)

        self.button4 = QtWidgets.QPushButton(self.centralWidget)
        self.button4.setGeometry(QtCore.QRect(1050, 250, 121, 30))
        self.button4.setText("Merge Sort")
        self.button4.setObjectName("button4")
        self.button4.clicked.connect(self.merge_sort_helper)

        self.button5 = QtWidgets.QPushButton(self.centralWidget)
        self.button5.setGeometry(QtCore.QRect(1050, 280, 121, 30))
        self.button5.setText("Quick Sort")
        self.button5.setObjectName("button5")
        self.button5.clicked.connect(self.quick_sort_helper)

        self.frame.raise_()
        self.button1.raise_()
        self.button2.raise_()
        self.button3.raise_()
        self.button4.raise_()

        MainWindow.setCentralWidget(self.centralWidget)
        self.menu = QtWidgets.QMenuBar(MainWindow)
        self.menu.setGeometry(QtCore.QRect(0, 0, 1182, 21))
        self.menu.setObjectName("menu")

        MainWindow.setMenuBar(self.menu)
        self.status = QtWidgets.QStatusBar(MainWindow)
        self.status.setObjectName("status")
        MainWindow.setStatusBar(self.status)

# add progress bar widgets to the central widget to reflect the number indicated by the slider
    def addBars(self, min, numAdd):
        for i in range(numAdd):
            self.randList.append(random.randint(1, self.slider.value()))
            bar = QtWidgets.QProgressBar(self.centralWidget)
            bar.setGeometry(QtCore.QRect((20 + (10 * (i + min))), 30, 11, 441))
            bar.setStyleSheet("QProgressBar {\n"
                                 "   background-color : rgba(0,0,0,0);\n"
                                 "   border : 1px;\n"
                                 "}\n"
                                 "\n"
                                 "QProgressBar::chunk {\n"
                                 "   \n"
                                 "   \n"
                                 "   background-color: rgb(85, 255, 0);\n"
                                 "   border: 1px solid black;\n"
                                 "}")
            bar.setProperty("value", self.randList[-1])
            bar.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignJustify)
            bar.setTextVisible(False)
            bar.setOrientation(QtCore.Qt.Vertical)
            bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
            bar.setObjectName("bar")
            bar.raise_()
            self.barWidgets.append(bar)
            bar.show()
            print(self.barWidgets[i].value())
        self.barNum = self.slider.value()

# remove progress bar widgets from the central widget to reflect the number indicated by the slider
    def removeBars(self):
        del self.randList[-1]
        self.barWidgets[-1].hide()
        del self.barWidgets[-1]
        print(len(self.randList), len(self.barWidgets))
        self.barNum = self.slider.value()

# create a psuedo random array of values
    def randomGen(self, max, add, remove):
        for i in range(add):
            self.randList.append(random.randint(1, max))
        for i in range(remove):
            self.randList.pop()

# changes display to reflect the number data points being set by the slider
    def changedVal(self):
        if self.barNum < self.slider.value():
            self.addBars(self.barNum, self.slider.value() - self.barNum)
        elif self.barNum >= self.slider.value():
            self.removeBars()
        self.sliderVal.setText("Number of values: {}".format(self.barNum))

# algorithms
    # bubble sort
    def bubble_sort(self):
        for i in range(self.slider.value() - 1):
            for j in range(0, self.slider.value() - i - 1):
                if self.barWidgets[j].value() > self.barWidgets[j + 1].value():
                    # set time delay before eash swap
                    time.sleep(self.sleepTime)
                    # print(self.randList[j], self.barWidgets[j].value())
                    self.barWidgets[j].setStyleSheet("QProgressBar {\n"
                                                     "   background-color : rgba(0,0,0,0);\n"
                                                     "   border : 1px;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QProgressBar::chunk {\n"
                                                     "   \n"
                                                     "   \n"
                                                     "   background-color: red;\n"
                                                     "   border: 1px solid black;\n"
                                                     "}")
                    self.barWidgets[j+1].setStyleSheet("QProgressBar {\n"
                                                       "   background-color : rgba(0,0,0,0);\n"
                                                       "   border : 1px;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QProgressBar::chunk {\n"
                                                       "   \n"
                                                       "   \n"
                                                       "   background-color: red;\n"
                                                       "   border: 1px solid black;\n"
                                                       "}")
                    self.barWidgets[j].setValue(self.randList[j+1])
                    self.barWidgets[j+1].setValue(self.randList[j])
                    self.randList[j], self.randList[j+1] = self.randList[j+1], self.randList[j]
                    self.barWidgets[j].setStyleSheet("QProgressBar {\n"
                                                     "   background-color : rgba(0,0,0,0);\n"
                                                     "   border : 1px;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QProgressBar::chunk {\n"
                                                     "   \n"
                                                     "   \n"
                                                     "   background-color: rgb(85, 255, 0);\n"
                                                     "   border: 1px solid black;\n"
                                                     "}")
                    self.barWidgets[j+1].setStyleSheet("QProgressBar {\n"
                                                       "   background-color : rgba(0,0,0,0);\n"
                                                       "   border : 1px;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QProgressBar::chunk {\n"
                                                       "   \n"
                                                       "   \n"
                                                       "   background-color: rgb(85, 255, 0);\n"
                                                       "   border: 1px solid black;\n"
                                                       "}")

    # insertion sort
    def insertion_sort(self):
        for i in range(1, self.barNum):
            key = self.randList[i]
            j = i - 1
            while j >= 0 and key < self.randList[j]:
                time.sleep(self.sleepTime)
                self.barWidgets[j].setStyleSheet("QProgressBar {\n"
                                                   "   background-color : rgba(0,0,0,0);\n"
                                                   "   border : 1px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QProgressBar::chunk {\n"
                                                   "   \n"
                                                   "   \n"
                                                   "   background-color: red;\n"
                                                   "   border: 1px solid black;\n"
                                                   "}")
                self.barWidgets[j+1].setStyleSheet("QProgressBar {\n"
                                                   "   background-color : rgba(0,0,0,0);\n"
                                                   "   border : 1px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QProgressBar::chunk {\n"
                                                   "   \n"
                                                   "   \n"
                                                   "   background-color: red;\n"
                                                   "   border: 1px solid black;\n"
                                                   "}")
                self.randList[j+1] = self.randList[j]
                self.barWidgets[j+1].setValue(self.randList[j])
                self.barWidgets[j].setStyleSheet("QProgressBar {\n"
                                                   "   background-color : rgba(0,0,0,0);\n"
                                                   "   border : 1px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QProgressBar::chunk {\n"
                                                   "   \n"
                                                   "   \n"
                                                   "   background-color: rgb(85, 255, 0);\n"
                                                   "   border: 1px solid black;\n"
                                                   "}")
                self.barWidgets[j+1].setStyleSheet("QProgressBar {\n"
                                                   "   background-color : rgba(0,0,0,0);\n"
                                                   "   border : 1px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QProgressBar::chunk {\n"
                                                   "   \n"
                                                   "   \n"
                                                   "   background-color: rgb(85, 255, 0);\n"
                                                   "   border: 1px solid black;\n"
                                                   "}")
                j -= 1
            self.randList[j+1] = key
            self.barWidgets[j+1].setValue(key)
        self.centralWidget.update()

    # selection sort
    def selection_sort(self):
        min_index = 0
        for i in range(self.barNum):
            min_index = i
            for j in range(i+1, self.barNum):
                if self.randList[min_index] > self.randList[j]:
                    self.barWidgets[min_index].setStyleSheet("QProgressBar {\n"
                                                     "   background-color : rgba(0,0,0,0);\n"
                                                     "   border : 1px;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QProgressBar::chunk {\n"
                                                     "   \n"
                                                     "   \n"
                                                     "   background-color: red;\n"
                                                     "   border: 1px solid black;\n"
                                                     "}")
                    self.barWidgets[j].setStyleSheet("QProgressBar {\n"
                                                     "   background-color : rgba(0,0,0,0);\n"
                                                     "   border : 1px;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QProgressBar::chunk {\n"
                                                     "   \n"
                                                     "   \n"
                                                     "   background-color: red;\n"
                                                     "   border: 1px solid black;\n"
                                                     "}")
                    temp = min_index
                    min_index = j
                    self.barWidgets[min_index].setStyleSheet("QProgressBar {\n"
                                                             "   background-color : rgba(0,0,0,0);\n"
                                                             "   border : 1px;\n"
                                                             "}\n"
                                                             "\n"
                                                             "QProgressBar::chunk {\n"
                                                             "   \n"
                                                             "   \n"
                                                             "   background-color: rgb(85, 255, 0);\n"
                                                             "   border: 1px solid black;\n"
                                                             "}")
                    self.barWidgets[temp].setStyleSheet("QProgressBar {\n"
                                                        "   background-color : rgba(0,0,0,0);\n"
                                                        "   border : 1px;\n"
                                                        "}\n"
                                                        "\n"
                                                        "QProgressBar::chunk {\n"
                                                        "   \n"
                                                        "   \n"
                                                        "   background-color: rgb(85, 255, 0);\n"
                                                        "   border: 1px solid black;\n"
                                                        "}")

            self.barWidgets[i].setValue(self.randList[min_index])
            self.barWidgets[min_index].setValue(self.randList[i])
            self.randList[i], self.randList[min_index] = self.randList[min_index], self.randList[i]
            time.sleep(self.sleepTime)
        self.centralWidget.update()

    # merge sort helper
    def merge_sort_helper(self):
        self.merge_sort(self.randList)
        self.centralWidget.update()

    # merge sort
    def merge_sort(self, arr):
        if len(arr) > 1:
            middle = len(arr) // 2
            left = arr[:middle]
            right = arr[middle:]
            self.merge_sort(left)
            self.merge_sort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    time.sleep(self.sleepTime)
                    self.barWidgets[k].setValue(left[i])
                    self.barWidgets[k].setStyleSheet("QProgressBar {\n"
                                      "   background-color : rgba(0,0,0,0);\n"
                                      "   border : 1px;\n"
                                      "}\n"
                                      "\n"
                                      "QProgressBar::chunk {\n"
                                      "   \n"
                                      "   \n"
                                      "   background-color: rgb(85, 255, 0);\n"
                                      "   border: 1px solid black;\n"
                                      "}")
                    arr[k] = left[i]
                    i += 1
                else:
                    time.sleep(self.sleepTime)
                    self.barWidgets[k].setValue(right[j])
                    self.barWidgets[k].setStyleSheet("QProgressBar {\n"
                                                     "   background-color : rgba(0,0,0,0);\n"
                                                     "   border : 1px;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QProgressBar::chunk {\n"
                                                     "   \n"
                                                     "   \n"
                                                     "   background-color: rgb(85, 255, 0);\n"
                                                     "   border: 1px solid black;\n"
                                                     "}")
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                time.sleep(self.sleepTime)
                self.barWidgets[k].setValue(left[i])
                self.barWidgets[k].setStyleSheet("QProgressBar {\n"
                                                 "   background-color : rgba(0,0,0,0);\n"
                                                 "   border : 1px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QProgressBar::chunk {\n"
                                                 "   \n"
                                                 "   \n"
                                                 "   background-color: rgb(85, 255, 0);\n"
                                                 "   border: 1px solid black;\n"
                                                 "}")
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                time.sleep(self.sleepTime)
                self.barWidgets[k].setValue(right[j])
                self.barWidgets[k].setStyleSheet("QProgressBar {\n"
                                                 "   background-color : rgba(0,0,0,0);\n"
                                                 "   border : 1px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QProgressBar::chunk {\n"
                                                 "   \n"
                                                 "   \n"
                                                 "   background-color: rgb(85, 255, 0);\n"
                                                 "   border: 1px solid black;\n"
                                                 "}")
                arr[k] = right[j]
                j += 1
                k += 1

    # quick sort helper
    def quick_sort_helper(self):
        max = self.barNum - 1
        self.quick_sort(0, max)
        self.centralWidget.update()

    # partition method for quick sort
    def partition(self, min, max):
        i = min - 1
        pivot = self.randList[max]

        for j in range(min, max):
            if self.randList[j] <= pivot:
                i = i + 1
                time.sleep(self.sleepTime)
                self.barWidgets[j].setStyleSheet("QProgressBar {\n"
                                                   "   background-color : rgba(0,0,0,0);\n"
                                                   "   border : 1px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QProgressBar::chunk {\n"
                                                   "   \n"
                                                   "   \n"
                                                   "   background-color: red;\n"
                                                   "   border: 1px solid black;\n"
                                                   "}")
                self.barWidgets[i].setStyleSheet("QProgressBar {\n"
                                                   "   background-color : rgba(0,0,0,0);\n"
                                                   "   border : 1px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QProgressBar::chunk {\n"
                                                   "   \n"
                                                   "   \n"
                                                   "   background-color: red;\n"
                                                   "   border: 1px solid black;\n"
                                                   "}")
                self.barWidgets[i].setValue(self.randList[j])
                self.barWidgets[j].setValue(self.randList[i])
                self.barWidgets[j].setStyleSheet("QProgressBar {\n"
                                                 "   background-color : rgba(0,0,0,0);\n"
                                                 "   border : 1px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QProgressBar::chunk {\n"
                                                 "   \n"
                                                 "   \n"
                                                 "   background-color: rgb(85, 255, 0);\n"
                                                 "   border: 1px solid black;\n"
                                                 "}")
                self.barWidgets[i].setStyleSheet("QProgressBar {\n"
                                                 "   background-color : rgba(0,0,0,0);\n"
                                                 "   border : 1px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QProgressBar::chunk {\n"
                                                 "   \n"
                                                 "   \n"
                                                 "   background-color: rgb(85, 255, 0);\n"
                                                 "   border: 1px solid black;\n"
                                                 "}")
                self.randList[i], self.randList[j] = self.randList[j], self.randList[i]

        time.sleep(self.sleepTime)
        self.barWidgets[i+1].setValue(self.randList[max])
        self.barWidgets[max].setValue(self.randList[i+1])
        self.randList[i+1], self.randList[max] = self.randList[max], self.randList[i+1]
        return i+1

    # quick sort
    def quick_sort(self, min, max):
        if min < max:
            index = self.partition(min, max)
            self.quick_sort(min, index - 1)
            self.quick_sort(index + 1, max)

# main code
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.UI_setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


