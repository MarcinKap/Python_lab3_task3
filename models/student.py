class Student:

    def __init__(self, imie):
        self.lista_ocen = []
        self.imie = imie

    def srednia_ocen(self):
        if(len(self.lista_ocen)>0):
            sum = 0
            suma_wag = 0
            for x in self.lista_ocen:
                sum = sum + x.ocena * x.waga_oceny
                suma_wag = suma_wag + x.waga_oceny
            return sum / suma_wag
        else:
            return 0


    def wyswietl_oceny(self):
        if (len(self.lista_ocen) > 0):
            print('Lista ocen: ')
            for x in self.lista_ocen:
                print(f'Ocena: {x.ocena}, waga oceny: {x.waga_oceny}')

            print("\n")
        else:
            print('Ten student nie ma żadnej oceny')

    def dodaj_ocene(self, School_grade):
        self.lista_ocen.append(School_grade)



    def przedstaw_sie(self):
        print(f"Jestem {self.imie} ")