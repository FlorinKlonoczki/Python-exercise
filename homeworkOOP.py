# 2. Rezolvă exercițiul după ce ai urcat proiectul (tot ce am facut până acum împreună).
#
# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’
from abc import abstractmethod


class FormaGeometrica:
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descriere(self):
        print("Cel mai probabil am colturi")


#
# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură
class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    # ENCAPSULATION
    # latura este proprietate privată
    # Implementează getter, setter, deleter pentru latură
    # Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

    @property
    def cls_patrat(self):
        print(f"Getter: Latura patratului este {self.__latura}")

    @cls_patrat.setter
    def cls_patrat(self, latura):
        print(f"Setter: Noua dimesiune a laturi este {latura}")
        self.__latura = latura

    @cls_patrat.deleter
    def cls_patrat(self):
        print("Deletter : Am sters latura")
        self.__latura = None

    def aria(self):
        aria_patratului = self.__latura * 4
        return aria_patratului

# Le putem apela si la sfarsit

# patrat = Patrat(4)
# patrat.cls_patrat
# patrat.cls_patrat = 3
# print(f"Aria patratului este {patrat.aria()}")
# del patrat.cls_patrat
# patrat.cls_patrat


# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    @property
    def cls_cerc(self):
        print(f"Raza cercului este {self.__raza}")

    @cls_cerc.setter
    def cls_cerc(self, raza):
        print(f"Setter: Noua raza a cercului este {raza}")
        self.__raza = raza

    @cls_cerc.deleter
    def cls_cerc(self):
        print("Deletter: Am sters raza cercului")
        self.__raza = None

    def aria(self):
        aria_cercului = self.__raza * self.PI
        print(f"Aria cercului este {aria_cercului}")


# cerc = Cerc(10)
# cerc.cls_cerc
# cerc.aria()
# cerc.cls_cerc = 20
# cerc.aria()
# del cerc.cls_cerc
# cerc.cls_cerc


# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
#
# Creează un obiect de tip Pătrat și joacă-te cu metodele lui
# Creează un obiect de tip Cerc și joacă-te cu metodele lui
    def descriere(self):
        print("Eu nu am colturi")

patrat = Patrat(4)
patrat.cls_patrat
patrat.cls_patrat = 3
print(f"Aria patratului este {patrat.aria()}")
del patrat.cls_patrat
patrat.cls_patrat
patrat.descriere()

cerc = Cerc(10)
cerc.cls_cerc
cerc.aria()
cerc.cls_cerc = 20
cerc.aria()
del cerc.cls_cerc
cerc.cls_cerc
cerc.descriere()
