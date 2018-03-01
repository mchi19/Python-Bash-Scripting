#! /bin/usr/env python3.4

from SteganographyGUI import *
from Steganography import *
from PySide.QtGui import *
from PySide.QtCore import *
from functools import partial

class Processor (QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Processor, self).__init__(parent)
        self.setupUi(self)
        self.chkApplyCompression.setEnabled(True)
        self.chkApplyCompression.setChecked(False)
        self.txtCompression.setEnabled(False)
        self.lblLevel.setEnabled(False)
        self.slideCompression.setEnabled(False)
        self.txtCompression.setText(str(0))
        self.slideCompression.setValue(0)
        self.chkOverride.setEnabled(False)
        self.btnSave.setEnabled(False)
        self.btnExtract.setEnabled(False)
        self.btnClean.setEnabled(False)

        self.chkApplyCompression.clicked.connect(self.slideCompressionOn)
        self.btnSave.clicked.connect(self.saveTo)
        self.btnExtract.clicked.connect(self.extractPayload)
        self.btnClean.clicked.connect(self.cleanCarrier)

        templist = [self.viewPayload1, self.viewCarrier1, self.viewCarrier2]
        for x in templist:
            x.dragEnterEvent = self.accept_event
            x.dropEvent = partial(self.processDrop, x)


    def slideCompressionOn(self):
        try:
            if self.chkApplyCompression.isChecked():
                self.lblLevel.setEnabled(True)
                self.slideCompression.setEnabled(True)
                self.txtCompression.setEnabled(True)
                self.payload1 = Payload(rawData=self.payload1_img,compressionLevel=self.slideCompression.value())
                self.txtPayloadSize.setText(str(len(self.payload1.json)))
                self.slideCompression.valueChanged.connect(self.doCompression)
            else:
                self.lblLevel.setEnabled(False)
                self.slideCompression.setEnabled(False)
                self.txtCompression.setEnabled(False)
                self.payload1 = Payload(rawData=self.payload1_img)
                self.txtPayloadSize.setText(str(len(self.payload1.json)))
        except:
            pass
    def doCompression(self):
        self.txtCompression.setText(str(self.slideCompression.value()))
        self.payload1 = Payload(rawData=self.payload1_img,compressionLevel=self.slideCompression.value())
        self.txtPayloadSize.setText(str(len(self.payload1.json)))

    def accept_event(self, event):
        event.accept()

    def processDrop(self, x, event):
        mime = event.mimeData()
        if not mime.hasUrls():
            return
        fp = mime.urls()[0].toLocalFile()
        if fp[-3:] != "png":
            return

        if x is self.viewPayload1:
            self.genP1(fp)
        elif x is self.viewCarrier1:
            self.genC1(fp)
        else:
            self.carrier2_fp = fp
            self.genC2(fp)

        scene = QGraphicsScene()
        pmap = QPixmap(fp)
        scene.addPixmap(pmap)
        scene.dragMoveEvent = self.accept_event
        x.setScene(scene)
        x.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        x.show()
        self.enableSave()

    def genP1(self, fp):
        self.chkApplyCompression.setChecked(False)
        self.lblLevel.setEnabled(False)
        self.slideCompression.setValue(0)
        self.slideCompression.setEnabled(False)
        self.txtCompression.setText(str(0))
        self.txtCompression.setEnabled(False)
        self.payload1_img = imread(fp)
        self.payload1 = Payload(self.payload1_img)
        self.txtPayloadSize.setText(str(len(self.payload1.json)))
        self.slideCompression.valueChanged.connect(self.doCompression)

    def genC1(self, fp):
        self.carrier1_img = imread(fp)
        self.carrier1 = Carrier(self.carrier1_img)
        self.txtCarrierSize.setText(str(int(self.carrier1_img.size)))
        if self.carrier1.payloadExists() == True:
            self.lblPayloadFound.setText(">>>> Payload Found <<<<")
            self.chkOverride.setEnabled(True)
        else:
            self.lblPayloadFound.setText("")
            self.chkOverride.setEnabled(False)

    def genC2(self, fp):
        self.carrier2_img = imread(fp)
        self.carrier2 = Carrier(self.carrier2_img)

        if self.carrier2.payloadExists() == False:
            self.lblCarrierEmpty.setText(">>>> Carrier Empty <<<<")
            self.btnExtract.setEnabled(False)
            self.btnClean.setEnabled(False)
        else:
            self.lblCarrierEmpty.setText("")
            self.btnExtract.setEnabled(True)
            self.btnClean.setEnabled(True)

    def enableSave(self):
        self.chkOverride.setChecked(False)
        try:
            if self.payload1 is not None and self.carrier1 is not None:
                if self.carrier1_img.size >= len(self.payload1.json):
                    if self.carrier1.payloadExists() == False:
                        self.btnSave.setEnabled(True)
                    else:
                        self.chkOverride.setEnabled(True)
                        self.chkOverride.stateChanged.connect(self.chkOv)
                else:
                    self.btnSave.setEnabled(False)
            else:
                self.btnSave.setEnabled(False)
        except:
            pass

    def chkOv(self):
        if self.chkOverride.isChecked():
            self.btnSave.setEnabled(True)
        else:
            self.btnSave.setEnabled(False)

    def saveTo(self):
        tc = self.carrier1.embedPayload(self.payload1,override=True)
        fp,_ = QFileDialog.getSaveFileName(self)
        if fp[-4:] != ".png":
            fp = fp + ".png"
        imsave(fp,tc)

    def extractPayload(self):
        self.payload2 = self.carrier2.extractPayload()
        e1 = self.payload2.rawData
        h = self.payload2.rawData.shape[0]
        w = self.payload2.rawData.shape[1]
        image = QImage(e1,w,h,QImage.Format_RGB888) #RGB888
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(image))
        self.viewPayload2.setScene(scene)
        self.viewPayload2.fitInView(scene.sceneRect(),Qt.KeepAspectRatio)
        self.viewPayload2.show()

    def cleanCarrier(self):
        cc1 = self.carrier2.clean()
        imsave(self.carrier2_fp,cc1)
        self.genC2()

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Processor()

    currentForm.show()
    currentApp.exec_()