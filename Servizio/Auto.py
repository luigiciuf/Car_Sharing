import os
import pathlib
import pickle
import uuid

from Utils.Const.PathFiles import PATH_VEICOLI


class Auto:

    def __init__(self):
        self.id = ""
        self.costo_minuto = 0.40
        self.disponibilita = True

    # 1. crea un nuovo auto
    # 2. salva sul file
    # return: self (questo auto)
    def crea(self):
        self.id = str(uuid.uuid4())[:8]  # genero un codice univoco identificativo da 8 cifre
        self.disponibilita = True
        veicoli = {}
        if os.path.isfile(PATH_VEICOLI):
            with open(PATH_VEICOLI, "rb") as f:
                veicoli = pickle.load(f)

        veicoli[self.id] = self
        if not os.path.isdir(pathlib.Path(PATH_VEICOLI).parent):
            os.mkdir(pathlib.Path(PATH_VEICOLI).parent)
        with open(PATH_VEICOLI, "wb") as f:
            pickle.dump(veicoli, f, pickle.HIGHEST_PROTOCOL)

        return self

    # Metodo setter
    # 1. setta la disponibilità
    # 2. salva su file
    def set_disponibilita(self, disponibilita):
        self.disponibilita = disponibilita

        veicoli = {}
        if os.path.isfile(PATH_VEICOLI):
            with open(PATH_VEICOLI, 'rb') as f:
                veicoli = dict(pickle.load(f))

        veicoli[self.id].disponibilita = disponibilita
        with open(PATH_VEICOLI, "wb") as f:
            pickle.dump(veicoli, f, pickle.HIGHEST_PROTOCOL)

    # metodo getter
    # ritorna lo stato attuale del auto relativo alla disponibilità
    # return: Boolean
    def get_disponibilita(self):
        return self.disponibilita

    # 1. elimina l auto
    # 2. salva su file
    def rimuovi(self):
        if os.path.isfile(PATH_VEICOLI):
            with open(PATH_VEICOLI, "rb") as f:
                veicoli = pickle.load(f)
                del veicoli[self.id]
            with open(PATH_VEICOLI, "wb") as f:
                pickle.dump(veicoli, f, pickle.HIGHEST_PROTOCOL)
            del self

    # ritorna un dizionario con tutti i veicoli
    # return: Dict of Auto
    def get_veicoli(self):
        veicoli = {}
        if os.path.isfile(PATH_VEICOLI):
            with open(PATH_VEICOLI, 'rb') as f:
                veicoli = dict(pickle.load(f))
        return veicoli

    # ritorna una lista di veicoli con disponibilità True
    # return: List
    def get_disponibili(self):
        disponibili = []
        if os.path.isfile(PATH_VEICOLI):
            with open(PATH_VEICOLI, 'rb') as f:
                veicoli = dict(pickle.load(f))
                for auto in veicoli.values():
                    if auto.disponibilita:
                        disponibili.append(auto)
        return disponibili

    # to_string()
    # return: String
    def __str__(self):
        if self.disponibilita:
            return "Targa Auto: " + self.id + "\n" + \
               "Costo al minuto: " + str(self.costo_minuto) + "\n" + \
               "Disponibilita: Disponibile" + "\n"
        else:
            return "Targa auto: " + self.id + "\n" + \
               "Costo al minuto: " + str(self.costo_minuto) + "\n" + \
               "Disponibilita: Non disponibile" + "\n"
