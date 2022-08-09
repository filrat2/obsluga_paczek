# -*- coding: utf-8 -*-

# messages for user
wiadomosc0 = """Jeśli podano element o wadze 0, program powinien zakończyć
działanie, tak jakby maksymalna liczba paczek została osiągnięta."""

wiadomosc1 = """Error! Działanie programu zakończone.
Waga przedmiotu musi mieścić się w zakresie 1.00 - 10.00 kg."""

wiadomosc2 = """Górny limit wagi przesyłki osiagnięty.
Przesyłka przekazana do wysyłki.
Rozpoczynam pakowanie do kolejnej paczki.
"""


# define objects
liczba_przedmiotow = int(input("Liczba przedmiotów do wysyłki: "))

lista = []
lista_fun = []
biezaca_przesylka = []
biezaca_przesylka_fun = []
wagi_przesylek = []

# for loop
for i in range(1, (liczba_przedmiotow + 1)):
    waga_przedmiotu = float(input("Podaj wagę przedmiotu: "))
    if waga_przedmiotu == 0:
        print(wiadomosc0)
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

# obiekty_w_paczce = len(biezaca_przesylka)
waga_ost_paczki = sum(biezaca_przesylka)
wagi_przesylek.append(waga_ost_paczki)

print(f"Wysłano {len(lista)} przedmiotów o wagach {lista} w {len(wagi_przesylek)}"
      f" paczkach. \nŁącznie wysłano {sum(lista)} kg."
      f"\nLiczba wysłanych 'pustych' kilogramów wynosi"
      f" {(len(wagi_przesylek)*20)-sum(lista)}.")

"""
print(lista)
print(wagi_przesylek)
print(sum(wagi_przesylek))
print(sum(lista))
"""
