from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Controller.GestioneContratto import GestioneContratto
from Utils.Const.PathViste import PATH_VISTA_RICEVUTE


class VistaContratto(QDialog):
    def __init__(self):
        super(VistaContratto, self).__init__()
        loadUi(PATH_VISTA_RICEVUTE, self)
        self.gestione_contratti = GestioneContratto()
        self.setup_ui()

    def setup_ui(self):
        self.widget = QtWidgets.QStackedWidget()
        self.back_button.clicked.connect(self.go_back)
        self.listWidget.setStyleSheet("""
                QListView {
                    background-color: rgb(255,255,255);
                    color: rgb(104,0,0);
                    }
                QScrollBar:vertical {              
                    border: none;
                    background:white;
                    width:3px;
                    margin: 0px 0px 0px 0px;
                }
                QScrollBar::handle:vertical {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop: 0 rgb(255,255,255), stop: 0.5 rgb(255,255,255), stop:1 rgb(255,255,255));
                    min-height: 0px;
                }
                QScrollBar::add-line:vertical {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop: 0 rgb(255,255,255), stop: 0.5 rgb(255,255,255),  stop:1 rgb(255,255,255));
                    height: 0px;
                    subcontrol-position: bottom;
                    subcontrol-origin: margin;
                }
                QScrollBar::sub-line:vertical {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop: 0  rgb(38, 157, 206), stop: 0.5 rgb(255,255,255),  stop:1 rgb(255,255,255);
                    height: 0 px;
                    subcontrol-position: top;
                    subcontrol-origin: margin;
                }
            """)
        self.popola_lista_contratti()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def popola_lista_contratti(self):
        contratti = self.gestione_contratti.get_contratti_cliente()
        if contratti is not None:
            self.listWidget.clear()
            self.listWidget.addItems(contratto.__str__() for contratto in contratti)

    def go_back(self):
        self.close()
