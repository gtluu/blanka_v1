# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blanka_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 551)
        MainWindow.setMinimumSize(QtCore.QSize(621, 551))
        MainWindow.setMaximumSize(QtCore.QSize(621, 551))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sample_label = QtWidgets.QLabel(self.centralwidget)
        self.sample_label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.sample_label.setObjectName("sample_label")
        self.sample_text = QtWidgets.QLineEdit(self.centralwidget)
        self.sample_text.setGeometry(QtCore.QRect(10, 30, 411, 20))
        self.sample_text.setObjectName("sample_text")
        self.sample_file_browser = QtWidgets.QPushButton(self.centralwidget)
        self.sample_file_browser.setGeometry(QtCore.QRect(440, 30, 31, 23))
        self.sample_file_browser.setObjectName("sample_file_browser")
        self.num_samples = QtWidgets.QCheckBox(self.centralwidget)
        self.num_samples.setGeometry(QtCore.QRect(490, 30, 121, 21))
        self.num_samples.setObjectName("num_samples")
        self.control_text = QtWidgets.QLineEdit(self.centralwidget)
        self.control_text.setGeometry(QtCore.QRect(10, 90, 411, 20))
        self.control_text.setObjectName("control_text")
        self.control_label = QtWidgets.QLabel(self.centralwidget)
        self.control_label.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.control_label.setObjectName("control_label")
        self.control_file_browser = QtWidgets.QPushButton(self.centralwidget)
        self.control_file_browser.setGeometry(QtCore.QRect(440, 90, 31, 23))
        self.control_file_browser.setObjectName("control_file_browser")
        self.num_controls = QtWidgets.QCheckBox(self.centralwidget)
        self.num_controls.setGeometry(QtCore.QRect(490, 90, 121, 21))
        self.num_controls.setObjectName("num_controls")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(10, 130, 141, 16))
        self.output_label.setObjectName("output_label")
        self.output_text = QtWidgets.QLineEdit(self.centralwidget)
        self.output_text.setGeometry(QtCore.QRect(10, 150, 411, 20))
        self.output_text.setObjectName("output_text")
        self.output_file_browser = QtWidgets.QPushButton(self.centralwidget)
        self.output_file_browser.setGeometry(QtCore.QRect(440, 150, 31, 23))
        self.output_file_browser.setObjectName("output_file_browser")
        self.instrument_label = QtWidgets.QLabel(self.centralwidget)
        self.instrument_label.setGeometry(QtCore.QRect(10, 190, 71, 21))
        self.instrument_label.setObjectName("instrument_label")
        self.instrument_choice = QtWidgets.QComboBox(self.centralwidget)
        self.instrument_choice.setGeometry(QtCore.QRect(90, 190, 161, 22))
        self.instrument_choice.setObjectName("instrument_choice")
        self.instrument_choice.addItem("")
        self.instrument_choice.addItem("")
        self.instrument_choice.addItem("")
        self.ms1_threshold_label = QtWidgets.QLabel(self.centralwidget)
        self.ms1_threshold_label.setGeometry(QtCore.QRect(10, 230, 251, 21))
        self.ms1_threshold_label.setObjectName("ms1_threshold_label")
        self.ms1_threshold_text = QtWidgets.QLineEdit(self.centralwidget)
        self.ms1_threshold_text.setGeometry(QtCore.QRect(260, 230, 51, 21))
        self.ms1_threshold_text.setObjectName("ms1_threshold_text")
        self.ms2_threshold_text = QtWidgets.QLineEdit(self.centralwidget)
        self.ms2_threshold_text.setGeometry(QtCore.QRect(260, 270, 51, 20))
        self.ms2_threshold_text.setText("")
        self.ms2_threshold_text.setObjectName("ms2_threshold_text")
        self.ms2_threshold_label = QtWidgets.QLabel(self.centralwidget)
        self.ms2_threshold_label.setGeometry(QtCore.QRect(10, 270, 251, 21))
        self.ms2_threshold_label.setObjectName("ms2_threshold_label")
        self.snr_label = QtWidgets.QLabel(self.centralwidget)
        self.snr_label.setGeometry(QtCore.QRect(10, 310, 111, 21))
        self.snr_label.setObjectName("snr_label")
        self.snr_text = QtWidgets.QLineEdit(self.centralwidget)
        self.snr_text.setGeometry(QtCore.QRect(120, 310, 51, 20))
        self.snr_text.setText("")
        self.snr_text.setObjectName("snr_text")
        self.snr_unit = QtWidgets.QLabel(self.centralwidget)
        self.snr_unit.setGeometry(QtCore.QRect(180, 310, 21, 21))
        self.snr_unit.setObjectName("snr_unit")
        self.rt_label = QtWidgets.QLabel(self.centralwidget)
        self.rt_label.setGeometry(QtCore.QRect(10, 350, 151, 21))
        self.rt_label.setObjectName("rt_label")
        self.rt_unit = QtWidgets.QLabel(self.centralwidget)
        self.rt_unit.setGeometry(QtCore.QRect(230, 350, 21, 21))
        self.rt_unit.setObjectName("rt_unit")
        self.rt_text = QtWidgets.QLineEdit(self.centralwidget)
        self.rt_text.setGeometry(QtCore.QRect(170, 350, 51, 20))
        self.rt_text.setText("")
        self.rt_text.setObjectName("rt_text")
        self.precursor_mz_label = QtWidgets.QLabel(self.centralwidget)
        self.precursor_mz_label.setGeometry(QtCore.QRect(10, 390, 151, 21))
        self.precursor_mz_label.setObjectName("precursor_mz_label")
        self.precursor_mz_text = QtWidgets.QLineEdit(self.centralwidget)
        self.precursor_mz_text.setGeometry(QtCore.QRect(160, 390, 51, 20))
        self.precursor_mz_text.setText("")
        self.precursor_mz_text.setObjectName("precursor_mz_text")
        self.precursor_mz_unit = QtWidgets.QLabel(self.centralwidget)
        self.precursor_mz_unit.setGeometry(QtCore.QRect(220, 390, 21, 21))
        self.precursor_mz_unit.setObjectName("precursor_mz_unit")
        self.peak_mz_label = QtWidgets.QLabel(self.centralwidget)
        self.peak_mz_label.setGeometry(QtCore.QRect(10, 430, 121, 21))
        self.peak_mz_label.setObjectName("peak_mz_label")
        self.peak_mz_unit = QtWidgets.QLabel(self.centralwidget)
        self.peak_mz_unit.setGeometry(QtCore.QRect(200, 430, 21, 21))
        self.peak_mz_unit.setObjectName("peak_mz_unit")
        self.peak_mz_text = QtWidgets.QLineEdit(self.centralwidget)
        self.peak_mz_text.setGeometry(QtCore.QRect(140, 430, 51, 20))
        self.peak_mz_text.setText("")
        self.peak_mz_text.setObjectName("peak_mz_text")
        self.noise_removal_only = QtWidgets.QCheckBox(self.centralwidget)
        self.noise_removal_only.setGeometry(QtCore.QRect(370, 310, 121, 21))
        self.noise_removal_only.setObjectName("noise_removal_only")
        self.blank_removal_only = QtWidgets.QCheckBox(self.centralwidget)
        self.blank_removal_only.setGeometry(QtCore.QRect(370, 350, 121, 21))
        self.blank_removal_only.setObjectName("blank_removal_only")
        self.verbose = QtWidgets.QCheckBox(self.centralwidget)
        self.verbose.setGeometry(QtCore.QRect(370, 390, 121, 21))
        self.verbose.setObjectName("verbose")
        self.advanced_options_label = QtWidgets.QLabel(self.centralwidget)
        self.advanced_options_label.setGeometry(QtCore.QRect(10, 470, 91, 16))
        self.advanced_options_label.setObjectName("advanced_options_label")
        self.cpu_text = QtWidgets.QLineEdit(self.centralwidget)
        self.cpu_text.setGeometry(QtCore.QRect(170, 490, 51, 20))
        self.cpu_text.setText("")
        self.cpu_text.setObjectName("cpu_text")
        self.cpu_label = QtWidgets.QLabel(self.centralwidget)
        self.cpu_label.setGeometry(QtCore.QRect(10, 490, 161, 21))
        self.cpu_label.setObjectName("cpu_label")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(520, 490, 75, 23))
        self.start.setObjectName("start")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sample_label.setText(_translate("MainWindow", "Sample"))
        self.sample_file_browser.setText(_translate("MainWindow", "..."))
        self.num_samples.setText(_translate("MainWindow", "Multiple Sample Files"))
        self.control_label.setText(_translate("MainWindow", "Control"))
        self.control_file_browser.setText(_translate("MainWindow", "..."))
        self.num_controls.setText(_translate("MainWindow", "Multiple Control Files"))
        self.output_label.setText(_translate("MainWindow", "Output Directory (Optional)"))
        self.output_file_browser.setText(_translate("MainWindow", "..."))
        self.instrument_label.setText(_translate("MainWindow", "Experiment"))
        self.instrument_choice.setItemText(0, _translate("MainWindow", "LC-MS or LC-MS/MS (LCQ)"))
        self.instrument_choice.setItemText(1, _translate("MainWindow", "LC-MS or LC-MS/MS (qTOF)"))
        self.instrument_choice.setItemText(2, _translate("MainWindow", "MALDI Dried Droplet"))
        self.ms1_threshold_label.setText(_translate("MainWindow", "Blank Removal Relative Intensity Threshold (MS1):"))
        self.ms2_threshold_label.setText(_translate("MainWindow", "Blank Removal Relative Intensity Threshold (MS2):"))
        self.snr_label.setText(_translate("MainWindow", "Signal to Noise Ratio:"))
        self.snr_unit.setText(_translate("MainWindow", ": 1"))
        self.rt_label.setText(_translate("MainWindow", "Retention Time Tolerance: +/-"))
        self.rt_unit.setText(_translate("MainWindow", "sec"))
        self.precursor_mz_label.setText(_translate("MainWindow", "Precursor m/z Tolerance: +/-"))
        self.precursor_mz_unit.setText(_translate("MainWindow", "Da"))
        self.peak_mz_label.setText(_translate("MainWindow", "Peak m/z Tolerance: +/-"))
        self.peak_mz_unit.setText(_translate("MainWindow", "Da"))
        self.noise_removal_only.setText(_translate("MainWindow", "Noise Removal Only"))
        self.blank_removal_only.setText(_translate("MainWindow", "Blank Removal Only"))
        self.verbose.setText(_translate("MainWindow", "Verbose"))
        self.advanced_options_label.setText(_translate("MainWindow", "Advanced Options"))
        self.cpu_label.setText(_translate("MainWindow", "Number of CPU Threads to Use:"))
        self.start.setText(_translate("MainWindow", "Run"))

