# -*- coding: utf-8 -*-

# messages for user
wiadomosc0 = "\nWprowadzanie przedmiotów zakończone."

wiadomosc1 = """\nError! Wprowadzanie przedmiotów zakończone.
Waga przedmiotu musi mieścić się w zakresie 1.00 - 10.00 kg."""

wiadomosc2 = """Górny limit wagi przesyłki osiagnięty.
Przesyłka przekazana do wysyłki.
Rozpoczynam pakowanie do kolejnej paczki.
"""


# define objects
liczba_przedmiotow = int(input("Liczba przedmiotów do wysyłki: "))

lista = []
biezaca_przesylka = []
wagi_przesylek = []
puste_kg = []


# for loop
for i in range(1, (liczba_przedmiotow + 1)):
    waga_przedmiotu = float(input("Podaj wagę przedmiotu: "))
    if waga_przedmiotu == 0:
        print(wiadomosc0)
        lista.append(int(999))
        break
    if waga_przedmiotu < 1 or waga_przedmiotu > 10:
        print(wiadomosc1)
        break
    lista.append(waga_przedmiotu)
    biezaca_przesylka.append(waga_przedmiotu)
    if sum(biezaca_przesylka) == 20:
        print(wiadomosc2)
        wagi_przesylek.append(sum(biezaca_przesylka))
        biezaca_przesylka = []
    if sum(biezaca_przesylka) > 20:
        print(wiadomosc2)
        biezaca_przesylka = biezaca_przesylka[:-1]
        wagi_przesylek.append(sum(biezaca_przesylka))
        biezaca_przesylka = []
        biezaca_przesylka.append(waga_przedmiotu)


# if user input item weigth == 0
if lista[-1] == int(999):
    lista = lista[:-1]
    for waga in lista:
        biezaca_przesylka.append(waga_przedmiotu)
        if sum(biezaca_przesylka) == 20:
            print(wiadomosc2)
            wagi_przesylek.append(sum(biezaca_przesylka))
            biezaca_przesylka = []
        if sum(biezaca_przesylka) > 20:
            print(wiadomosc2)
            biezaca_przesylka = biezaca_przesylka[:-1]
            wagi_przesylek.append(sum(biezaca_przesylka))
            biezaca_przesylka = []
            biezaca_przesylka.append(waga_przedmiotu)


waga_ost_paczki = sum(biezaca_przesylka)

if waga_ost_paczki >= 1:
    wagi_przesylek.append(waga_ost_paczki)

for waga in wagi_przesylek:
    puste_kg.append(20 - waga)


# indexing in Python starts from 0
maks_puste_kg = max(puste_kg)
index = (puste_kg.index(maks_puste_kg) + 1)

if sum(lista) == 0:
    lista = []


# printing final summary
print(f"\n----------\n"
      f"Wysłano {len(lista)} przedmioty(ów) o wagach {lista} w {len(wagi_przesylek)}"
      f" paczkach. \nŁącznie wysłano {sum(lista)} kg.")

if sum(puste_kg) > 0:
    print(f"\nLiczba wysłanych 'pustych' kilogramów wynosi"
          f" {(len(wagi_przesylek)*20)-sum(lista)}."
          f"\nPaczka z największą liczbą wysłanych 'pustych' kilogramów to paczka"
          f" nr {index}, \nw której wysłano {maks_puste_kg} 'pustych' kilogramów")
