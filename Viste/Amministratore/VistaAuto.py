from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Controller.GestioneAuto import  GestioneAuto
from Utils.Const.PathViste import PATH_VISTA_MEZZI
from Viste.Amministratore.VistaModificaAuto import VistaModificaAuto


class VistaAuto(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(PATH_VISTA_MEZZI, self)
        self.gestione_auto = GestioneAuto()
        self.id_auto = None
        self.lista_veicoli = {}
        self.setup_ui()

    def setup_ui(self):
        self.widget = QtWidgets.QStackedWidget()
        self.bottone_crea_mezzo.clicked.connect(self.go_aggiungi_auto)
        self.bottone_elimina_mezzo.clicked.connect(self.go_elimina_auto)
        self.bottone_modifica_mezzo.clicked.connect(self.go_modifica_auto)
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
                    stop: 0  rgb(255,255,255), stop: 0.5 rgb(255,255,255),  stop:1 rgb(255,255,255));
                    height: 0 px;
                    subcontrol-position: top;
                    subcontrol-origin: margin;
                }
            """)
        self.popola_lista_veicoli()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def popola_lista_veicoli(self):
        self.listWidget.clear()
        self.lista_veicoli=self.gestione_auto.get_all_veicoli()
        if len(self.lista_veicoli) > 0:
            self.listWidget.addItems(auto.__str__() for auto in self.lista_veicoli.values())
            self.listWidget.clicked.connect(self.seleziona_auto)

    # 1. preleva il numero di riga cliccata
    # 2. prelevo le chiavi dal dizionario self.lista_monopattini
    # 3. interccetto la chiave da cercare che si trova nella posizione "riga"
    # 4. prelevo i dati relativi al monopattino
    # 5. salvo l'id del monopattino selezionato
    def seleziona_auto(self):
        riga = self.listWidget.currentRow()
        keys = list(self.lista_veicoli.keys())
        da_cercare = keys[riga]
        auto = self.lista_veicoli.get(da_cercare)
        self.id_auto = auto.id

    def go_aggiungi_auto(self):
        self.gestione_auto.aggiungi_auto()
        self.popola_lista_veicoli()

    def go_elimina_auto(self):
        if self.id_auto is not None:
            res = self.gestione_auto.elimina_auto(self.id_auto)
            if res:
                self.print_messagebox("Auto eliminato con successo!")
            else:
                self.print_messagebox("Errore durante l'eliminazione!")
            self.id_auto = None
        self.popola_lista_veicoli()

    def go_modifica_auto(self):
        if self.id_auto is not None:
            auto = self.gestione_auto.ricerca_auto_id(self.id_auto)
            if auto is not None:
                self.gestione_auto.set_auto(auto)
                self.modifica_auto = VistaModificaAuto(self.gestione_auto)
                self.modifica_auto.closed.connect(self.popola_lista_veicoli)
                self.modifica_auto.show()
                self.id_auto = None

    def go_back(self):
        self.close()

    def print_messagebox(self, message):
        mb = QMessageBox()
        mb.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        mb.setWindowTitle("Attenzione!")
        mb.setIcon(QMessageBox.Information)
        mb.setStyleSheet("background-color: rgb(255,255,255); color: rgb(0,0,0);")
        mb.setText(message)
        mb.exec()
