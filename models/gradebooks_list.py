from models.gradebook import Gradebook


class Gradebooks_list:
    def __init__(self):
        self.lista_dziennikow = []

    def dodanie_dziennika(self, Gradebook):
        self.lista_dziennikow.append(Gradebook)

    def dodanie_dziennika_na_podstawie_starego(self, nazwa_nowego, stary_dziennik):
        self.lista_dziennikow.append(Gradebook(nazwa_nowego))
        self.wyszukaj_dziennik_po_nazwie(nazwa_nowego).lista_studentow = stary_dziennik.lista_studentow

    def wypisz_liste_dziennikow(self):
        for x in self.lista_dziennikow:
            print(f'{x.nazwa}')
        print('\n')

    def wyszukaj_dziennik_po_nazwie(self, nazwa):
        for x in self.lista_dziennikow:
            if(x.nazwa == nazwa):
                return x