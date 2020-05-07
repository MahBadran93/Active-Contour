# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

# needed libraries to install : 
# pyqt5, matplotlib, pydicom, qimage2ndarray, 
# skimage, cv2, os, pandas  
#...........................Imported libraries..................
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files,get_testdata_file
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from pydicom.data import get_testdata_files,get_testdata_file
import qimage2ndarray
import  numpy as np
from skimage.color import lab2rgb, lch2lab, rgb2gray
#from pydicom.pixel_data_handlers.util import apply_voi_lut
import  cv2
import  os
from PyQt5.QtWidgets import QMessageBox, QDialogButtonBox
#from numpy.lib import recfunctions as rfn
import  pandas as pd
from skimage.draw import polygon, line, set_color
#import  PIL.Image as imgCnv
from pydicom.dataset import Dataset, FileDataset
# lib to draw 3D
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
#####################################################################


from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from skimage import data

from shapely.geometry import Polygon



class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1500, 540)
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
        self.Segment_bott.setGeometry(QtCore.QRect(395, 80, 80, 23))
        self.Segment_bott.setObjectName("Segment_bott")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(500, 20, 151, 16))
        self.label_2.setObjectName("label_2")
      
        self.imageTest = QtWidgets.QLabel(Dialog)
        self.imageTest.setStyleSheet("background-color: white; border: 1px inset grey; min-height: 200px;")
        self.imageTest.setGeometry(QtCore.QRect(5, 40, 384, 308))
        self.imageTest.setText("")
        self.imageTest.setObjectName("imageTest")
        self.infoTable = QtWidgets.QTableWidget(Dialog)
        self.infoTable.setGeometry(QtCore.QRect(900, 40, 230, 230))
        self.infoTable.setObjectName("infoTable")
        self.infoTable.setColumnCount(1)
        self.infoTable.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem() 
        self.infoTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(6, item)
        self.infoLabel = QtWidgets.QLabel(Dialog)
        self.infoLabel.setGeometry(QtCore.QRect(920, 20, 121, 16))
        self.infoLabel.setObjectName("infoLabel")
        #####################################################
        self.cnvJPG = QtWidgets.QPushButton(Dialog)
        self.cnvJPG.setGeometry(QtCore.QRect(250, 380, 80, 23))
        self.cnvJPG.setObjectName("cnvJPG")
        self.plt3D = QtWidgets.QPushButton(Dialog)
        self.plt3D.setGeometry(QtCore.QRect(160, 380, 80, 23))
        self.plt3D.setObjectName("plt3D")
        self.Save_anonymized = QtWidgets.QPushButton(Dialog)
        self.Save_anonymized.setGeometry(QtCore.QRect(20, 380, 130, 23))
        self.Save_anonymized.setObjectName("Save anonymized")
        #############################################
        self.jpgSaveLabel = QtWidgets.QLabel(Dialog)
        self.jpgSaveLabel.setGeometry(QtCore.QRect(250, 360, 71, 23))
        self.jpgSaveLabel.setObjectName("jpgSaveLabel")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(185, 360, 91, 23))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 360, 80, 23))
        self.label_4.setObjectName("anonymized")

        
        self.alpha = QtWidgets.QDoubleSpinBox(Dialog)
        self.alpha.setGeometry(QtCore.QRect(395, 140, 80, 23))
        self.alpha.setObjectName("alpha")
        self.alpha.setDecimals(5)
        self.beta = QtWidgets.QDoubleSpinBox(Dialog)
        self.beta.setGeometry(QtCore.QRect(395, 200, 80, 23))
        self.beta.setObjectName("beta")
        self.beta.setDecimals(5)
        self.gama = QtWidgets.QDoubleSpinBox(Dialog)
        self.gama.setGeometry(QtCore.QRect(395, 260, 80, 23))
        self.gama.setObjectName("gama")
        self.gama.setDecimals(5)

        
        self.alpha_label = QtWidgets.QLabel(Dialog)
        self.alpha_label.setGeometry(QtCore.QRect(395, 120, 80, 23))

        self.beta_label = QtWidgets.QLabel(Dialog)
        self.beta_label.setGeometry(QtCore.QRect(395, 180, 80, 23))

        self.gamm_label = QtWidgets.QLabel(Dialog)
        self.gamm_label.setGeometry(QtCore.QRect(395, 240, 80, 23))

        # Set background color 
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background,QtGui.QColor(174, 173, 172));
        Dialog.autoFillBackground()
        Dialog.setPalette(pal)
        

        self.Upload_bott.clicked.connect(self.loadDicom)
        self.cnvJPG.clicked.connect(self.savePNG)
        self.Segment_bott.clicked.connect(self.active_contour)
        self.plt3D.clicked.connect(self.draw3D)
        self.Save_anonymized.clicked.connect(self.Anonymize)



        
        self.msg = QtWidgets.QMessageBox()
        
        
        # disable segment button until the user manually segment all the manual contours required 
        self.Segment_bott.setEnabled(False)
        
        # disable save jpg button until the two images are loaded(test image and segmented image)
        self.cnvJPG.setEnabled(False)
        
        # disable anonymized button until you loaded the test image.
        self.Save_anonymized.setEnabled(False)
        
        # disable show 3D button
        self.plt3D.setEnabled(False)

     
        
        # initalise the x,y coordinates 
        self.last_x, self.last_y = None, None

        # initalise variable to hold the image of dicom file 
        self.imginit=0
        
        #self.flagLabelnotempty = 0
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "MRI Image"))
        self.Upload_bott.setText(_translate("Dialog", "Upload Dicom "))
        self.Segment_bott.setText(_translate("Dialog", "Segment"))
        self.label_2.setText(_translate("Dialog", "Segmented Image "))
        #item = self.infoTable.horizontalHeaderItem(0)
        #item.setText(_translate("Dialog", "results"))
        item = self.infoTable.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Name"))
        item = self.infoTable.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "ID"))
        item = self.infoTable.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "BirthDate"))
        item = self.infoTable.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "StudyID"))
        item = self.infoTable.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "StudyDate"))
        item = self.infoTable.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "SliceLocation"))
        item = self.infoTable.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "InstanceNumber"))
        self.infoLabel.setText(_translate("Dialog", "Patient Information "))
        self.cnvJPG.setText(_translate("Dialog", "JPG"))
        self.plt3D.setText(_translate("Dialog", "plot 3D"))
        self.jpgSaveLabel.setText(_translate("Dialog", "save to JPG"))
        self.label_3.setText(_translate("Dialog", "Plot"))
        self.label_4.setText(_translate("Dialog", "anonymize"))

        self.Save_anonymized.setText(_translate("Dialog", "Save anonymized"))
        self.alpha_label.setText('alpha')
        self.beta_label.setText('beta')
        self.gamm_label.setText('gamma')
       




    # this function is used  to load dicom data   
    def loadDicom(self):
        '''
        
        '''    
        # disable segment button until the user manually segment all the manual contours required 
        self.Segment_bott.setEnabled(False)
        
        # disable save jpg button until the two images are loaded(test image and segmented image)
        self.cnvJPG.setEnabled(False)

        # disable show 3d button
        self.plt3D.setEnabled(False)

        
        # disable anonymized button until you loaded the test image.
        self.Save_anonymized.setEnabled(False)
     
        # initalise the x,y coordinates 
        self.last_x, self.last_y = None, None
        
        # initalize variables to hold numpy array of coordinates to plot 3D shape 
        self.x, self.x1, self.x2 = [], [], []
        self.y, self.y1, self.y2 = [], [], []
        self.z = []
        
        # list of coordinates for each contour the user segmented. 
        self.countCoords = 0 
        self.listOfCoords1 = []
        self.listOfCoords2 = []
        self.listOfCoords3 = []
        self.listOfCoords4 = []

         
        # Flags to not draw more that 3 contours 
        self.countCoords = 0
        
        #self.flagLabelnotempty = 1
        
        
        
        # open browse dialog 
        fileName = QFileDialog.getOpenFileName()
        
       
        # when load the test image enable the save Save_anonymize button 
        self.Save_anonymized.setEnabled(True)
        
        # clear the label each time we load an image 
        self.segmetLabel.clear()
        self.imageTest.clear()
        # empty the list of coords each load of new DICOM image
        self.listOfCoords1.clear()
        self.listOfCoords2.clear()
        self.listOfCoords3.clear()
        self.listOfCoords4.clear()

   

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
        self.imageTest.mouseMoveEvent = self.drawMove
        #information Message
        self.msg.setWindowTitle("Informations")
        self.msg.setInformativeText('You can draw on the image for manual segmetation of the tumor, TZ, CZ,PZ by moving the mouse around the object. Only 4 objects are allowed to segment or you cant continue. You can edit the alpha, beta, gamma for a better segmentation results  ')
        self.msg.exec()
    '''        
    def otherWindowSaveDicom(self):
       self.EditDicom = EditDicomWindow()
       self.EditDicom.show()
    '''         
    # Activates when the user start press and moving the mouse to draw the contours
    def drawMove(self, e):
        if(self.countCoords > 3 ):
            self.msg.setWindowTitle("Warning")
            self.msg.setInformativeText('3 segmented objects needed!')
            self.msg.exec()
        else:     
        
            if self.last_x is None: # First event.
                self.last_x = e.x()
                self.last_y = e.y()
                return # Ignore the first time.
            
            # Pen drawing settings 
            painter = QtGui.QPainter(self.imageTest.pixmap())
            p = painter.pen()
            p.setWidth(1)
            p.setColor(QtGui.QColor('#FF0000'))
            painter.setPen(p)
            painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
            painter.end()
           
            # Update the origin for next time.
            self.last_x = e.x()
            self.last_y = e.y()
            #print(self.last_x, self.last_y)
            
            # Save the manual segmented coordinates to list 
            if(self.countCoords == 0):
                self.listOfCoords1.append([self.last_x,self.last_y])
                
            if(self.countCoords == 1):
                self.listOfCoords2.append([self.last_x,self.last_y])
                
            if(self.countCoords == 2):
                self.listOfCoords3.append([self.last_x,self.last_y])    
            
            if(self.countCoords == 3):
                self.listOfCoords4.append([self.last_x,self.last_y])    
            
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
     
    # Mouse event, when the user release the mouse this function activates     
    def release(self, e):
        self.last_x = None
        self.last_y = None
        self.countCoords += 1
        if (self.countCoords == 4):
            # list of coords to numpy array 
            self.ss1 = np.array(self.listOfCoords1)
            self.ss2 = np.array(self.listOfCoords2)
            self.ss3 = np.array(self.listOfCoords3)
            self.ss4 = np.array(self.listOfCoords4)
            self.Segment_bott.setEnabled(True)
        
    # this function activates when the user press JPG button, which saves the two images in folder Dicom_JPG  
    def savePNG(self):     
        self.path = './Dicom_JPG'
        # Save Dicom MRI image to file 
        cv2.imwrite(os.path.join(self.path,'testImage{0}.jpg'.format(self.dataset.InstanceNumber)), self.image_2d_scaled) 
        # same Dicom mri image with segmentation above it
        cv2.imwrite(os.path.join(self.path,'segmentedImg{0}.jpg'.format(self.dataset.InstanceNumber)), self.img) 
        # same only the segmented objects, masks
        cv2.imwrite(os.path.join(self.path,'Mask{0}.jpg'.format(self.dataset.InstanceNumber)), self.maskImg) 

        # pop up message to check image is saved
        self.msg.setWindowTitle("Save To JPG ")
        self.msg.setInformativeText('Images has been Saved.')
        self.msg.exec()
               

    # Activate when the user press 'segment' button    
    def active_contour(self):
        
        # enable saving the image button 
        self.cnvJPG.setEnabled(True)
        
        # enable plt 3D button 
        self.plt3D.setEnabled(True)
        
        # clear the label each time the user press segment, to not store alot above each other 
        self.segmetLabel.clear()
  
        
        # convert to gray scale image 
        self.img = rgb2gray(self.image_2d_scaled.copy())
        
        # #  values of alpha, beta, gamma, that active contour function requires 
        # alpha=self.alpha.toPlainText()
        # print(alpha)
        # beta=self.beta.toPlainText()
        # print(beta)
        # gamma=self.gama.toPlainText()
        # print(gamma)
        
        alpha=self.alpha.value()
        beta=self.beta.value()
        gamma=self.gama.value()

        # Convert coordinates to numpy array
        init1 = np.array([self.ss1[:,0],self.ss1[:,1]]).T
        init2 = np.array([self.ss2[:,0],self.ss2[:,1]]).T
        init3 = np.array([self.ss3[:,0],self.ss3[:,1]]).T
        init4 = np.array([self.ss4[:,0],self.ss4[:,1]]).T


        # Apply the Active Contour functions on our 3 contours 
        snake1 = active_contour(gaussian(self.img, 3),
                               init1, alpha, beta,gamma,max_iterations=2500,  
                               coordinates='rc')
        
        
        snake2 = active_contour(gaussian(self.img, 3),
                                init2, alpha, beta,gamma,max_iterations=2500,  
                                coordinates='rc')
        snake3 = active_contour(gaussian(self.img, 3),
                                init3, alpha, beta,gamma,max_iterations=2500,  
                                coordinates='rc')
        snake4 = active_contour(gaussian(self.img, 3),
                                init4, alpha, beta,gamma,max_iterations=2500,  
                                coordinates='rc')

        # x,y,z for 3D plotting 
        self.x1 = snake1[:,0] 
        self.y1 = snake1[:,1] 
        self.z1 = np.ones(snake1.shape[0])

        self.x2 = snake2[:,0] 
        self.y2 = snake2[:,1] 
        self.z2 = np.ones(snake2.shape[0])

        self.x3 = snake3[:,0] 
        self.y3 = snake3[:,1] 
        self.z3 = np.ones(snake3.shape[0])

        self.x4 = snake4[:,0] 
        self.y4 = snake4[:,1]
        self.z4 = np.ones(snake4.shape[0])
                
        
       
        # draw the Segmentation results the snakes and edit on the image 
        cv2.fillConvexPoly(self.img,np.array(snake1,'int32'),(180, 0, 0))
        cv2.fillConvexPoly(self.img,np.array(snake2,'int32'),(100, 0, 50))
        cv2.fillConvexPoly(self.img,np.array(snake3,'int32'),(250, 15, 0))
        cv2.fillConvexPoly(self.img,np.array(snake4,'int32'),(250, 15, 0))

        self.maskImg = np.zeros(self.img.shape)
        
        cv2.fillConvexPoly(self.maskImg,np.array(snake1,'int32'),(180, 0, 0))
        cv2.fillConvexPoly(self.maskImg,np.array(snake2,'int32'),(100, 0, 50))
        cv2.fillConvexPoly(self.maskImg,np.array(snake3,'int32'),(250, 15, 0))
        cv2.fillConvexPoly(self.maskImg,np.array(snake4,'int32'),(250, 15, 0))

        
        self.segmentedImg = qimage2ndarray.array2qimage(self.maskImg)
        self.pixmap2 = QtGui.QPixmap(self.segmentedImg)    
        self.segmetLabel.setPixmap(self.pixmap2.scaled(self.imageTest.width(),self.imageTest.height()))
    
    # Activate when press on plot 3D button to draw the 3D shapes 
    def draw3D(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        surf = ax.plot_trisurf(self.x1, self.y1, self.z1)
        #ax.plot_trisurf(self.x1, self.y1, self.z, cmap = cm.cool)
        surf2 = ax.plot_trisurf(self.x2, self.y2, self.z2)
        surf3 = ax.plot_trisurf(self.x3, self.y3, self.z3)
        surf3 = ax.plot_trisurf(self.x4, self.y4, self.z4)
        for angle in range(0, 360):
            ax.view_init(30, angle)
            plt.draw()
            plt.pause(.001)
            plt.show()
        # rotate the axes and update

        fig.savefig('./3D_Plots/Plot3D{0}.png'.format(self.dataset.InstanceNumber))

    # Edit patient information and save to a Dicom file in folder DICOM_Anony     
    def Anonymize(self):
        data_elements = ['PatientID',
                         'PatientName'
                         'PatientBirthDate']
        for de in data_elements:
            print(self.dataset.data_element(de))
        self.dataset.PatientName = '' 
        self.dataset.PatientID = '' 
        self.dataset.PatientBirthDate = '' 
        self.dataset.save_as('./DICOM_Anony/Dicom_Slice{0}.dcm'.format(self.dataset.InstanceNumber))
        # this function used to plot the labeled image, not used in the gui currently  
        self.msg.setWindowTitle("Save TAnonymized ")
        self.msg.setInformativeText('Dicom file has been Saved.')
        self.msg.exec()
    

    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.update()
    sys.exit(app.exec_())
    