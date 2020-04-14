import sys
import csv
import os
import sqlite3
from sqlite3 import connect
from argparse import ArgumentParser

from models.gradebook import Gradebook
from models.gradebooks_list import Gradebooks_list
from models.shool_grade import School_grade
from models.student import Student


def main():
    # WLASCIWY PROGRAM
    print("\nMenu programu ETL\nProszę wpisać cyfrę")

    lista_dziennikow = Gradebooks_list()
    lista_dziennikow.dodanie_dziennika(Gradebook('dziennik_ocen'))

    dziennik_ocen = lista_dziennikow.wyszukaj_dziennik_po_nazwie('dziennik_ocen')

    dziennik_ocen.dodaj_studenta(Student('marcin'))

    while True:


        print("1 - dodawanie nowego studenta\n"
              "2 - przypisanie oceny oraz jej wagi danemu studentowi\n"
              "3 - policzenie średniej arytmetycznej ocen dla każdego ze studentów\n"
              "4 - wyświetlenie ocen danego studenta\n"
              "5 - wyświetl liste studentow\n"
              "6 - Utwórz nowy dziennik na podstawie starego\n"
              "7 - Znajdz dziennik po nazwie i przełącz się na niego\n"
              "8 - Wypisz listę dzienników\n"
              "9 - exit\n"
              "\nWybierz: ", end='')


        code = input()



        if code == '1':
            print('\nDodawanie nowego studenta...')
            print('\nPodaj imie:', end=' ')
            nowy_student = input()

            wyszukany_student = dziennik_ocen.wyszukaj_studenta_po_imieniu(nowy_student)
            print(wyszukany_student)
            if (wyszukany_student != None):
                print('Taki student już istnieje - spróbuj ponownie\n')
                continue
            else:
                print('wchodzimy zapisac uz')
                dziennik_ocen.dodaj_studenta(Student(nowy_student))
                continue
        if code == '2':
            print('\nPrzypisanie oceny oraz jej wagi danemu studentowi...')
            print('\nPodaj imie:', end=' ')
            szukany_student = input()
            wyszukany_student = dziennik_ocen.wyszukaj_studenta_po_imieniu(szukany_student)
            if (wyszukany_student != None):
                print('\nPodaj ocene:', end=' ')
                dodawana_ocena = int(input())
                print('\nPodaj wage oceny:', end=' ')
                waga_dodawanej_ocena = int(input())
                wyszukany_student.dodaj_ocene(School_grade(dodawana_ocena, waga_dodawanej_ocena))
            else:
                print('Nie udalo sie znaleźć studenta\n')
            continue

        if code == '3':
            print('\nPoliczenie średniej arytmetycznej ocen dla każdego studenta...')
            dziennik_ocen.wyswietl_srednia_ocen_wszystkich_studentow()
            continue
        if code == '4':
            print('\nWyświetl oceny danego studenta...')
            print('\nPodaj imie:', end=' ')
            szukany_student = input()
            wyszukany_student = dziennik_ocen.wyszukaj_studenta_po_imieniu(szukany_student)
            if (wyszukany_student != None):
                dziennik_ocen.wyszukaj_studenta_po_imieniu(szukany_student).wyswietl_oceny()
                continue
            else:
                print('Nie udalo sie znaleźć studenta\n')
                continue

            continue
        if code == '5':
            print('\nWyświetl listę studentów...')
            print('Lista studentów:')
            dziennik_ocen.wypisz_liste_studentow()
            continue
        if code == '6':
            print('\nUtwórz nowy dziennik na podstawie starego...')
            print('\nPodaj nazwe:', end=' ')
            nazwa_nowego_dziennika = input()
            lista_dziennikow.dodanie_dziennika_na_podstawie_starego(nazwa_nowego_dziennika, dziennik_ocen)
            continue
        if code == '7':
            print('\nZnajdz dziennik po nazwie...')
            print('\nPodaj nazwe:', end=' ')
            znajdz_dziennik = input()
            dziennik_ocen = lista_dziennikow.wyszukaj_dziennik_po_nazwie(znajdz_dziennik)
            continue
        if code == '8':
            print('\nWypisz listę dzienników...')
            lista_dziennikow.wypisz_liste_dziennikow()
            continue
        elif code == '9':
            sys.exit()
        else:
            print("Error - zła ")


if '__main__' == __name__:
    main()
