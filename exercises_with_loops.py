# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for x in range(len(masini)):  # for
    x = masini[x]
    print(f"masina mea preferata este {x}")
print()
for masina in masini:  # for each
    print(f"masina mea preferata este {masina}")
print()
x = 0
while x < len(masini):  # atata timp cat x este mai mic decat lungimea listei
    masina = masini[x]  # variabila masina ia valoarea fiecarui index x
    x += 1  # incrementam pe x pentru fiecare index din lista
    print(f"masina mea preferata este {masina}")

# 2. Aceeași listă:
# Folosește un for else
# În for
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule, exceptând primul și ultimul.
# În else:
# - Printează lista.

for x in range(1, len(masini), -1):
    x = masini[x].upper()
    print(f"masina mea preferata este {x}")
else:
    print(masini)

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == "Mercedes":
        print("Am găsit mașina dorită de dvs")
        break
    else:
        print(f"Am găsit mașina {masina}. Mai căutam")

# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Trabant:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.

for masina in masini:
    if masina == "Trabant":
        continue
    if masina == "Lăstun":
        continue
    print(f"S-ar putea să vă placă mașina {masina}")

# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for i in range(len(masini)):
    if masini[i] == 'Lastun' or masini[i] == 'Trabant':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
print(f'Modele vechi {masini_vechi}')
print(f'Modele noi {masini}')

# 6. Având dict:
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.

pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

for k, v in pret_masini.items():
    if v < 15000:
        print(f' Pentru bugetul dvs de 15000 euro puteti alege masina {k} cu pretul de {v} euro.')
for k, v in pret_masini.items():
    print(f'In showroom avem masina {k} la pretul {v} euro.')
for k, v in pret_masini.items():
    if v < 15000 and k == 'Lastun':
        print(f'Pentru bugetul de sub 15000 euro puteti alege masina {k} la pretul de {v} euro.')

# 7. Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
cifra_trei = 0
for i in numere:
    if i == 3:
        cifra_trei += 1
print(f'Cifra 3 apare de {cifra_trei} ori.')

# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for i in numere:
    suma += i
    print(f'Suma numerelor este: {suma}')

# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
biggest_number = 0
for i in range(len(numere)):
    if i > biggest_number:
        biggest_number = i
print(f'Cel mai mare numar este {biggest_number}')

# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numere_negative = []
for i in range(len(numere)):
    if numere[i] >0:
        numere_negative = - abs(numere[i])
        print(numere_negative, end= " ")

# 11.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișeaza cele 4 liste la final

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    if numar % 2 != 0:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    if numar < 0:
        numere_negative.append(numar)
print(f"numerele pare: {numere_pare}")
print(f"numerele impare: {numere_impare}")
print(f"numerele pozitive: {numere_pozitive}")
print(f"numerele negative: {numere_negative}")

# 12. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.

for i in range(len(alte_numere)):
    for j in range(0, len(alte_numere) - i - 1):
      if alte_numere[j] > alte_numere[j + 1]:
        temp = alte_numere[j]
        alte_numere[j] = alte_numere[j+1]
        alte_numere[j+1] = temp

print(alte_numere)

# 13. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# Ex:3
# 1
# 22
# 333

numar = int(input('Pick a number: '))
for i in range(1, numar + 1):
    for j in range(i):
        print(i, end="")
    print()

# 5.
# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’


tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este: {tastatura_telefon[i][j]}')