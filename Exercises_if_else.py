# Exercitii Python


# Verifică și afișează dacă x este număr natural sau nu.
x = int(input("Introduceti un numar:"))
if x > 0:
    print(f" {x} este un numar natural")
else:
    print(f"{x} nu este un numar natural")

# Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.

x = int(input("Introduceti un numar:"))
if x > 0:
    print(f" {x} este un numar pozitiv")
elif x == 0:
    print(f"{x} este un numar neutru")
else:
    print(f"{x} este un numar negativ")

# Verifică și afișează dacă x este între -2 și 13.

x = int(input("Introduceti un numar:"))
if x > -2 and x > 13:
    print(f" {x} se afla intre -2 si 13.")
else:
    print(f" {x} nu se afla intre -2 si 13.")

# Verifică și afișează dacă diferența dintre x și y este mai mică de 5.

x = int(input("Introduceti un numar x :"))
y = int(input("Introduceti un numar y :"))
if (x - y > 5):
    print("Diferența dintre x și y este mai mare de 5")
elif x - y == 5:
    print("Diferența dintre x și y este de 5")
else:
    print("Diferența dintre x și y este mai mica de 5")

# Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.

x = int(input("Introduceti un numar x :"))
if not (5 <= x <= 27):
    print(f"{x} NU este între 5 și 27")
else:
    print(f"{x} este între 5 și 27")

# x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.

x = int(input("Introduceti un numar x :"))
y = int(input("Introduceti un numar y :"))
if x == y:
    print(f"{x} si {y} sunt egal")
elif x > y:
    print(f"{x} este mai mare decat {y}")
else:
    print(f"{y} este mai mare decat {x}")

# X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

x = int(input("Introduceti un numar pentru latura triunghiului x :"))
y = int(input("Introduceti un numar pentru latura triunghiului y :"))
z = int(input("Introduceti un numar pentru latura triunghiului z :"))
if x == y != z:
    print(f" Triunghiul este isoscel")
elif x == y == z:
    print(f" Triunghiul este echilateral")
else:
    print(f" Triunghiul este oarecare")

# Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu

litera = input('Introduceti o litera: ')
if litera in 'a, e, i, o, u, A, E, I, O , U':
    print('Litera aleasa este o vocala!')
else:
    print('Litera aleasa este o consoana!')

# Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub =>

nota = float(input('Introduceti nota: '))
if nota > 9 and nota <= 10:
    print('A')
elif nota > 8 and nota <= 9:
    print('B')
elif nota > 7 and nota <= 8:
    print('C')
elif nota > 6 and nota <= 7:
    print('D')
elif nota > 4 and nota <= 6:
    print('E')
elif nota <= 4 and nota > 0:
    print('F')
else:
    print('Nota nu se incadreaza in sistemul romanesc de notare!')

# Verifică dacă x are minim 4 cifre (x e int).(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

x = input("Introduceti un numar: ")

if len(x) == 4:
    print(f"{x} are 4 cifre")
elif len(x) > 4:
    print(f"{x} nu are mai mult de 4 cifre")
else:
    print(f"{x} nu are minim 4 cifre")

# Verifică dacă x are exact 6 cifre.

x = input("Introduceti un numar: ")

if len(x) == 6:
    print(f"{x} are 6 cifre")
else:
    print(f"{x} nu are 6 cifre")

# Verifică dacă x este număr par sau impar (x e int).

x = int(input("Introduceti un numar: "))

if x % 2 == 0:
    print(f"{x} este număr par")
else:
    print(f"{x} nu este număr par")

# x, y, z (int)
# Afișează care este cel mai mare dintre ele?

x = int(input("Introduceti un numar x: "))
y = int(input("Introduceti un numar y: "))
z = int(input("Introduceti un numar z: "))

print(max(x, y, z), "este cel mai mare numar.")

# X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.

x = (int(input('Introduceti x ca unghi a unui triunghi: ')))
y = (int(input('Introduceti y ca unghi a unui triunghi: ')))
z = (int(input('Introduceti z ca unghi a unui triunghi: ')))
if x > 0 and y > 0 and z > 0:
    print('Triunghiul este valid.')
else:
    print('Triunghiul nu este valid!')

# Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citiți de la tastatură un int x
# ● Afișează stringul fără ultimele x caractere
# Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'

text = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introduceti un numar: '))
print(text[0:-x])

# Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5

text = 'Coral is either the stupidest animal or the smartest rock'
text_1 = (text[:5], text[-5:])
print(text_1)

# Același string.
# ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
# ● Folosind această variabilă + slicing, afișează tot stringul până la acest cuvant
# ● output: 'Coral is either the stupidest animal or the smartest'

text = 'Coral is either the stupidest animal or the smartest rock'
x = text.index("rock")
print(text)
print(f"Indexul de start al cuvântului rock este {x}")
print(text[0:x])

# Citește de la tastatura un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat

txt = input('Introduceti un cuvant: ')
assert txt[0].upper() == txt[-1].upper(), 'nu sunt la fel'

# Avand stringul '0123456789'
# ● Afișați doar numerele pare
# ● Afișați doar numerele impare
# (hint: folositi slicing, controlați din pas)

str = '0123456789'
str_par = str[0::2]
str_impar = str[1::2]
print(f'Numerele pare sunt {str_par}')
print(f'Numerele impare sunt {str_impar}')

#  Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll


import random

dice = random.randint(1, 6)
print(f"Your number is {dice}")

# Luați un numărul ghicit de la utilizator
# Verificați și afișați dacă utilizatorul a ghicit
# Veți avea 3 opțiuni
# ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# ● Ai ghicit. Felicitari! Ai ales x si zarul a fost y


dice_roll = random.randint(1, 6)
zar_ghicit = input('Ghiceste numar zar: ')
if zar_ghicit in ['1', '2', '3', '4', '5', '6']:
    if int(zar_ghicit) < int(dice_roll) and int(zar_ghicit) >= 1:
        print(f'Ai pierdut! Numarul {zar_ghicit} < {dice_roll}')
    elif int(zar_ghicit) > int(dice_roll) and int(zar_ghicit) <= 6:
        print(f'Ai pierdut! Numarul ales {zar_ghicit} > {dice_roll}')
    elif int(zar_ghicit) == int(dice_roll):
        print(f'Ai ghicit! Numarul ales {zar_ghicit} = {dice_roll}')
    else:
        print('Numarul ales nu este pe zar!')
else:
    print('Nu esti in jocul corect! Alege un zar intre 1 si 6!')
