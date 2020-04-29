"""
=======================================
Read DICOM and ploting using matplotlib
=======================================

This example illustrates how to open a DICOM file, print some dataset
information, and show it using matplotlib.

"""

# authors : Guillaume Lemaitre <g.lemaitre58@gmail.com>
# license : MIT

import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files,get_testdata_file
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from pydicom.data import get_testdata_files,get_testdata_file
import pydicom
import qimage2ndarray
import  numpy as np
import qwt


#self.Upload_bott.clicked.connect(self.loadDicom)

def loadDicom(self):
    fileName = QFileDialog.getOpenFileName()
    print(fileName[0])
    dataset = pydicom.dcmread(fileName[0])
    img=qimage2ndarray.array2qimage(dataset.pixel_array)
    #qimg = QtGui.QImage(dataset.pixel_array)
    #img2 = dataset.pixel_array.astype(np.int32)
    
    
    #myImg = qwt.toqimage.array_to_qimage(dataset.pixel_array)
    pixmap = QtGui.QPixmap(img)
    print('ttttt',self.imageTest.width())
    
    self.imageTest.setPixmap(pixmap.scaled(self.imageTest.width(),self.imageTest.height()))


