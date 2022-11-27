from Attivita.Corsa import Corsa
from Controller.GestioneClienti import  GestioneClienti
from Controller.GestioneAuto import  GestioneAuto
from Controller.GestioneContratto import  GestioneContratto
from Controller.GestioneContratto import Contratto
from Servizio.Auto import Auto


class GestioneNoleggio:

    def __init__(self):
        self.gestione_clienti = GestioneClienti()
        self.gestione_contratti = GestioneContratto()
        self.gestione_veicoli = GestioneAuto()
        self.corsa = None

    # 1. controllo il saldo (minimo 5€)
    # 2. prelevo le informazioni dell auto
    # 3. setto l auto  a "non disponibile"
    # 4. avvio la corsa
    # return: Boolean
    def avvia_corsa(self, id_auto):
        if float(self.gestione_clienti.visualizza_portafoglio()) >= 5.00:
            auto = self.gestione_veicoli.ricerca_auto_id(id_auto)
            if isinstance(auto, Auto):
                self.gestione_veicoli.set_auto(auto)
                self.gestione_veicoli.set_disponibilita_auto(False)
                self.corsa = Corsa()
                self.corsa.avvia()
                return True
        return False

    # 1. controllo se esiste una corsa avviata
    # 2. calcolo il tempo_utilizzo impiegato e il costo totale
    # 3. prelevo il denaro dal conto
    # 4. stilo la gestore_statistiche
    # return: String
    def termina_corsa(self):
        if isinstance(self.corsa, Corsa) and isinstance(self.gestione_veicoli.auto, Auto):
            self.corsa.termina()
            self.gestione_veicoli.set_disponibilita_auto(True)
            tempo_totale = self.corsa.tempo_utilizzo()
            costo_totale = self.corsa.costo_totale()
            self.gestione_clienti.preleva_denaro(costo_totale)
            contratto = self.gestione_contratti.stila_contratto(
                id_auto=self.gestione_veicoli.auto.id,
                tempo_totale=tempo_totale,
                costo_totale=costo_totale,
                saldo_portafoglio=self.gestione_clienti.visualizza_portafoglio(),
                id_cliente=self.gestione_clienti.cliente_corrente.id
            )
            self.corsa = None
            return True, contratto
        return False, None
