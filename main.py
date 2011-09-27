from PyQt4 import QtCore, QtGui
from ui.main_window import Ui_main_window 
from layer import criteria_layer

class main_window(QtGui.QMainWindow, Ui_main_window):

    def __init__(self, iface):
        super(QtGui.QMainWindow, self).__init__(iface.mainWindow())
        self.setupUi(self)

        self.iface = iface

        self.__update_layer_list(iface.mapCanvas())
        self.table_criteria.connect(self.table_criteria,
                                    QtCore.SIGNAL("criterion_state_changed"),
                                    self.__criterion_state_changed)

    def __update_layer_list(self, map_canvas):
        if map_canvas == None:
            return

        for i in range(map_canvas.layerCount()):
            layer = map_canvas.layer(i)
            self.combo_layer.addItem(layer.name())

    def on_button_loadlayer_pressed(self):
        index = self.combo_layer.currentIndex()
        map_canvas = self.iface.mapCanvas()
        try:
            self.layer = criteria_layer(map_canvas.layer(index))
            self.__loadlayer()
        except:
            QtGui.QMessageBox.information(None, "Error", "Cannot load specified layer")

    def __loadlayer(self):
        self.criteria = self.layer.criteria
        self.table_criteria.add(self.criteria)
        self.table_prof.add_criteria(self.criteria)
        self.table_indiff.add_criteria(self.criteria)
        self.table_pref.add_criteria(self.criteria)
        self.table_veto.add_criteria(self.criteria)

    def __criterion_state_changed(self, criterion):
        for table in [ self.table_prof, self.table_indiff, self.table_pref, self.table_veto ]:
            table.disable_criterion(criterion, criterion.disabled)
