from Uzytkownik import Uzytkownik


imie1 = "abba"
imie2 = "akka"
imie3 = "kabba"
imie4 = "aaaak"

imiona = [imie1,imie2,imie3,imie4]

nazwisko1 = "canna"
nazwisko2 = "lakka"
nazwisko3 = "popoa"
nazwisko4 = "tikka"

nazwisko = [nazwisko1,nazwisko2,nazwisko3,nazwisko4]

wiek1 = 12
wiek2 = 23
wiek3 = 34
wiek4 = 1

wieki = [wiek1,wiek2,wiek3,wiek4]

#for x in imiona:
#    y = imiona.index(x)
#    print(imiona[y], nazwisko[y])
#    if wieki[y] >=18:
#        print("pelnoletni")
#    else:
#        print("niepelnoletni")
#    print(" ")



user1 = Uzytkownik()
user2 = Uzytkownik()
user3 = Uzytkownik()

user1.imie = "jan"
user1.nazwisko = "janowski"
user1.wiek = 5

user2.imie = "jakub"
user2.nazwisko = "kubowski"
user2.wiek = 51

user3.imie = "pawel"
user3.nazwisko = "pawlowski"
user3.wiek = 31

user1.zmienwiek(30)

user1.wyswietl()

user2.wyswietl()

user3.wyswietl()

