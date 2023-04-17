# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# O variabilă este un container din memorie care stochează valori.

# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
# # variabilă :

marca = 'mercedess'  # string -sir de caractere
an_fabricatie = 2020  # int - nr intreg
pret: float = 49.999  # float - nr zecimal
inmatriculata = True  # bool

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(marca))
print(type(an_fabricatie))
print(type(pret))
print(type(inmatriculata))

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
# aceeași variabilă (suprascriere):
# - Verifică tipul acesteia
print(round(pret))
pret = round(pret)
print(pret)

# 5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.
print(f'Am o masina marca {marca}')
print(f'Masina este din {an_fabricatie}')
print(f'Si am dat pe ea {pret} de mi de euro')
print(f'Masina este inamtriculata: {inmatriculata}')
marca = bool(marca)
print(type(marca))
an_fabricatie = float(an_fabricatie)
print(type(an_fabricatie))
pret = int(pret)
print(type(pret))
inmatriculata = str(inmatriculata)
print(type(inmatriculata))
print()

# 6. Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.

# nume = input('Introdu numele tau:')
# prenume = input ('introdu prenumele tau:')
# print(f'Numele tau este {nume +" "+ prenume} si are {len(nume + prenume)}caractere')


# 7. Citește de la tastatură:
# - lungimea;
# - lățimea.
# Afișează: 'Aria dreptunghiului este x'.
# lungime = int(input('Adauga lunimea dreptunghiului :'))
# latime = int(input('Adauga latimea dreptunghiului :'))
# x = lungime * latime
# print(f'Aria dreptunghiului este {x}')


# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# - afișează de câte ori apare cuvântul 'the';

text = 'Coral is either the stupidest animal or the smartest rock'
print(text.count('the'))

# 9. Același string.
# ● Afișează de câte ori apare cuvântul 'the';
# ● Printează rezultatul.
text1 = 'Coral is either the stupidest animal or the smartest rock'
x = text1.count('the')
print(f'Cuvantul "the" apare de {x} ori.')

# 10. Același string.
# ● Folosiți un assert ca să verificați dacă acest string conține doar numere.

# text2 = 'Coral is either the stupidest animal or the smartest rock'
# assert text2.isdigit(), 'txt nu contine numere'
# print()

# Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai
# nevoie de Google).
# 1. Exercițiu:
# - citește de la tastatură un string de dimensiune impară;
# - afișează caracterul din mijloc.

# opt_1 = input('Introduceti un string de dimensiune impara: ')
# print(f'Caracterul din mijloc este {opt_1[int(len(opt_1)/2)]}')

# 2. Folosind assert, verifică dacă un string este palindrom.

s = "malayalam"
assert s == s[::-1]
print(s)
if s == s[::-1]:
    print("Yes, malayalam is a polidrom")
else:
    print("No, is not a polidrom")

# 3. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.
# x, y = input('Introduceti un string din doua cuvinte: ').split()
# print(x)
# print(y)

# 4. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.
# opt_4 = input('Citeste un string de la tastatura: ')
# primul_car = opt_4[0]
# print(primul_car)
# x = opt_4.replace(primul_car,primul_car.upper())
# print(x)
#

# 5.Exercițiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ****

user = input('Introduceti userul dvs: ')
parola = input('Introduceti parola dvs: ')
parola = len(parola) * '*'
print(f'Parola pentru userul {user} este {parola} si are {len(parola)} caractere.')