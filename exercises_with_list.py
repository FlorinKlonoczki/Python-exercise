# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# ● Afișeaz-o
# ● Inversează ordinea folosind slicing și suprascrie această listă.
# ● Printează varianta actuală (inversată).
# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.


note_muzicale = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si', 'Do']
print(note_muzicale)
new_note_muzicale = note_muzicale[::-1]  # suprascriem prima lista prin slicing
print(new_note_muzicale)
new_note_muzicale.reverse()  # se inverseaza lista prin metoda reverse
print(new_note_muzicale)

# 2. De câte ori apare ‘do’?

note_muzicale = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si', 'Do']

print(f"'Do' apare de {note_muzicale.count('Do')} ori")

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.

list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]

list_3 = list_1 + list_2
list_1.extend(list_2)
print(list_3)
print(list_1)

# 4.
# ● Sortează și afișază lista generată la exercițiul anterior.
# ● Sortează numărul 0 folosind o funcție.
# ● Afișaza iar lista.
list_1.sort()
print(list_1)
list_1.pop(0)
print(list_1)
#
# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
# ● Lista este goală.
# ● Lista nu este goală.
list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]
list_1.extend(list_2)

if len(list_1) == 0:
    print("List is empty")
else:
    print("List is not empty")

# 6.Folosește o funcție care să șteargă lista de la exercițiul 3.

list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]
list_1.extend(list_2)
print(list_1)
list_1.clear()
print(list_1)

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.

if len(list_1) == 0:
    print("List is empty")
else:
    print("List is not empty")

# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}

print(dict1.keys())

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie

# for i in dict1:
#     print(f" {i} are nota {dict1[i]}")
print(f"Ana a luat nota {dict1.get('Ana')}")
print(f"Ana a luat nota {dict1.get('Gigel')}")
print(f"Ana a luat nota {dict1.get('Dorel')}")

# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1)
dict1.update(Dorel=6)
print(dict1)

# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi

dict1.pop('Gigel')
print(dict1)
dict1['Ionica'] = 9    # add a new item in dict
print(dict1)

# 12.
# Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
# ● Afișeaza zile_sapt


zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
print(zile_sapt)
zile_sapt.add('luni') # adaugam 'luni' setului, acesta nu permite duplicate, deci nu o afiseaza de 2 ori
print(zile_sapt)

# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.

if weekend.issubset(zile_sapt):
    print("Weekend este un subset al zilelor din săptămânii")
else:
    print("Weekend nu este un subset al zilelor din săptămânii")

    # 14.Afișează diferențele dintre aceste 2 seturi.

diferente = zile_sapt.difference(weekend)
print(diferente)

# 15. Afișază intersecția elementelor din aceste 2 seturi.

instersectia = zile_sapt.intersection(weekend)
print(instersectia)


# 16. Ne imaginăm o echipă de fotbal pt teren sintetic.
#  3 Schimbări maxime admise:
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3

list_players = ['Dorel', 'Dorin', 'Radu', 'Paul', 'George']
list_rezerva = ['Marian', 'Marin', 'Anton']
print(list_players)
list_players.sort()
print(list_players)
list_players.remove('Paul')
print(list_players)
list_players.append('Paul')
print(list_players)