import os
import pathlib
import pickle
import uuid

from Servizio.Auto import Auto
from Utils.Const.PathFiles import PATH_CONTRATTI


class Contratto:

    def __init__(self):
        self.id = ""
        self.id_auto = ""
        self.costo_totale = 0.0
        self.tempo_totale = 0.0
        self.saldo_portafoglio = ""
        self.id_cliente = ""

    # 1. crea un nuovo contratto
    # 2. salva su file
    # return: self (questo contratto )
    def crea(self, id_auto, costo_totale, tempo_totale, saldo_portafoglio, id_cliente):
        self.id = str(uuid.uuid4())[:8]  # genero un codice identificativo univoco da 8 cifre
        self.id_auto = id_auto
        self.costo_totale = costo_totale
        self.tempo_totale = tempo_totale
        self.saldo_portafoglio = saldo_portafoglio
        self.id_cliente = id_cliente

        contratti = {}
        if os.path.isfile(PATH_CONTRATTI):
            with open(PATH_CONTRATTI, "rb") as f:
                contratti = dict(pickle.load(f))
        contratti[self.id] = self
        if not os.path.isdir(pathlib.Path(PATH_CONTRATTI).parent):
            os.mkdir(pathlib.Path(PATH_CONTRATTI).parent)
        with open(PATH_CONTRATTI, "wb") as f:
            pickle.dump(contratti, f, pickle.HIGHEST_PROTOCOL)

        return self

    # to_string()
    # return: String
    def __str__(self):
        # se sono passati piu di 60 secondi
        if self.tempo_totale >= 60:
            return "Targa auto: " + self.id_auto + "\n" + \
                   "Costo per minuto: " + str(Auto().costo_minuto) + " €/min\n" + \
                   "Minuti utilizzati: " + str(format(self.tempo_totale / 60, '.1f')) + "\n" + \
                   "Costo totale: " + str(self.costo_totale) + " €\n"
        # se sono passati meno di 60 secondi
        else:
            return "Targa auto: " + self.id_auto + "\n" + \
                   "Costo per minuto: " + str(Auto().costo_minuto) + " €/min\n" + \
                   "Secondi utilizzati: " + str(self.tempo_totale) + "\n" + \
                   "Costo totale: " + str(self.costo_totale) + " €\n"
