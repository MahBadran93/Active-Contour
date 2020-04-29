# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files,get_testdata_file
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from pydicom.data import get_testdata_files,get_testdata_file
import pydicom
import qimage2ndarray
import  numpy as np
import qwt
from skimage.color import lab2rgb, lch2lab, rgb2gray
from pydicom.pixel_data_handlers.util import apply_voi_lut
import  cv2
import  os
from PyQt5.QtWidgets import QMessageBox 



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(891, 588)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 71, 16))
        self.label.setObjectName("label")
        self.Upload_bott = QtWidgets.QPushButton(Dialog)
        self.Upload_bott.setGeometry(QtCore.QRect(90, 260, 101, 23))
        self.Upload_bott.setObjectName("Upload_bott")
        self.Segment_bott = QtWidgets.QPushButton(Dialog)
        self.Segment_bott.setGeometry(QtCore.QRect(210, 320, 80, 23))
        self.Segment_bott.setObjectName("Segment_bott")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(310, 20, 151, 16))
        self.label_2.setObjectName("label_2")
        self.image = QtWidgets.QLabel(Dialog)
        self.image.setGeometry(QtCore.QRect(320, 50, 271, 211))
        self.image.setText("")
        self.image.setObjectName("image")
        self.imageTest = QtWidgets.QLabel(Dialog)
        self.imageTest.setGeometry(QtCore.QRect(0, 40, 271, 211))
        self.imageTest.setText("")
        self.imageTest.setObjectName("imageTest")
        self.infoTable = QtWidgets.QTableWidget(Dialog)
        self.infoTable.setGeometry(QtCore.QRect(10, 450, 521, 111))
        self.infoTable.setObjectName("infoTable")
        self.infoTable.setColumnCount(7)
        self.infoTable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(6, item)
        self.infoLabel = QtWidgets.QLabel(Dialog)
        self.infoLabel.setGeometry(QtCore.QRect(10, 430, 121, 16))
        self.infoLabel.setObjectName("infoLabel")
        self.cnvJPG = QtWidgets.QPushButton(Dialog)
        self.cnvJPG.setGeometry(QtCore.QRect(100, 320, 80, 23))
        self.cnvJPG.setObjectName("cnvJPG")
        self.cnvDicom = QtWidgets.QPushButton(Dialog)
        self.cnvDicom.setGeometry(QtCore.QRect(100, 380, 80, 23))
        self.cnvDicom.setObjectName("cnvDicom")
        self.jpgSaveLabel = QtWidgets.QLabel(Dialog)
        self.jpgSaveLabel.setGeometry(QtCore.QRect(100, 300, 71, 20))
        self.jpgSaveLabel.setObjectName("jpgSaveLabel")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 360, 91, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(540, 450, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.Upload_bott.clicked.connect(self.loadDicom)
        self.cnvJPG.clicked.connect(self.savePNG)

        self.count = 0



        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "MRI Image"))
        self.Upload_bott.setText(_translate("Dialog", "Upload Image"))
        self.Segment_bott.setText(_translate("Dialog", "Segment"))
        self.label_2.setText(_translate("Dialog", "Segmented Image "))
        item = self.infoTable.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "results"))
        item = self.infoTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name"))
        item = self.infoTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "ID"))
        item = self.infoTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "BirthDate"))
        item = self.infoTable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "StudyID"))
        item = self.infoTable.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "StudyDate"))
        item = self.infoTable.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "SliceLocation"))
        item = self.infoTable.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "InstanceNumber"))
        self.infoLabel.setText(_translate("Dialog", "Patient Information "))
        self.cnvJPG.setText(_translate("Dialog", "JPG"))
        self.cnvDicom.setText(_translate("Dialog", "DICOM"))
        self.jpgSaveLabel.setText(_translate("Dialog", "save to JPG"))
        self.label_3.setText(_translate("Dialog", "save to Dicom"))
        self.pushButton.setText(_translate("Dialog", "Save anonymized"))


    def loadDicom(self):
        
        # open browse dialog 
        fileName = QFileDialog.getOpenFileName()
        
        # load dicom file
        self.dataset = pydicom.dcmread(fileName[0])
        
        # normalize the image to darken the dicom slice image
        self.imginit = self.dataset.pixel_array
        self.threshold = 500 # Adjust as needed
        self.image_2d_scaled = (np.maximum(self.imginit, 0) / (np.amax(self.imginit) + self.threshold)) * 255.0 
        self.img=qimage2ndarray.array2qimage(self.image_2d_scaled)
        
        #write on table, Patient info 
        self.infoTable.setItem(0, 0, QtWidgets.QTableWidgetItem(str(self.dataset.PatientName)))
        self.infoTable.setItem(0, 1, QtWidgets.QTableWidgetItem(str(self.dataset.PatientID)))
        self.infoTable.setItem(0, 2, QtWidgets.QTableWidgetItem(str(self.dataset.PatientBirthDate)))
        self.infoTable.setItem(0, 3, QtWidgets.QTableWidgetItem(str(self.dataset.StudyID)))
        self.infoTable.setItem(0, 4, QtWidgets.QTableWidgetItem(str(self.dataset.StudyDate)))
        self.infoTable.setItem(0, 5, QtWidgets.QTableWidgetItem(str(self.dataset.SliceLocation)))
        self.infoTable.setItem(0, 6, QtWidgets.QTableWidgetItem(str(self.dataset.InstanceNumber)))

        # add the image to label     
        self.pixmap = QtGui.QPixmap(self.img)    
        self.imageTest.setPixmap(self.pixmap.scaled(self.imageTest.width(),self.imageTest.height()))

    def savePNG(self):
        msg = QMessageBox()

        self.path = './Dicom_Slices'
        cv2.imwrite(os.path.join(self.path,'testImage{0}.jpg'.format(self.count)), self.image_2d_scaled) 
        self.count += 1
    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
