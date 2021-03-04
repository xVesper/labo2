# lista = ["wyraz", 4.23, 5, 6, 2, [4,5,6]]
#
# print(lista)
#
# lista.append("a")
# lista.append(12)
# print(lista)
#
# lista.insert(3,3.13)
# print(lista)
#
# lista.pop()
# print(lista)
#
# lista.pop(3)
# print(lista)
#
# lista.remove("wyraz")
# print(lista)
#
# del lista[2]
# print(lista)
#
# lista.extend((2, 3, "ab"))
# print(lista)
#
# lista.reverse()
# print(lista)
#
# lista_nowa = [6, 3.13, 10, 3, 1, 5.6, 2]
# print(lista_nowa)
# lista_nowa.sort()
# print(lista_nowa)
#
# print("------------------------------------------------------------")
#
# slownik = {2: "a", 3: 5, "cos": "abc", 2: 2}
# print(slownik)
#
# slownik[6] = 1.1
# print(slownik)
#
# print(slownik[6])
#
# slownik.pop(6)
# print(slownik)
#
# print(slownik.keys())
# print(slownik.values())
#
# del slownik[2]
# print(slownik)
#
# print("------------------------------------------------------------")
#
# import sys as system
#
# system.stdout.write("wpisz dowolna liczbe :")
# liczba = system.stdin.readline()
# system.stdout.write(liczba)
# system.stdout.write("a")
# system.stdout.write("a")
#
# print("------------------------------------------------------------")

# if warunek:
#     instrukcje
#     instrukcja2
# else warunek1:
#     isntrukcje
# else:

# a = input("wprowadz liczbe a: ")
# b = input("wprowadz liczbe b: ")
# c = input("wprowadz liczbe c: ")
# d = input("wprowadz liczbe d: ")
#
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
#
# if (a > b) & (c > d):
#     print("liczba a jest wieksza od b i liczba c jest wieksza od d")
#     print(type((a > b) & (c > d)))
# else:
#     print("liczba a jest mniejsza od b lub liczba c jest mniejsza od d")
#
# print("------------------------------------------------------------")

# for licznik in sekwencja:
#     instrukcja
# else:

# for x in range(1,6,1):
#     print(x)

# lista = [3, 45, "s", 7.5]
# for x in lista:
#     print(x)
# else:
#     print("petla zakonczyla swoje dzialanie")

# print("------------------------------------------------------------")

# while warunek:
#     instrukcja
# else:
#     instrukcja

# z = 0
# while z != 10:
#     print(z)
#     z +=1
# else:
#     print("zostalo wyswietlone " +str(z) + "liczba")

# lista = [4, 6, 2, 3, 5, 9, 1]
# a = input("podaj liczbe a: ")
#
# licznik = 0
#
# while licznik < len(lista) - 1:
#     if int(a) - lista[licznik] == 0:
#         print(a + "-" + str(lista[licznik])+ " = 0")
#         break
#     else:
#         licznik += 1

# lista = [4, 6, 2, 3, 5, 9, 1]
# lista2 = [7, 3, 4, 6]
# suma = []
#
# for a in lista:
#     for b in lista2:
#         wynik = a + b
#         suma.append(wynik)
#     print(suma)

# a = input("wczytaj liczba a: ")
# b = input("wczoraj liczba b: ")
#
# try:
#     wynik = int(a) / int(b)
#     print(wynik)
# except ZeroDivisionError:
#     print("tylko Chuck Norris moze dzielic przez 0")