# Clasa Cerc
#     Atribute: rază, culoare
#     Constructor pentru ambele atribute
#     Metode:
# ●	descrie_cerc() - va PRINTA culoarea și raza
# ●	aria() - va RETURNA aria
# ●	diametru()
# ●	circumferinta()
#
import math
from math import pi


class Cerc:
    raza = 20
    culoare = "red"

    def descriere_cer(self):
        print(f" Raza cercului este {self.raza} si are culoare {self.culoare}")

    def aria(self):
        print(f" Aria cercului este {math.pi * (self.raza * self.raza)}")

    def diametru(self):
        diametru_cer = self.raza * 2
        print(f" Diametrul cercului este {diametru_cer}")

    def circumferinta(self):
        print(f" Circumferinta cercului este {(self.raza * 2) * math.pi}")


cerc = Cerc()
cerc.descriere_cer()
cerc.aria()
cerc.diametru()
cerc.circumferinta()


# 2. Clasa Dreptunghi
#      Atribute: lungime, lățime, culoare
#      Constructor pentru toate atributele
#      Metode:
# ●	descrie()
# ●	aria()
# ●	perimetrul()
# ●	schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().

class Dreptunghi:

    def __init__(self, new_lungime, new_latime, new_culoare):
        self.lungime = new_lungime
        self.latime = new_latime
        self.culoare = new_culoare

    def descriere(self):
        print(f"Dreptunghiul are lungimea de {self.lungime}, latimea de {self.latime}, si culoarea {self.culoare}")

    def aria(self):
        return self.lungime * self.latime

    def perimetrul(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self, new_color):
        print(f"Noua culoare a dreptungiului este {new_color}")
        self.culoare = new_color


dreptunghi = Dreptunghi(2, 3, "blue")
dreptunghi.descriere()
print(f"Aria dreptungiului este {dreptunghi.aria()}")
print(f"Perimetrul dreptungiului este {dreptunghi.perimetrul()}")
dreptunghi.schimba_culoarea("black")
dreptunghi.descriere()


# 3. Clasa Angajat
#      Atribute: nume, prenume, salariu
#      Constructor pentru toate atributele
#      Metode:
# ●	descrie()
# ●	nume_complet()
# ●	salariu_lunar()
# ●	salariu_anual()
# ●	marire_salariu(procent)

class Angajat:

    def __init__(self):
        self.nume = "Klonoczki"
        self.prenume = "Florin"
        self.salariu = 5000

    def descrie(self):
        print(f"Numele meu este {self.nume + ' ' + self.prenume} si am un salariu de {self.salariu} ron")

    def nume_complet(self):
        print(f"Numele meu complet este {self.nume + ' ' + self.prenume} ")

    def salariu_lunar(self):
        print(f"Am un salariu de {self.salariu} ron")

    def salariu_anual(self):
        print(f"Am un salariu  anual de {self.salariu * 12} ron")

    def marire_salariu(self, procent):
        marire = int(self.salariu / 100 * procent + self.salariu)
        self.salariu = marire
        print(f"Mi sa marit salariu cu {procent} % si acuma salariul meu este {marire} ")


angajat = Angajat()
angajat.descrie()
angajat.nume_complet()
angajat.salariu_lunar()
angajat.salariu_anual()
angajat.marire_salariu(5.56)
angajat.salariu_lunar()
angajat.salariu_anual()

# 1. Clasa Factură
#      Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
#      Constructor: toate atributele, fără serie
#      Metode:
# ●	schimbă_cantitatea(cantitate)
# ●	schimbă_prețul(pret)
# ●	schimbă_nume_produs(nume)
# ●	generează_factura() - va printa tabelar dacă reușiți
#
# Factura seria x număr y
# Data: generează automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon |      7       |       700       | 49000
#
# Indiciu pentru dată: https://www.geeksforgeeks.org/get-current-date-using-python/
from tabulate import tabulate
import datetime


class Factura:
    SERIA = "fgk444555"
    data = datetime.datetime.now()

    def __init__(self):
        self.numar = 23412
        self.nume_produs = "Telefon"
        self.cantitate = 7
        self.pret_buc = 4900

    def schimba_cantitatea(self, cantitatea):
        self.cantitate = cantitatea
        return cantitatea

    def schimba_pret(self, pret):
        self.pret_buc = pret
        return pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume
        return nume

    def total(self):
        totalul = self.pret_buc * self.cantitate
        return totalul

    def genereaza_factura(self, ):
        print(tabulate([[self.schimba_nume_produs("Telefon promo"), self.schimba_cantitatea(3), self.schimba_pret(4000), self.total()]],
                       headers=['Produs', 'cantitate', 'pret bucata', 'total'], tablefmt='orgtbl'))


factura = Factura()
print(f"Factura are seria {factura.SERIA} si număr {factura.numar}")
print(f"Data: {factura.data}")
factura.genereaza_factura()
