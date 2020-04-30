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
from PyQt5.QtWidgets import QMessageBox, QDialogButtonBox
from numpy.lib import recfunctions as rfn
import  pandas as pd
from skimage.draw import polygon, line, set_color



from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from skimage import data

from shapely.geometry import Polygon



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 540)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label.setObjectName("label")
        self.segmetLabel = QtWidgets.QLabel(Dialog)
        self.segmetLabel.setGeometry(QtCore.QRect(479, 40, 384, 308))
        self.segmetLabel.setStyleSheet("background-color: white; border: 1px inset grey; min-height: 200px;")

        self.segmetLabel.setObjectName("segmetLabel")
        self.Upload_bott = QtWidgets.QPushButton(Dialog)
        self.Upload_bott.setGeometry(QtCore.QRect(120, 15, 101, 23))
        self.Upload_bott.setObjectName("Upload_bott")
        self.Segment_bott = QtWidgets.QPushButton(Dialog)
        self.Segment_bott.setGeometry(QtCore.QRect(392, 380, 80, 23))
        self.Segment_bott.setObjectName("Segment_bott")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(500, 20, 151, 16))
        self.label_2.setObjectName("label_2")
        self.image = QtWidgets.QLabel(Dialog)
        self.image.setGeometry(QtCore.QRect(320, 50, 271, 211))
        self.image.setText("")
        self.image.setObjectName("image")
        self.imageTest = QtWidgets.QLabel(Dialog)
        self.imageTest.setStyleSheet("background-color: white; border: 1px inset grey; min-height: 200px;")
        self.imageTest.setGeometry(QtCore.QRect(5, 40, 384, 308))
        self.imageTest.setText("")
        self.imageTest.setObjectName("imageTest")
        self.infoTable = QtWidgets.QTableWidget(Dialog)
        self.infoTable.setGeometry(QtCore.QRect(10, 450, 300, 70))
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
        self.cnvJPG.setGeometry(QtCore.QRect(220, 380, 80, 23))
        self.cnvJPG.setObjectName("cnvJPG")
        self.cnvDicom = QtWidgets.QPushButton(Dialog)
        self.cnvDicom.setGeometry(QtCore.QRect(100, 380, 80, 23))
        self.cnvDicom.setObjectName("cnvDicom")
        self.jpgSaveLabel = QtWidgets.QLabel(Dialog)
        self.jpgSaveLabel.setGeometry(QtCore.QRect(220, 360, 71, 20))
        self.jpgSaveLabel.setObjectName("jpgSaveLabel")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 360, 91, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(540, 450, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.alpha = QtWidgets.QDoubleSpinBox(Dialog)
        self.alpha.setGeometry(QtCore.QRect(500, 380, 80, 23))
        self.alpha.setObjectName("alpha")
        self.beta = QtWidgets.QDoubleSpinBox(Dialog)
        self.beta.setGeometry(QtCore.QRect(500, 450, 80, 23))
        self.beta.setObjectName("beta")
        self.gama = QtWidgets.QDoubleSpinBox(Dialog)
        self.gama.setGeometry(QtCore.QRect(500, 500, 80, 23))
        self.gama.setObjectName("gama")
        
    
        
        self.Upload_bott.clicked.connect(self.loadDicom)
        self.cnvJPG.clicked.connect(self.savePNG)
        self.Segment_bott.clicked.connect(self.active_contour)


        
        self.count = 0
        self.msg = QtWidgets.QMessageBox()
        self.last_x, self.last_y = None, None
        self.apt = 0
        
        self.countCoords = 0
        self.listOfCoords1 = []
        self.listOfCoords2 = []
        self.listOfCoords3 = []
        
        self.ss1=0
        self.imginit=0
        
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
        
        #empty the list of coords each load of new DICOM image
        self.countCoords = 0
        
        self.listOfCoords1.clear()
        self.listOfCoords2.clear()
        self.listOfCoords3.clear()
        
        # load dicom file
        self.dataset = pydicom.dcmread(fileName[0])
        # normalize the image to darken the dicom slice image
        self.imginit = self.dataset.pixel_array
        print('shape',self.imginit.shape, type(self.imginit) , self.imginit.dtype)
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
        self.imageTest.mouseMoveEvent = self.drawMove
        
        

        
        

    
    def drawMove(self, e):
        
        if self.last_x is None: # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return # Ignore the first time.
        
        # Pen drawing settings 
        painter = QtGui.QPainter(self.imageTest.pixmap())
        p = painter.pen()
        p.setWidth(4)
        p.setColor(QtGui.QColor('#FF0000'))
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
       
        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()
        print(self.last_x, self.last_y)
        
        # Save the manual segmented coordinates to list 
        if(self.countCoords == 0):
            self.listOfCoords1.append([self.last_x,self.last_y])
            
        if(self.countCoords == 1):
            self.listOfCoords2.append([self.last_x,self.last_y])
            
        if(self.countCoords == 2):
            self.listOfCoords3.append([self.last_x,self.last_y])    
        
        # release mouse 
        self.imageTest.mouseReleaseEvent = self.release
     
        # not drawing outside the image 
        if(self.last_x > self.imageTest.width() or self.last_y > self.imageTest.height() or self.last_y < 0 or self.last_x < 0 ):
            self.msg.setWindowTitle("Image")
            self.msg.setInformativeText('Out of image label.')
            self.msg.exec()
            self.last_x = None
            self.last_y = None
            
        # Refresh    
        self.imageTest.update()
     
        
    def release(self, e):
        self.last_x = None
        self.last_y = None
        self.countCoords += 1
        
    def savePNG(self):
        if(self.countCoords != 3 ):
            self.msg.setWindowTitle("Warning")
            self.msg.setInformativeText('3 segmented objects needed!')
            self.msg.exec()
        else:
            # pop up message to check image is saved
            self.msg.setWindowTitle("Save To JPG ")
            self.msg.setInformativeText('Image has been Saved.')
            self.msg.exec()
            self.path = './Dicom_Slices'
            # Save Dicom MRI image to file 
            cv2.imwrite(os.path.join(self.path,'testImage{0}.jpg'.format(self.count)), self.image_2d_scaled) 
            
               
            # normalize the labeled image
            self.qImg = self.pixmap.toImage()
            
            #s = self.qImg.bits().asstring((self.imageTest.width * self.imageTest.height) * channels_count)
            #arr = np.fromstring(s, dtype=np.uint8).reshape((self.imageTest.height, self.imageTest.width, channels_count))
            self.labeledImg = qimage2ndarray.recarray_view(self.qImg)
            self.threshold = 500 # Adjust as needed
            #self.imgLabeledScaled = (np.maximum(self.labeledImg, 0) / (np.amax(self.labeledImg) + self.threshold)) * 255.0 
            #print('shape2' , self.labeledImg.shape , type(self.labeledImg))
            #cv2.imwrite(os.path.join(self.path,'testImageLabeled{0}.jpg'.format(self.count)), np.array(self.qImg)) 
            self.ss1 = np.array(self.listOfCoords1)
            self.ss2 = np.array(self.listOfCoords2)
            self.ss3 = np.array(self.listOfCoords3)
            #plt.imshow(self.imginit)
            
            #plt.plot(ss1[:,0],ss1[:,1],'r')
            #plt.plot(ss2[:,0],ss2[:,1],'r')
            #plt.plot(ss3[:,0],ss3[:,1],'r')
            
            #poly1 = Polygon([p[0],p[1]] for p in self.ss1)
            #self.x1,self.y1 = poly1.convex_hull.exterior.coords.xy
            
            #poly2 = Polygon([p[0],p[1]] for p in self.ss2)
            #self.x2,self.y2 = poly2.convex_hull.exterior.coords.xy
            
            #poly3 = Polygon([p[0],p[1]] for p in self.ss3)
            #self.x3,self.y3 = poly3.convex_hull.exterior.coords.xy
            
            
            plt.plot(self.ss1[:,0],self.ss1[:,1],'r')
            plt.plot(self.ss2[:,0],self.ss2[:,1],'r')

            plt.plot(self.ss3[:,0],self.ss3[:,1],'r')

            self.img = np.zeros((308, 384), dtype=np.uint8)
            set_color(self.imginit, (self.ss1[:,1],self.ss1[:,0]), 1)
            plt.imshow(self.imginit)
            plt.show()
            
         
            
            
    def active_contour(self):
        img = rgb2gray(self.image_2d_scaled)
        alpha=self.alpha.value()
        beta=self.beta.value()
        gamma=self.gama.value()

        
        init1 = np.array([self.ss1[:,0],self.ss1[:,1]]).T
        init2 = np.array([self.ss2[:,0],self.ss2[:,1]]).T

        init3 = np.array([self.ss3[:,0],self.ss3[:,1]]).T
        
    
        '''  ..
        (image, snake, alpha=0.01, beta=0.1,
                   w_line=0, w_edge=1, gamma=0.01,
                   bc=None, max_px_move=1.0,
                   max_iterations=2500, convergence=0.1,
                   *,
                   boundary_condition='periodic',
                   coordinates=None):
            
        '''
     
        snake1 = active_contour(gaussian(img, 3),
                               init1, alpha, beta,gamma,max_iterations=4000,  
                               coordinates='rc')
        
        
        snake2 = active_contour(gaussian(img, 3),
                               init2, alpha, beta,gamma,max_iterations=4000,  
                               coordinates='rc')
        snake3 = active_contour(gaussian(img, 3),
                               init3, alpha, beta,gamma,max_iterations=4000,  
                               coordinates='rc')
        
        
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.imshow(img, cmap=plt.cm.gray)
        ax.plot(init1[:, 0], init1[:, 1], '-r', lw=3)
        ax.plot(snake1[:, 0], snake1[:, 1], '-b', lw=3)
        ax.plot(init2[:, 0], init2[:, 1], '-r', lw=3)
        ax.plot(snake2[:, 0], snake2[:, 1], '-b', lw=3)
        ax.plot(init3[:, 0], init3[:, 1], '-r', lw=3)
        ax.plot(snake3[:, 0], snake3[:, 1], '-b', lw=3)
        ax.set_xticks([]), ax.set_yticks([])
        ax.axis([0, img.shape[1], img.shape[0], 0])
        
        plt.show()
        
        
        
                            
                

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.update()
    sys.exit(app.exec_())
