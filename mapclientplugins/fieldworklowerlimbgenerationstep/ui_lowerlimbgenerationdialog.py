# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/lowerlimbgenerationdialog.ui'
#
# Created: Sat Jun 20 22:10:13 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1177, 722)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget1 = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setMinimumSize(QtCore.QSize(400, 0))
        self.widget1.setMaximumSize(QtCore.QSize(600, 16777215))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtGui.QTableWidget(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.toolBox = QtGui.QToolBox(self.widget1)
        self.toolBox.setObjectName("toolBox")
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 382, 388))
        self.page_2.setObjectName("page_2")
        self.formLayout_3 = QtGui.QFormLayout(self.page_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_5 = QtGui.QLabel(self.page_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_7 = QtGui.QLabel(self.page_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(self.page_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtGui.QLabel(self.page_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_15 = QtGui.QLabel(self.page_2)
        self.label_15.setObjectName("label_15")
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtGui.QLabel(self.page_2)
        self.label_16.setObjectName("label_16")
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_16)
        self.label_17 = QtGui.QLabel(self.page_2)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_17)
        self.comboBox_RASIS = QtGui.QComboBox(self.page_2)
        self.comboBox_RASIS.setObjectName("comboBox_RASIS")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_RASIS)
        self.comboBox_LASIS = QtGui.QComboBox(self.page_2)
        self.comboBox_LASIS.setObjectName("comboBox_LASIS")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_LASIS)
        self.comboBox_Sacral = QtGui.QComboBox(self.page_2)
        self.comboBox_Sacral.setObjectName("comboBox_Sacral")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox_Sacral)
        self.comboBox_LEC = QtGui.QComboBox(self.page_2)
        self.comboBox_LEC.setObjectName("comboBox_LEC")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBox_LEC)
        self.comboBox_MEC = QtGui.QComboBox(self.page_2)
        self.comboBox_MEC.setObjectName("comboBox_MEC")
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.comboBox_MEC)
        self.comboBox_LM = QtGui.QComboBox(self.page_2)
        self.comboBox_LM.setObjectName("comboBox_LM")
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.comboBox_LM)
        self.comboBox_MM = QtGui.QComboBox(self.page_2)
        self.comboBox_MM.setObjectName("comboBox_MM")
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.FieldRole, self.comboBox_MM)
        self.label_23 = QtGui.QLabel(self.page_2)
        self.label_23.setObjectName("label_23")
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_23)
        self.doubleSpinBox_markerRadius = QtGui.QDoubleSpinBox(self.page_2)
        self.doubleSpinBox_markerRadius.setObjectName("doubleSpinBox_markerRadius")
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.FieldRole, self.doubleSpinBox_markerRadius)
        self.label_24 = QtGui.QLabel(self.page_2)
        self.label_24.setObjectName("label_24")
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_24)
        self.doubleSpinBox_skinPad = QtGui.QDoubleSpinBox(self.page_2)
        self.doubleSpinBox_skinPad.setObjectName("doubleSpinBox_skinPad")
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.FieldRole, self.doubleSpinBox_skinPad)
        self.toolBox.addItem(self.page_2, "")
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 405, 388))
        self.page.setObjectName("page")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_14 = QtGui.QLabel(self.page)
        self.label_14.setObjectName("label_14")
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_14)
        self.label_18 = QtGui.QLabel(self.page)
        self.label_18.setObjectName("label_18")
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_18)
        self.label_19 = QtGui.QLabel(self.page)
        self.label_19.setObjectName("label_19")
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_19)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.doubleSpinBox_ptx = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_ptx.setMinimum(-10000.0)
        self.doubleSpinBox_ptx.setMaximum(10000.0)
        self.doubleSpinBox_ptx.setObjectName("doubleSpinBox_ptx")
        self.horizontalLayout_11.addWidget(self.doubleSpinBox_ptx)
        self.doubleSpinBox_pty = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_pty.setMinimum(-1000.0)
        self.doubleSpinBox_pty.setMaximum(1000.0)
        self.doubleSpinBox_pty.setObjectName("doubleSpinBox_pty")
        self.horizontalLayout_11.addWidget(self.doubleSpinBox_pty)
        self.doubleSpinBox_ptz = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_ptz.setMinimum(-1000.0)
        self.doubleSpinBox_ptz.setMaximum(1000.0)
        self.doubleSpinBox_ptz.setObjectName("doubleSpinBox_ptz")
        self.horizontalLayout_11.addWidget(self.doubleSpinBox_ptz)
        self.formLayout_5.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_11)
        self.label_20 = QtGui.QLabel(self.page)
        self.label_20.setObjectName("label_20")
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_20)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.doubleSpinBox_prx = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_prx.setMinimum(-360.0)
        self.doubleSpinBox_prx.setMaximum(360.0)
        self.doubleSpinBox_prx.setObjectName("doubleSpinBox_prx")
        self.horizontalLayout_12.addWidget(self.doubleSpinBox_prx)
        self.doubleSpinBox_pry = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_pry.setMinimum(-360.0)
        self.doubleSpinBox_pry.setMaximum(360.0)
        self.doubleSpinBox_pry.setObjectName("doubleSpinBox_pry")
        self.horizontalLayout_12.addWidget(self.doubleSpinBox_pry)
        self.doubleSpinBox_prz = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_prz.setMinimum(-360.0)
        self.doubleSpinBox_prz.setMaximum(360.0)
        self.doubleSpinBox_prz.setObjectName("doubleSpinBox_prz")
        self.horizontalLayout_12.addWidget(self.doubleSpinBox_prz)
        self.formLayout_5.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_12)
        self.label_21 = QtGui.QLabel(self.page)
        self.label_21.setObjectName("label_21")
        self.formLayout_5.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_21)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.doubleSpinBox_hipx = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_hipx.setMinimum(-360.0)
        self.doubleSpinBox_hipx.setMaximum(360.0)
        self.doubleSpinBox_hipx.setObjectName("doubleSpinBox_hipx")
        self.horizontalLayout_13.addWidget(self.doubleSpinBox_hipx)
        self.doubleSpinBox_hipy = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_hipy.setMinimum(-360.0)
        self.doubleSpinBox_hipy.setMaximum(360.0)
        self.doubleSpinBox_hipy.setObjectName("doubleSpinBox_hipy")
        self.horizontalLayout_13.addWidget(self.doubleSpinBox_hipy)
        self.doubleSpinBox_hipz = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_hipz.setMinimum(-360.0)
        self.doubleSpinBox_hipz.setMaximum(360.0)
        self.doubleSpinBox_hipz.setObjectName("doubleSpinBox_hipz")
        self.horizontalLayout_13.addWidget(self.doubleSpinBox_hipz)
        self.formLayout_5.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout_13)
        self.label_22 = QtGui.QLabel(self.page)
        self.label_22.setObjectName("label_22")
        self.formLayout_5.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_22)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.doubleSpinBox_kneex = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_kneex.setMinimum(-180.0)
        self.doubleSpinBox_kneex.setMaximum(180.0)
        self.doubleSpinBox_kneex.setObjectName("doubleSpinBox_kneex")
        self.horizontalLayout_14.addWidget(self.doubleSpinBox_kneex)
        self.doubleSpinBox_kneey = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_kneey.setMinimum(-180.0)
        self.doubleSpinBox_kneey.setMaximum(180.0)
        self.doubleSpinBox_kneey.setObjectName("doubleSpinBox_kneey")
        self.horizontalLayout_14.addWidget(self.doubleSpinBox_kneey)
        self.doubleSpinBox_kneez = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_kneez.setMinimum(-180.0)
        self.doubleSpinBox_kneez.setMaximum(180.0)
        self.doubleSpinBox_kneez.setObjectName("doubleSpinBox_kneez")
        self.horizontalLayout_14.addWidget(self.doubleSpinBox_kneez)
        self.formLayout_5.setLayout(6, QtGui.QFormLayout.FieldRole, self.horizontalLayout_14)
        self.doubleSpinBox_scaling = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_scaling.setMinimum(-5.0)
        self.doubleSpinBox_scaling.setMaximum(5.0)
        self.doubleSpinBox_scaling.setSingleStep(0.1)
        self.doubleSpinBox_scaling.setObjectName("doubleSpinBox_scaling")
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.FieldRole, self.doubleSpinBox_scaling)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.doubleSpinBox_pc1 = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_pc1.setMinimum(-99.0)
        self.doubleSpinBox_pc1.setMaximum(99.0)
        self.doubleSpinBox_pc1.setSingleStep(0.1)
        self.doubleSpinBox_pc1.setObjectName("doubleSpinBox_pc1")
        self.gridLayout_3.addWidget(self.doubleSpinBox_pc1, 1, 1, 1, 1)
        self.doubleSpinBox_pc4 = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_pc4.setMinimum(-99.0)
        self.doubleSpinBox_pc4.setMaximum(99.0)
        self.doubleSpinBox_pc4.setSingleStep(0.1)
        self.doubleSpinBox_pc4.setObjectName("doubleSpinBox_pc4")
        self.gridLayout_3.addWidget(self.doubleSpinBox_pc4, 2, 3, 1, 1)
        self.doubleSpinBox_pc3 = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_pc3.setMinimum(-99.0)
        self.doubleSpinBox_pc3.setMaximum(99.0)
        self.doubleSpinBox_pc3.setSingleStep(0.1)
        self.doubleSpinBox_pc3.setObjectName("doubleSpinBox_pc3")
        self.gridLayout_3.addWidget(self.doubleSpinBox_pc3, 2, 1, 1, 1)
        self.doubleSpinBox_pc2 = QtGui.QDoubleSpinBox(self.page)
        self.doubleSpinBox_pc2.setMinimum(-99.0)
        self.doubleSpinBox_pc2.setMaximum(99.0)
        self.doubleSpinBox_pc2.setSingleStep(0.1)
        self.doubleSpinBox_pc2.setObjectName("doubleSpinBox_pc2")
        self.gridLayout_3.addWidget(self.doubleSpinBox_pc2, 1, 3, 1, 1)
        self.label = QtGui.QLabel(self.page)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.page)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.page)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 2, 1, 1)
        self.formLayout_5.setLayout(1, QtGui.QFormLayout.FieldRole, self.gridLayout_3)
        self.verticalLayout_5.addLayout(self.formLayout_5)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_manual_reset = QtGui.QPushButton(self.page)
        self.pushButton_manual_reset.setObjectName("pushButton_manual_reset")
        self.horizontalLayout_15.addWidget(self.pushButton_manual_reset)
        self.pushButton_manual_accept = QtGui.QPushButton(self.page)
        self.pushButton_manual_accept.setObjectName("pushButton_manual_accept")
        self.horizontalLayout_15.addWidget(self.pushButton_manual_accept)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)
        self.toolBox.addItem(self.page, "")
        self.page_reg = QtGui.QWidget()
        self.page_reg.setGeometry(QtCore.QRect(0, 0, 382, 388))
        self.page_reg.setObjectName("page_reg")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page_reg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_13 = QtGui.QLabel(self.page_reg)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_13)
        self.label_11 = QtGui.QLabel(self.page_reg)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_11)
        self.spinBox_pcsToFit = QtGui.QSpinBox(self.page_reg)
        self.spinBox_pcsToFit.setObjectName("spinBox_pcsToFit")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinBox_pcsToFit)
        self.label_12 = QtGui.QLabel(self.page_reg)
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_12)
        self.spinBox_mWeight = QtGui.QDoubleSpinBox(self.page_reg)
        self.spinBox_mWeight.setSingleStep(0.1)
        self.spinBox_mWeight.setObjectName("spinBox_mWeight")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinBox_mWeight)
        self.label_6 = QtGui.QLabel(self.page_reg)
        self.label_6.setObjectName("label_6")
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_6)
        self.checkBox_kneecorr = QtGui.QCheckBox(self.page_reg)
        self.checkBox_kneecorr.setText("")
        self.checkBox_kneecorr.setObjectName("checkBox_kneecorr")
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.checkBox_kneecorr)
        self.label_10 = QtGui.QLabel(self.page_reg)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_10)
        self.checkBox_kneedof = QtGui.QCheckBox(self.page_reg)
        self.checkBox_kneedof.setText("")
        self.checkBox_kneedof.setObjectName("checkBox_kneedof")
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.FieldRole, self.checkBox_kneedof)
        self.comboBox_regmode = QtGui.QComboBox(self.page_reg)
        self.comboBox_regmode.setObjectName("comboBox_regmode")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_regmode)
        self.verticalLayout_2.addLayout(self.formLayout_4)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_auto_reg = QtGui.QPushButton(self.page_reg)
        self.pushButton_auto_reg.setObjectName("pushButton_auto_reg")
        self.gridLayout_2.addWidget(self.pushButton_auto_reg, 0, 0, 1, 1)
        self.pushButton_auto_abort = QtGui.QPushButton(self.page_reg)
        self.pushButton_auto_abort.setObjectName("pushButton_auto_abort")
        self.gridLayout_2.addWidget(self.pushButton_auto_abort, 1, 0, 1, 1)
        self.pushButton_auto_reset = QtGui.QPushButton(self.page_reg)
        self.pushButton_auto_reset.setObjectName("pushButton_auto_reset")
        self.gridLayout_2.addWidget(self.pushButton_auto_reset, 0, 1, 1, 1)
        self.pushButton_auto_accept = QtGui.QPushButton(self.page_reg)
        self.pushButton_auto_accept.setObjectName("pushButton_auto_accept")
        self.gridLayout_2.addWidget(self.pushButton_auto_accept, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.errorGroup = QtGui.QGroupBox(self.page_reg)
        self.errorGroup.setObjectName("errorGroup")
        self.formLayout_2 = QtGui.QFormLayout(self.errorGroup)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.landmarkErrorLabel = QtGui.QLabel(self.errorGroup)
        self.landmarkErrorLabel.setObjectName("landmarkErrorLabel")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.landmarkErrorLabel)
        self.lineEdit_landmarkError = QtGui.QLineEdit(self.errorGroup)
        self.lineEdit_landmarkError.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_landmarkError.setReadOnly(True)
        self.lineEdit_landmarkError.setObjectName("lineEdit_landmarkError")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_landmarkError)
        self.mDistLabel = QtGui.QLabel(self.errorGroup)
        self.mDistLabel.setObjectName("mDistLabel")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.mDistLabel)
        self.lineEdit_mDist = QtGui.QLineEdit(self.errorGroup)
        self.lineEdit_mDist.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_mDist.setReadOnly(True)
        self.lineEdit_mDist.setObjectName("lineEdit_mDist")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_mDist)
        self.verticalLayout_2.addWidget(self.errorGroup)
        self.toolBox.addItem(self.page_reg, "")
        self.Screenshot = QtGui.QWidget()
        self.Screenshot.setGeometry(QtCore.QRect(0, 0, 382, 388))
        self.Screenshot.setObjectName("Screenshot")
        self.formLayout = QtGui.QFormLayout(self.Screenshot)
        self.formLayout.setObjectName("formLayout")
        self.pixelsXLabel = QtGui.QLabel(self.Screenshot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixelsXLabel.sizePolicy().hasHeightForWidth())
        self.pixelsXLabel.setSizePolicy(sizePolicy)
        self.pixelsXLabel.setObjectName("pixelsXLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pixelsXLabel)
        self.screenshotPixelXLineEdit = QtGui.QLineEdit(self.Screenshot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshotPixelXLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelXLineEdit.setSizePolicy(sizePolicy)
        self.screenshotPixelXLineEdit.setObjectName("screenshotPixelXLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.screenshotPixelXLineEdit)
        self.pixelsYLabel = QtGui.QLabel(self.Screenshot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixelsYLabel.sizePolicy().hasHeightForWidth())
        self.pixelsYLabel.setSizePolicy(sizePolicy)
        self.pixelsYLabel.setObjectName("pixelsYLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.pixelsYLabel)
        self.screenshotPixelYLineEdit = QtGui.QLineEdit(self.Screenshot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshotPixelYLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotPixelYLineEdit.setSizePolicy(sizePolicy)
        self.screenshotPixelYLineEdit.setObjectName("screenshotPixelYLineEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.screenshotPixelYLineEdit)
        self.screenshotFilenameLabel = QtGui.QLabel(self.Screenshot)
        self.screenshotFilenameLabel.setObjectName("screenshotFilenameLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.screenshotFilenameLabel)
        self.screenshotFilenameLineEdit = QtGui.QLineEdit(self.Screenshot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshotFilenameLineEdit.sizePolicy().hasHeightForWidth())
        self.screenshotFilenameLineEdit.setSizePolicy(sizePolicy)
        self.screenshotFilenameLineEdit.setObjectName("screenshotFilenameLineEdit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.screenshotFilenameLineEdit)
        self.screenshotSaveButton = QtGui.QPushButton(self.Screenshot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenshotSaveButton.sizePolicy().hasHeightForWidth())
        self.screenshotSaveButton.setSizePolicy(sizePolicy)
        self.screenshotSaveButton.setObjectName("screenshotSaveButton")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.screenshotSaveButton)
        self.toolBox.addItem(self.Screenshot, "")
        self.verticalLayout_3.addWidget(self.toolBox)
        self.gridLayout.addWidget(self.widget1, 0, 0, 1, 1)
        self.MayaviScene = MayaviSceneWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.MayaviScene.sizePolicy().hasHeightForWidth())
        self.MayaviScene.setSizePolicy(sizePolicy)
        self.MayaviScene.setObjectName("MayaviScene")
        self.gridLayout.addWidget(self.MayaviScene, 0, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget)

        self.retranslateUi(Dialog)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tableWidget, self.screenshotPixelXLineEdit)
        Dialog.setTabOrder(self.screenshotPixelXLineEdit, self.screenshotPixelYLineEdit)
        Dialog.setTabOrder(self.screenshotPixelYLineEdit, self.screenshotFilenameLineEdit)
        Dialog.setTabOrder(self.screenshotFilenameLineEdit, self.screenshotSaveButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Lower Limb Registration", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog", "Visible", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "RASIS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "LASIS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Sacral", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Lateral Epicondyle", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Dialog", "Medial Epicondyle", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Dialog", "Lateral Malleolus", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Dialog", "Medial Malleolus", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("Dialog", "Marker Radius", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("Dialog", "Skin Padding", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("Dialog", "Landmarks", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Dialog", "Shape Modes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Dialog", "Scaling:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Dialog", "Pelvis Trans.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Dialog", "Pelvis Rot.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("Dialog", "Hip Rot.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("Dialog", "Knee Rot.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_manual_reset.setText(QtGui.QApplication.translate("Dialog", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_manual_accept.setText(QtGui.QApplication.translate("Dialog", "Accept", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("Dialog", "Manual Registration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Dialog", "Registration Mode:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "PCs to Fit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog", "Mahalanobis Weight:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Correct Knee Abd.:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Fit Knee Abd.:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_auto_reg.setText(QtGui.QApplication.translate("Dialog", "Register", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_auto_abort.setText(QtGui.QApplication.translate("Dialog", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_auto_reset.setText(QtGui.QApplication.translate("Dialog", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_auto_accept.setText(QtGui.QApplication.translate("Dialog", "Accept", None, QtGui.QApplication.UnicodeUTF8))
        self.errorGroup.setTitle(QtGui.QApplication.translate("Dialog", "Registration Results", None, QtGui.QApplication.UnicodeUTF8))
        self.landmarkErrorLabel.setText(QtGui.QApplication.translate("Dialog", "Landmark Error (mm RMS):", None, QtGui.QApplication.UnicodeUTF8))
        self.mDistLabel.setWhatsThis(QtGui.QApplication.translate("Dialog", "Percentage of landmarks that have converged to their texture match.", None, QtGui.QApplication.UnicodeUTF8))
        self.mDistLabel.setText(QtGui.QApplication.translate("Dialog", "Mahalanobis Distance:", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_reg), QtGui.QApplication.translate("Dialog", "Auto Registration", None, QtGui.QApplication.UnicodeUTF8))
        self.pixelsXLabel.setText(QtGui.QApplication.translate("Dialog", "Pixels X:", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotPixelXLineEdit.setText(QtGui.QApplication.translate("Dialog", "800", None, QtGui.QApplication.UnicodeUTF8))
        self.pixelsYLabel.setText(QtGui.QApplication.translate("Dialog", "Pixels Y:", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotPixelYLineEdit.setText(QtGui.QApplication.translate("Dialog", "600", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotFilenameLabel.setText(QtGui.QApplication.translate("Dialog", "Filename:", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotFilenameLineEdit.setText(QtGui.QApplication.translate("Dialog", "screenshot.png", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshotSaveButton.setText(QtGui.QApplication.translate("Dialog", "Save Screenshot", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Screenshot), QtGui.QApplication.translate("Dialog", "Screenshots", None, QtGui.QApplication.UnicodeUTF8))

from mayaviscenewidget import MayaviSceneWidget
