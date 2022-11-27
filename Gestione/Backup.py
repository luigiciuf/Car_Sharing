import pickle
import time

import schedule

from Controller.GestioneClienti import  GestioneClienti
from Controller.GestioneAuto import  GestioneAuto
from Controller.GestioneContratto import  GestioneContratto
from Utils.Const.PathFiles import PATH_BACKUP


class Backup:

    def __int__(self):
        self.gestione_clienti=GestioneClienti()
        self.gestione_contratto=GestioneContratto()
        self.gestione_auto=GestioneAuto()
        self.portafogli={}
        self.contratti={}
        self.clienti={}
        self.veicoli={}

    def esegui_backup(self):
        self.clienti=self.gestione_clienti.cliente_corrente.get_clienti()
        self.contratti=self.gestione_contratto.get_contratti()
        self.portafogli=self.gestione_clienti.portafoglio_corrente.get_portafoglio()
        self.veicoli=self.gestione_auto.get_all_veicoli()

        with open(PATH_BACKUP,"wb") as f:
            for cliente in self.clienti:
                pickle.dump(cliente, f)
            for contratto in self.contratti:
                pickle.dump(contratto,f)
            for portafoglo in self.portafogli:
                pickle.dump(portafoglo,f)
            for veicoli in self.veicoli:
                pickle.dump(veicoli,f)




    def backup_every_day(self):
        schedule.every().day.at("23:30").do(self.esegui_backup)
        while True:
            schedule.run_pending()
            time.sleep(1)












