from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Utils.Const.PathViste import PATH_VISTA_MODIFICA_MEZZO


class VistaModificaAuto(QDialog):
    closed = pyqtSignal()

    def __init__(self, gestione_auto):
        super().__init__()
        loadUi(PATH_VISTA_MODIFICA_MEZZO, self)
        self.gestione_auto = gestione_auto
        self.setup_ui()

    def setup_ui(self):
        self.disponibile_button.clicked.connect(self.go_disponibile)
        self.non_disponibile_button.clicked.connect(self.go_non_disponibile)
        self.back_button.clicked.connect(self.go_back)
        self.id_label_to_edit.setText(str(self.gestione_auto.auto.id))
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        if self.gestione_auto.auto.get_disponibilita():
            self.disponibile_label_to_edit.setText("Disponibile")
            self.disponibile_button.setChecked(False)
            self.non_disponibile_button.setChecked(True)
        else:
            self.disponibile_label_to_edit.setText("Non Disponibile")
            self.disponibile_button.setChecked(True)
            self.non_disponibile_button.setChecked(False)

    def go_disponibile(self):
        self.gestione_auto.set_disponibilita_auto(True)
        self.disponibile_label_to_edit.setText("Disponibile")
        self.disponibile_button.setChecked(False)
        self.non_disponibile_button.setChecked(True)

    def go_non_disponibile(self):
        self.gestione_auto.set_disponibilita_auto(False)
        self.disponibile_label_to_edit.setText("Non Disponibile")
        self.disponibile_button.setChecked(True)
        self.non_disponibile_button.setChecked(False)

    def go_back(self):
        self.close()

    def closeEvent(self, event):
        self.closed.emit()
