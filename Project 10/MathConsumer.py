# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *

from calculator import *

class MathConsumer (QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MathConsumer, self).__init__(parent)
        self.setupUi(self)
        self.btnCalculate.pressed.connect(self.performOperation)

    def performOperation(self):
        try:
            if self.edtNumber1.text() == "" or self.edtNumber2.text() == "":
                self.edtResult.setText("E")
            if self.cboOperation.currentIndex() == 0:
                self.edtResult.setText(str(float(self.edtNumber1.text()) + float(self.edtNumber2.text())))
            elif self.cboOperation.currentIndex() == 1:
                self.edtResult.setText(str(float(self.edtNumber1.text()) - float(self.edtNumber2.text())))
            elif self.cboOperation.currentIndex() == 2:
                self.edtResult.setText(str(float(self.edtNumber1.text()) * float(self.edtNumber2.text())))
            elif self.cboOperation.currentIndex() == 3:
                if self.edtNumber2.text() == "0":
                    self.edtResult.setText("E")
                else:
                    self.edtResult.setText(str(float(self.edtNumber1.text()) / float(self.edtNumber2.text())))
        except:
            self.edtResult.setText("E")

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = MathConsumer()

    currentForm.show()
    currentApp.exec_()
