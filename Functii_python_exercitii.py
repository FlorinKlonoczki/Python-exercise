# 1.Funcție care să calculeze și să returneze suma a două numere

def suma():
    a = [2, 5]
    x = sum(a)
    return x


suma()


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def odd_even_number(x):
    if x % 2 == 0:
        return True
    else:
        return False


print(odd_even_number(4))


# 3. Funcție care returnează numărul total de caractere din numele tău complet.(nume, prenume, nume_mijlociu)

def numar_caracter(nume, prenume, nume_mijlociu):
    nume_complet = nume + prenume + nume_mijlociu
    return len(nume_complet)


print(numar_caracter("klonoczki", "florin", "silviu"))


# 4. Funcție care returnează aria dreptunghiului

def aria_dreptunghiului(latime, lungime):
    aria = latime * lungime
    return aria


print(aria_dreptunghiului(10, 40))

# 5. Funcție care returnează aria cercului
import math


def area_of_the_circle(Radius):
    area = Radius ** 2 * math.pi
    return area


Radius = float(input("Please enter the radius of the given circle: "))
print(" The area of the given circle is: ", area_of_the_circle(Radius))


# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și Talse dacă nu găsește.

def get_char(text):
    if 'Buna' in text:
        return True
    else:
        return False


print(get_char('Buna, ce faci?'))


# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

def char_lower_upper(text):
    calc_upper = 0
    calc_lower = 0
    for cuvinte in text:
        if cuvinte.islower():
            calc_lower += 1
        if cuvinte.isupper():
            calc_upper += 1
    print(f"Nr. de caractere lower case este{calc_lower}")
    print(f"Nr. de caractere lower case este{calc_upper}")


print(char_lower_upper("Buna, ce faci Geo?"))


# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive

def positive_list(my_list):
    my_list_positive = []
    for x in my_list:
        if x >= 0:
            my_list_positive.append(x)
    return my_list_positive


my_list = [2, 3, -1, 5, 0, -6]
print(positive_list(my_list))


# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

def numere(x, y):
    if x > y:
        print(f"Primul număr {x} este mai mare decat al doilea nr {y}")
    if y > x:
        print(f"Al doilea nr {y} este mai mare decat primul nr {x}")
    else:
        print("Numerele sunt egale.")


numere(2, 2)


# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False

def adauga(x, my_set):
    if x not in my_set:
        my_set.add(x)
        print(f'I added the new number {x} in the set!')

    else:
        print(f"I didn't add the number {x}, it is already in the set!")
        return False


print(adauga(5, {2, 3, 6}))

# 11. Funcție care primește o lună din an și returnează câte zile are acea luna.

year = {'ianuarie': '31', 'februarie': '28/29', 'martie': '31', 'aprilie': '30', 'mai': '31', 'iunie': '30',
        'iulie': '31', 'august': '31', 'septembrie': '30', 'octombrie': '31', 'noiembrie': '30',
        'decembrie': '31'}


def get_days_of_month(get_month, year):
    for month, days in year.items():
        if month == get_month:
            return days


print(get_days_of_month(get_month=input('enter a month: '),
                        year={'ianuarie': '31', 'februarie': '28/29', 'martie': '31', 'aprilie': '30', 'mai': '31',
                              'iunie': '30', 'iulie': '31', 'august': '31', 'septembrie': '30', 'octombrie': '31',
                              'noiembrie': '30', 'decembrie': '31'}))


# 12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)

def calculator(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    print("Suma: ", a)
    print("Diferenta: ", b)
    print("Inmultirea: ", c)
    print("Impartirea: ", d)


calculator(10, 2)


# 13. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
def count_list(my_list):
    contor = {}
    for i in my_list:
        if i in contor:
            contor[i] += 1
        else:
            contor[i] = 1
    return contor


print(count_list(my_list=[1, 3, 1, 5, 9, 7, 7, 5, 5]))


# 14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele

def max_number(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z


print(f"numarul mai mare este {max_number(2, 3, 1)}")


# 15. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)

def sum_numbers(number):
    """iteram prin numere si returnam suma lor"""

    total = sum(range(0, number + 1))

    return total


print(f"suma numerelor este={sum_numbers(5)}")


# Exerciții Opționale - Bonus
#
# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.
#
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}
def afisare_numere_duble(list1, list2):
    numere_duble = []
    for i in list1:
        if i in list2:
            numere_duble.append(i)
            print(numere_duble)


list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]

afisare_numere_duble(list1, list2)

# sau mai simplu
matches = {x for x in list1 if x in list2}
print(matches)


# 2. Funcție care să aplice o reducere de preț.
# Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
# Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.


def discount_calculator(user_price, user_discount):
    if 0 < user_discount < 100:
        final_price = user_price - user_price * user_discount / 100
        return final_price
    else:
        print("\nThe entered discount is invalid!")


price = float(input("\nEnter the product price to calculate the discount price:\t"))
discount = float(input("\nEnter the discount (%):\t"))
print(f"\nThe final price is: {round(discount_calculator(price, discount), 2)}")

#  3.Funcție care să afișeze data și ora curentă din România.
# (bonus: afișazăi și data și ora curentă din China)
from datetime import datetime
import pytz

now = datetime.now()
print(now)
china = pytz.timezone('Asia/Shanghai')
china_time = datetime.now(china)
print(china_time.strftime("Date is %d-%m-%y and time is %H:%M:%S"))

# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta :)


from datetime import date


def zile_pana_la_craciun(chistmas_date, today):
    zile_ramase = (chistmas_date - today).days
    print(f"Zile ramase pana la craciun sunt:{zile_ramase}")


now = date.today()
chistmas = date(2023, 12, 25)

zile_pana_la_craciun(chistmas, now)
