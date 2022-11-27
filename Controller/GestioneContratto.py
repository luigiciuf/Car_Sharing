import os
import pickle

from Attivita.Contratto import Contratto

from Controller.GestioneClienti import GestioneClienti
from Utils.Const.PathFiles import PATH_CONTRATTI


class GestioneContratto:
    def __init__(self):
        self.gestione_clienti = GestioneClienti()
        self.contratto = None

    # ritorna un dizionario di tutte le ricevute del cliente corrente
    # return: Dict of contratto
    def get_contratti_cliente(self):
        if os.path.isfile(PATH_CONTRATTI):
            with open(PATH_CONTRATTI, "rb") as f:
                contratti = dict(pickle.load(f))
            return [contratto for contratto in contratti.values() if
                    contratto.id_cliente == self.gestione_clienti.cliente_corrente.id]
        else:
            return None

    # ritorna un dizionario con tutte i contratto
    # return: Dict of COntratto
    def get_contratti(self):
        contratti = {}
        if os.path.isfile(PATH_CONTRATTI):
            with open(PATH_CONTRATTI, "rb") as f:
                contratti = dict(pickle.load(f))
        if len(contratti) > 0:
            return contratti
        else:
            return None

            # provvede a creare un contratto

    # return: String
    def stila_contratto(self, id_auto, tempo_totale, costo_totale, id_cliente, saldo_portafoglio):
        self.contratto= Contratto()
        return self.contratto.crea(
            id_auto=id_auto,
            costo_totale=costo_totale,
            tempo_totale=tempo_totale,
            id_cliente=id_cliente,
            saldo_portafoglio=saldo_portafoglio
        )
