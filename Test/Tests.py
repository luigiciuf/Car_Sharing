import os.path
import unittest

from Controller.GestioneAuto import GestioneAuto
from Controller.GestioneClienti import GestioneClienti
from Controller.GestioneContratto import GestioneContratto
from Controller.GestioneStatistiche import GestioneStatistiche
from Utils.Const import PathFiles


class Tests(unittest.TestCase):
    def tes_registra_cliente(self):
        self.gestione_clienti=GestioneClienti()
        if os.path.exists(PathFiles.PATH_CLIENTI):
            os.remove(PathFiles.PATH_CLIENTI)
        cliente, portafoglio=self.gestione_clienti.registra_cliente("Mario", "Rossi","RSSMRA80A01H501U","1234567890","password")

        self.assertEqual(cliente.cf, "RSSMRA80A01H501U")
        self.assertEqual(portafoglio.saldo,0)

    def test_crea_auto(self):
        self.gestione_auto= GestioneAuto()
        if os.path.exists(PathFiles.PATH_VEICOLI):
            os.remove(PathFiles.PATH_VEICOLI)
        for i in range(5):
            self.gestione_auto.aggiungi_auto()
        self.assertEqual(len(self.gestione_auto.get_all_veicoli()),5)
        self.assertEqual(all(value.disponibilita is True for value in self.gestione_auto.get_all_veicoli().values()),True)

    def test_versamento(self):
        self.gestione_clienti=GestioneClienti()
        if os.path.exists(PathFiles.PATH_CLIENTI):
            os.remove(PathFiles.PATH_CLIENTI)
        cliente, portafoglio = self.gestione_clienti.registra_cliente("Mario", "Rossi", "RSSMRA80A01H501U",
                                                                     "1234567890", "password")
        portafoglio.versa(10.0)
        self.assertEqual(portafoglio.saldo, 10.0)

    def test_statistiche(self):
        self.gestione_statistiche = GestioneStatistiche()
        self.gestione_contratti = GestioneContratto()
        if os.path.exists(PathFiles.PATH_CONTRATTI):
            os.remove(PathFiles.PATH_CONTRATTI)
        self.gestione_contratti.stila_contratto("12345678", 60.0, 0.2, "abcdefgh", 0.0)
        self.gestione_contratti.stila_contratto("12345567", 30.0, 0.1, "abcdefgh", 0.0)
        self.gestione_contratti.stila_contratto("12345687", 120.0, 0.4, "abcdefgh", 0.0)
        self.assertEqual(len(self.gestione_contratti.get_contratti()), 3)

    def test_creazione_contratto(self):
        self.gestione_contratti=GestioneContratto()
        if os.path.exists(PathFiles.PATH_CONTRATTI):
            os.remove(PathFiles.PATH_CONTRATTI)
        contratto=self.gestione_contratti.stila_contratto("12345678", 60.0,0.4 , "abcdefgh", 0.0)
        self.assertEqual(contratto.id_auto,"12345678")
