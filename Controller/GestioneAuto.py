import os
import pickle

from Servizio.Auto import Auto
from Utils.Const.PathFiles import PATH_VEICOLI


class GestioneAuto:
    def __init__(self):
        self.auto = Auto()

    # metodo setter
    def set_auto(self, auto):
        self.auto = auto

    # metodo setter
    # imposta la disponibilita di un auto
    def set_disponibilita_auto(self, disponibilita):
        self.auto.set_disponibilita(disponibilita)

    # ritorna una lista di veicoli con disponibilita True
    # return: List
    def get_veicoli_disponibili(self):
        return self.auto.get_disponibili()

    # ritorna un dizionario di tutti i veicoli
    # return: Dict of Auto
    def get_all_veicoli(self):
        return self.auto.get_veicoli()

    # crea un nuova auto
    def aggiungi_auto(self):
        self.auto.crea()

    # elimina un auto tramite id_auto
    # return: Boolean

    def elimina_auto(self, id_auto):
        temp_auto = self.ricerca_auto_id(id_auto)
        if isinstance(temp_auto, Auto):
            temp_auto.rimuovi()
            return True
        else:
            return False

    # ricerca del auto tramite id_auto
    # return: Auto
    def ricerca_auto_id(self, id_auto):
        veicoli = {}
        if os.path.isfile(PATH_VEICOLI):
            with open(PATH_VEICOLI, 'rb') as f:
                veicoli = dict(pickle.load(f))

        if len(veicoli) > 0:
            for auto in veicoli.values():
                if auto.id == id_auto:
                    return auto
            return None
        else:
            return None

    # ritorna la disponibilità dell auto
    # return: Boolean
    def is_disponibile(self):
        return self.auto.get_disponibilita()
