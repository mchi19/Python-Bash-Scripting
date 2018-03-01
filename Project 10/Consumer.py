#! /bin/usr/env python3.4

import sys
import re
from PySide.QtGui import *
from BasicUI import *


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.componentNameList = [self.txtComponentName_1, self.txtComponentName_2, self.txtComponentName_3, self.txtComponentName_4, self.txtComponentName_5,
                                  self.txtComponentName_6, self.txtComponentName_7, self.txtComponentName_8, self.txtComponentName_9, self.txtComponentName_10,
                                  self.txtComponentName_11, self.txtComponentName_12, self.txtComponentName_13, self.txtComponentName_14, self.txtComponentName_15,
                                  self.txtComponentName_16, self.txtComponentName_17, self.txtComponentName_18, self.txtComponentName_19, self.txtComponentName_20]
        self.componentCountList = [self.txtComponentCount_1, self.txtComponentCount_2, self.txtComponentCount_3, self.txtComponentCount_4, self.txtComponentCount_5,
                                   self.txtComponentCount_6, self.txtComponentCount_7, self.txtComponentCount_8, self.txtComponentCount_9, self.txtComponentCount_10,
                                   self.txtComponentCount_11, self.txtComponentCount_12, self.txtComponentCount_13, self.txtComponentCount_14, self.txtComponentCount_15,
                                   self.txtComponentCount_16, self.txtComponentCount_17, self.txtComponentCount_18, self.txtComponentCount_19, self.txtComponentCount_20]
        self.btnSave.setEnabled(False)
        self.txtStudentID.textChanged.connect(self.enable_save)
        self.txtStudentID.textChanged.connect(self.disable_load)
        self.txtStudentName.textChanged.connect(self.enable_save)
        self.txtStudentName.textChanged.connect(self.disable_load)
        self.chkGraduate.stateChanged.connect(self.enable_save)
        self.chkGraduate.stateChanged.connect(self.disable_load)
        self.cboCollege.currentIndexChanged.connect(self.enable_save)
        self.cboCollege.currentIndexChanged.connect(self.disable_load)
        for cn in self.componentNameList:
            cn.textChanged.connect(self.enable_save)
            cn.textChanged.connect(self.disable_load)
        for cc in self.componentCountList:
            cc.textChanged.connect(self.enable_save)
            cc.textChanged.connect(self.disable_load)
        self.btnLoad.clicked.connect(self.loadData)
        self.btnSave.clicked.connect(self.save)
        self.btnClear.clicked.connect(self.clear)

    def clear(self):
        self.txtStudentID.setText("")
        self.txtStudentName.setText("")
        self.chkGraduate.setChecked(False)
        self.cboCollege.setCurrentIndex(0)
        for cn in self.componentNameList:
            cn.setText("")
        for cc in self.componentCountList:
            cc.setText("")
        self.btnLoad.setEnabled(True)
        self.btnSave.setEnabled(False)

    def enable_save(self):
        self.btnSave.setEnabled(True)

    def disable_load(self):
        self.btnLoad.setEnabled(False)

    def save(self):
        with open("target.xml", "w") as tfile:
            tfile.writelines('<?xml version="1.0" encoding="UTF-8"?>\n')
            tfile.writelines("<Content>\n")
            sname = self.txtStudentName.text()
            sid = self.txtStudentID.text()
            if self.chkGraduate.isChecked():
                sgrad = "true"
            else:
                sgrad = "false"
            scollege = self.cboCollege.itemText(self.cboCollege.currentIndex())
            tfile.writelines('    <StudentName graduate="{0}">{1}</StudentName>\n'.format(sgrad, sname))
            tfile.writelines('    <StudentID>{0}</StudentID>\n'.format(sid))
            tfile.writelines('    <College>{0}</College>\n'.format(scollege))
            tfile.writelines('    <Components>')
            for x in range(len(self.componentNameList)):
                if not self.componentNameList[x].text() == "" and not self.componentCountList == "":
                    tfile.writelines('\n        <Component name="{0}" count="{1}" />'.format(self.componentNameList[x].text(), self.componentCountList[x].text()))
            tfile.writelines('\n    </Components>')
            tfile.writelines('\n</Content>')



    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """
        with open(filePath, "r") as tfile:
            data = tfile.readlines()
        data = data[2:-2]
        e1 = r"\"(?P<a>[\w]+)\">(?P<b>[\w\s]+)<"
        m1 = re.search(e1,data[0])
        tg = m1.group("a")
        tn = m1.group("b")
        if tg == "true":
            self.chkGraduate.setChecked(True)
        else:
            self.chkGraduate.setChecked(False)
        self.txtStudentName.setText(tn)
        e2 = r">(?P<c>[\d|\-]+)<"
        m2 = re.search(e2, data[1])
        tid = m2.group("c")
        self.txtStudentID.setText(tid)
        e3 = r">(?P<d>[\w\s\-]+)<"
        m3 = re.search(e3, data[2])
        colleges = ["-----", "Aerospace Engineering", "Civil Engineering", "Computer Engineering", "Electrical Engineering", "Industrial Engineering", "Mechanical Engineering"]
        tcol = m3.group("d")
        for x in range(len(colleges)):
            if tcol == colleges[x]:
                self.cboCollege.setCurrentIndex(x)
        e4 = r"name=\"(?P<e>[\w\s\-]+)\" count=\"(?P<f>[\d]+)\""
        if len(data) > 24:
            tlen = 24
        else:
            tlen = len(data)
        for i in range(4,tlen):
            m4 = re.search(e4, data[i])
            cn = m4.group("e")
            cc = m4.group("f")
            self.componentNameList[i-4].setText(cn)
            self.componentCountList[i-4].setText(cc)
        self.btnLoad.setEnabled(False)


    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
