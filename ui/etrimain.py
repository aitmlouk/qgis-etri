# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/etrimain.ui'
#
# Created: Sun Sep 18 15:21:41 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EtriMainWindow(object):
    def setupUi(self, EtriMainWindow):
        EtriMainWindow.setObjectName(_fromUtf8("EtriMainWindow"))
        EtriMainWindow.resize(800, 606)
        EtriMainWindow.setWindowTitle(QtGui.QApplication.translate("EtriMainWindow", "Electre Tri", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(EtriMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Tab_params = QtGui.QTabWidget(self.centralwidget)
        self.Tab_params.setObjectName(_fromUtf8("Tab_params"))
        self.tab_criteria = QtGui.QWidget()
        self.tab_criteria.setObjectName(_fromUtf8("tab_criteria"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_criteria)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.table_crit = QtGui.QTableWidget(self.tab_criteria)
        self.table_crit.setDragEnabled(False)
        self.table_crit.setAlternatingRowColors(False)
        self.table_crit.setShowGrid(False)
        self.table_crit.setCornerButtonEnabled(False)
        self.table_crit.setRowCount(0)
        self.table_crit.setObjectName(_fromUtf8("table_crit"))
        self.table_crit.setColumnCount(3)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("EtriMainWindow", "Criterion", None, QtGui.QApplication.UnicodeUTF8))
        self.table_crit.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_crit.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("EtriMainWindow", "Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.table_crit.setHorizontalHeaderItem(2, item)
        self.table_crit.horizontalHeader().setVisible(False)
        self.table_crit.horizontalHeader().setDefaultSectionSize(100)
        self.table_crit.horizontalHeader().setHighlightSections(False)
        self.table_crit.verticalHeader().setVisible(False)
        self.table_crit.verticalHeader().setHighlightSections(False)
        self.table_crit.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout_2.addWidget(self.table_crit, 0, 0, 1, 1)
        self.Tab_params.addTab(self.tab_criteria, _fromUtf8(""))
        self.tab_profiles = QtGui.QWidget()
        self.tab_profiles.setObjectName(_fromUtf8("tab_profiles"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_profiles)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.table_prof = QtGui.QTableWidget(self.tab_profiles)
        self.table_prof.setObjectName(_fromUtf8("table_prof"))
        self.table_prof.setColumnCount(0)
        self.table_prof.setRowCount(0)
        self.gridLayout_5.addWidget(self.table_prof, 0, 0, 1, 1)
        self.tab_thresholds = QtGui.QTabWidget(self.tab_profiles)
        self.tab_thresholds.setTabPosition(QtGui.QTabWidget.North)
        self.tab_thresholds.setTabShape(QtGui.QTabWidget.Rounded)
        self.tab_thresholds.setObjectName(_fromUtf8("tab_thresholds"))
        self.tab_indiff = QtGui.QWidget()
        self.tab_indiff.setObjectName(_fromUtf8("tab_indiff"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_indiff)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.table_indiff = QtGui.QTableWidget(self.tab_indiff)
        self.table_indiff.setObjectName(_fromUtf8("table_indiff"))
        self.table_indiff.setColumnCount(0)
        self.table_indiff.setRowCount(0)
        self.gridLayout_3.addWidget(self.table_indiff, 0, 1, 1, 1)
        self.tab_thresholds.addTab(self.tab_indiff, _fromUtf8(""))
        self.tab_pref = QtGui.QWidget()
        self.tab_pref.setObjectName(_fromUtf8("tab_pref"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_pref)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.table_pref = QtGui.QTableWidget(self.tab_pref)
        self.table_pref.setObjectName(_fromUtf8("table_pref"))
        self.table_pref.setColumnCount(0)
        self.table_pref.setRowCount(0)
        self.gridLayout_4.addWidget(self.table_pref, 0, 0, 1, 1)
        self.tab_thresholds.addTab(self.tab_pref, _fromUtf8(""))
        self.tab_veto = QtGui.QWidget()
        self.tab_veto.setObjectName(_fromUtf8("tab_veto"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_veto)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.table_veto = QtGui.QTableWidget(self.tab_veto)
        self.table_veto.setObjectName(_fromUtf8("table_veto"))
        self.table_veto.setColumnCount(0)
        self.table_veto.setRowCount(0)
        self.gridLayout_7.addWidget(self.table_veto, 0, 0, 1, 1)
        self.tab_thresholds.addTab(self.tab_veto, _fromUtf8(""))
        self.gridLayout_5.addWidget(self.tab_thresholds, 1, 0, 1, 1)
        self.Tab_params.addTab(self.tab_profiles, _fromUtf8(""))
        self.tab_plot = QtGui.QWidget()
        self.tab_plot.setObjectName(_fromUtf8("tab_plot"))
        self.gridLayout_10 = QtGui.QGridLayout(self.tab_plot)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.graph_plot = mygraphicsview(self.tab_plot)
        self.graph_plot.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graph_plot.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graph_plot.setAlignment(QtCore.Qt.AlignCenter)
        self.graph_plot.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing)
        self.graph_plot.setObjectName(_fromUtf8("graph_plot"))
        self.gridLayout_10.addWidget(self.graph_plot, 0, 0, 1, 1)
        self.Tab_params.addTab(self.tab_plot, _fromUtf8(""))
        self.tab_inference = QtGui.QWidget()
        self.tab_inference.setObjectName(_fromUtf8("tab_inference"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_inference)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.group_refs = QtGui.QGroupBox(self.tab_inference)
        self.group_refs.setTitle(QtGui.QApplication.translate("EtriMainWindow", "Reference actions", None, QtGui.QApplication.UnicodeUTF8))
        self.group_refs.setObjectName(_fromUtf8("group_refs"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.group_refs)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.table_refs = QtGui.QTableWidget(self.group_refs)
        self.table_refs.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_refs.setObjectName(_fromUtf8("table_refs"))
        self.table_refs.setColumnCount(1)
        self.table_refs.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("EtriMainWindow", "Category", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table_refs.setHorizontalHeaderItem(0, item)
        self.verticalLayout_3.addWidget(self.table_refs)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Bchooserefs = QtGui.QPushButton(self.group_refs)
        self.Bchooserefs.setEnabled(False)
        self.Bchooserefs.setText(QtGui.QApplication.translate("EtriMainWindow", "Choose reference actions", None, QtGui.QApplication.UnicodeUTF8))
        self.Bchooserefs.setObjectName(_fromUtf8("Bchooserefs"))
        self.horizontalLayout.addWidget(self.Bchooserefs)
        self.Binfer = QtGui.QPushButton(self.group_refs)
        self.Binfer.setEnabled(False)
        self.Binfer.setText(QtGui.QApplication.translate("EtriMainWindow", "Infer parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.Binfer.setObjectName(_fromUtf8("Binfer"))
        self.horizontalLayout.addWidget(self.Binfer)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout_6.addWidget(self.group_refs, 1, 0, 1, 1)
        self.group_infparams = QtGui.QGroupBox(self.tab_inference)
        self.group_infparams.setTitle(QtGui.QApplication.translate("EtriMainWindow", "Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.group_infparams.setObjectName(_fromUtf8("group_infparams"))
        self.verticalLayout = QtGui.QVBoxLayout(self.group_infparams)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.model_layout = QtGui.QHBoxLayout()
        self.model_layout.setObjectName(_fromUtf8("model_layout"))
        self.label_combo = QtGui.QLabel(self.group_infparams)
        self.label_combo.setText(QtGui.QApplication.translate("EtriMainWindow", "Electre Tri model:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_combo.setObjectName(_fromUtf8("label_combo"))
        self.model_layout.addWidget(self.label_combo)
        self.combo_model = QtGui.QComboBox(self.group_infparams)
        self.combo_model.setObjectName(_fromUtf8("combo_model"))
        self.combo_model.addItem(_fromUtf8(""))
        self.combo_model.setItemText(0, QtGui.QApplication.translate("EtriMainWindow", "Bouyssou-Marchant (Pessimistic)", None, QtGui.QApplication.UnicodeUTF8))
        self.model_layout.addWidget(self.combo_model)
        self.verticalLayout.addLayout(self.model_layout)
        self.inference_layout = QtGui.QHBoxLayout()
        self.inference_layout.setObjectName(_fromUtf8("inference_layout"))
        self.label_inference = QtGui.QLabel(self.group_infparams)
        self.label_inference.setText(QtGui.QApplication.translate("EtriMainWindow", "Inference:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_inference.setObjectName(_fromUtf8("label_inference"))
        self.inference_layout.addWidget(self.label_inference)
        self.combo_inference = QtGui.QComboBox(self.group_infparams)
        self.combo_inference.setObjectName(_fromUtf8("combo_inference"))
        self.combo_inference.addItem(_fromUtf8(""))
        self.combo_inference.setItemText(0, QtGui.QApplication.translate("EtriMainWindow", "Global", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_inference.addItem(_fromUtf8(""))
        self.combo_inference.setItemText(1, QtGui.QApplication.translate("EtriMainWindow", "Profiles", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_inference.addItem(_fromUtf8(""))
        self.combo_inference.setItemText(2, QtGui.QApplication.translate("EtriMainWindow", "Weights and lambda", None, QtGui.QApplication.UnicodeUTF8))
        self.inference_layout.addWidget(self.combo_inference)
        self.verticalLayout.addLayout(self.inference_layout)
        self.gridLayout_6.addWidget(self.group_infparams, 0, 0, 1, 1)
        self.Tab_params.addTab(self.tab_inference, _fromUtf8(""))
        self.gridLayout.addWidget(self.Tab_params, 0, 0, 1, 1)
        self.right_layout = QtGui.QVBoxLayout()
        self.right_layout.setObjectName(_fromUtf8("right_layout"))
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.right_layout.addItem(spacerItem)
        self.group_options = QtGui.QGroupBox(self.centralwidget)
        self.group_options.setTitle(QtGui.QApplication.translate("EtriMainWindow", "XMCDA", None, QtGui.QApplication.UnicodeUTF8))
        self.group_options.setObjectName(_fromUtf8("group_options"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.group_options)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Bloadxmcda = QtGui.QPushButton(self.group_options)
        self.Bloadxmcda.setEnabled(False)
        self.Bloadxmcda.setText(QtGui.QApplication.translate("EtriMainWindow", "Load parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.Bloadxmcda.setObjectName(_fromUtf8("Bloadxmcda"))
        self.verticalLayout_2.addWidget(self.Bloadxmcda)
        self.Bsavexmcda = QtGui.QPushButton(self.group_options)
        self.Bsavexmcda.setEnabled(False)
        self.Bsavexmcda.setText(QtGui.QApplication.translate("EtriMainWindow", "Save parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.Bsavexmcda.setObjectName(_fromUtf8("Bsavexmcda"))
        self.verticalLayout_2.addWidget(self.Bsavexmcda)
        self.right_layout.addWidget(self.group_options)
        self.group_input = QtGui.QGroupBox(self.centralwidget)
        self.group_input.setTitle(QtGui.QApplication.translate("EtriMainWindow", "Input Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.group_input.setObjectName(_fromUtf8("group_input"))
        self.gridLayout_9 = QtGui.QGridLayout(self.group_input)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.combo_layer = QtGui.QComboBox(self.group_input)
        self.combo_layer.setObjectName(_fromUtf8("combo_layer"))
        self.gridLayout_9.addWidget(self.combo_layer, 0, 0, 1, 1)
        self.Bloadlayer = QtGui.QPushButton(self.group_input)
        self.Bloadlayer.setText(QtGui.QApplication.translate("EtriMainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.Bloadlayer.setObjectName(_fromUtf8("Bloadlayer"))
        self.gridLayout_9.addWidget(self.Bloadlayer, 0, 1, 1, 1)
        self.right_layout.addWidget(self.group_input)
        self.group_profiles = QtGui.QGroupBox(self.centralwidget)
        self.group_profiles.setTitle(QtGui.QApplication.translate("EtriMainWindow", "Categories", None, QtGui.QApplication.UnicodeUTF8))
        self.group_profiles.setObjectName(_fromUtf8("group_profiles"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.group_profiles)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Badd_profile = QtGui.QPushButton(self.group_profiles)
        self.Badd_profile.setEnabled(False)
        self.Badd_profile.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/etri/images/plus.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Badd_profile.setIcon(icon)
        self.Badd_profile.setObjectName(_fromUtf8("Badd_profile"))
        self.horizontalLayout_2.addWidget(self.Badd_profile)
        self.label_ncategories = QtGui.QLabel(self.group_profiles)
        self.label_ncategories.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_ncategories.setText(_fromUtf8("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">-</span></p></body></html>"))
        self.label_ncategories.setObjectName(_fromUtf8("label_ncategories"))
        self.horizontalLayout_2.addWidget(self.label_ncategories)
        self.Bdel_profile = QtGui.QPushButton(self.group_profiles)
        self.Bdel_profile.setEnabled(False)
        self.Bdel_profile.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/etri/images/min.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Bdel_profile.setIcon(icon1)
        self.Bdel_profile.setObjectName(_fromUtf8("Bdel_profile"))
        self.horizontalLayout_2.addWidget(self.Bdel_profile)
        self.right_layout.addWidget(self.group_profiles)
        self.group_thresholds = QtGui.QGroupBox(self.centralwidget)
        self.group_thresholds.setMaximumSize(QtCore.QSize(388, 16777215))
        self.group_thresholds.setTitle(QtGui.QApplication.translate("EtriMainWindow", "Thresholds", None, QtGui.QApplication.UnicodeUTF8))
        self.group_thresholds.setObjectName(_fromUtf8("group_thresholds"))
        self.formLayout = QtGui.QFormLayout(self.group_thresholds)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.cbox_samethresholds = QtGui.QCheckBox(self.group_thresholds)
        self.cbox_samethresholds.setText(QtGui.QApplication.translate("EtriMainWindow", "Use same for all profiles", None, QtGui.QApplication.UnicodeUTF8))
        self.cbox_samethresholds.setObjectName(_fromUtf8("cbox_samethresholds"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.cbox_samethresholds)
        self.cbox_noveto = QtGui.QCheckBox(self.group_thresholds)
        self.cbox_noveto.setText(QtGui.QApplication.translate("EtriMainWindow", "No Veto", None, QtGui.QApplication.UnicodeUTF8))
        self.cbox_noveto.setObjectName(_fromUtf8("cbox_noveto"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.cbox_noveto)
        self.cbox_sameqp = QtGui.QCheckBox(self.group_thresholds)
        self.cbox_sameqp.setText(QtGui.QApplication.translate("EtriMainWindow", "Indifference = Preference", None, QtGui.QApplication.UnicodeUTF8))
        self.cbox_sameqp.setObjectName(_fromUtf8("cbox_sameqp"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.cbox_sameqp)
        self.right_layout.addWidget(self.group_thresholds)
        self.group_affectation = QtGui.QGroupBox(self.centralwidget)
        self.group_affectation.setTitle(QtGui.QApplication.translate("EtriMainWindow", "Affectation", None, QtGui.QApplication.UnicodeUTF8))
        self.group_affectation.setObjectName(_fromUtf8("group_affectation"))
        self.gridLayout_8 = QtGui.QGridLayout(self.group_affectation)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.cutlevel_layout = QtGui.QHBoxLayout()
        self.cutlevel_layout.setObjectName(_fromUtf8("cutlevel_layout"))
        self.label_cutlevel = QtGui.QLabel(self.group_affectation)
        self.label_cutlevel.setText(QtGui.QApplication.translate("EtriMainWindow", "Cutting level:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cutlevel.setObjectName(_fromUtf8("label_cutlevel"))
        self.cutlevel_layout.addWidget(self.label_cutlevel)
        self.spinbox_cutlevel = QtGui.QDoubleSpinBox(self.group_affectation)
        self.spinbox_cutlevel.setMinimum(0.5)
        self.spinbox_cutlevel.setMaximum(1.0)
        self.spinbox_cutlevel.setSingleStep(0.01)
        self.spinbox_cutlevel.setProperty("value", 0.75)
        self.spinbox_cutlevel.setObjectName(_fromUtf8("spinbox_cutlevel"))
        self.cutlevel_layout.addWidget(self.spinbox_cutlevel)
        self.gridLayout_8.addLayout(self.cutlevel_layout, 0, 0, 1, 1)
        self.procedure_layout = QtGui.QHBoxLayout()
        self.procedure_layout.setObjectName(_fromUtf8("procedure_layout"))
        self.label_procedure = QtGui.QLabel(self.group_affectation)
        self.label_procedure.setText(QtGui.QApplication.translate("EtriMainWindow", "Procedure:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_procedure.setObjectName(_fromUtf8("label_procedure"))
        self.procedure_layout.addWidget(self.label_procedure)
        self.combo_procedure = QtGui.QComboBox(self.group_affectation)
        self.combo_procedure.setObjectName(_fromUtf8("combo_procedure"))
        self.combo_procedure.addItem(_fromUtf8(""))
        self.combo_procedure.setItemText(0, QtGui.QApplication.translate("EtriMainWindow", "Pessimistic", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_procedure.addItem(_fromUtf8(""))
        self.combo_procedure.setItemText(1, QtGui.QApplication.translate("EtriMainWindow", "Optimistic", None, QtGui.QApplication.UnicodeUTF8))
        self.procedure_layout.addWidget(self.combo_procedure)
        self.gridLayout_8.addLayout(self.procedure_layout, 1, 0, 1, 1)
        self.right_layout.addWidget(self.group_affectation)
        self.Bgenerate = QtGui.QPushButton(self.centralwidget)
        self.Bgenerate.setEnabled(False)
        self.Bgenerate.setText(QtGui.QApplication.translate("EtriMainWindow", "Generate Decision Map", None, QtGui.QApplication.UnicodeUTF8))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/etri/images/etri.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Bgenerate.setIcon(icon2)
        self.Bgenerate.setObjectName(_fromUtf8("Bgenerate"))
        self.right_layout.addWidget(self.Bgenerate)
        self.gridLayout.addLayout(self.right_layout, 0, 1, 1, 1)
        EtriMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(EtriMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        EtriMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(EtriMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        EtriMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EtriMainWindow)
        self.Tab_params.setCurrentIndex(0)
        self.tab_thresholds.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(EtriMainWindow)

    def retranslateUi(self, EtriMainWindow):
        item = self.table_crit.horizontalHeaderItem(0)
        item = self.table_crit.horizontalHeaderItem(2)
        self.Tab_params.setTabText(self.Tab_params.indexOf(self.tab_criteria), QtGui.QApplication.translate("EtriMainWindow", "Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_thresholds.setTabText(self.tab_thresholds.indexOf(self.tab_indiff), QtGui.QApplication.translate("EtriMainWindow", "Indifference", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_thresholds.setTabText(self.tab_thresholds.indexOf(self.tab_pref), QtGui.QApplication.translate("EtriMainWindow", "Preference", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_thresholds.setTabText(self.tab_thresholds.indexOf(self.tab_veto), QtGui.QApplication.translate("EtriMainWindow", "Veto", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab_params.setTabText(self.Tab_params.indexOf(self.tab_profiles), QtGui.QApplication.translate("EtriMainWindow", "Profiles", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab_params.setTabText(self.Tab_params.indexOf(self.tab_plot), QtGui.QApplication.translate("EtriMainWindow", "Model plot", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table_refs.horizontalHeaderItem(0)
        self.Tab_params.setTabText(self.Tab_params.indexOf(self.tab_inference), QtGui.QApplication.translate("EtriMainWindow", "Inference", None, QtGui.QApplication.UnicodeUTF8))

from graphic import mygraphicsview
import resources_rc