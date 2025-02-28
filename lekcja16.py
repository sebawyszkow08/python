import random

list1 = []

for x in range(50):
    list1.append(x * 2)  #random.randint(1,100)

#print(list1)

def bubblesort(list1):
        leng = len(list1) - 1
        issorted = 0

        while issorted != leng:
                issorted = 0
                a = 0
                b = 0
                for elementnr in range(leng):
                        if elementnr < leng  + 1:
                                #print(elementnr)
                                a = list1[elementnr]
                                b = list1[elementnr + 1]
                                if a > b:
                                       list1[elementnr] = b
                                       list1[elementnr + 1] = a
                                else:
                                       issorted +=1

        return list1


list1 = bubblesort(list1)
#print(list1)


#def linearsearch(list1,wantedv):
#        for element in range(len(list1)):
#                if list1[element] == wantedv:
#                        return element
#        return "none"
#       
#
#print(linearsearch(list1,2), end = "")
#print(linearsearch(list1,3), end = "")
#print(linearsearch(list1,16), end = "")
#print(linearsearch(list1,64), end = "")


#def binarys (list1,w):
#        if list1.count(w) != 0:
#                leng = len(list1) 
#                b = 0
#                u = leng
#                while True:
#                        
#                        middle = b + ((u-b)//2)
#                        if list1[middle] != w:
#                                if list1[middle] < w:
#                                        b = middle
#                                        print("a")
#                                elif list1[middle] < w:
#                                        u = middle
#                                        print("b")
#                        else:
#                                return middle , " index: ", middle
#                        print("new")
#                        input()
#                        print( u , b, list1[middle], middle, w)
#                        
#        else:
#                return "NO!!!"
#
#       
#        
#print(binarys(list1,2))
#print(binarys(list1,64))
#print(binarys(list1,128))
#
#
#

kontakty = [
       
]
while True:
       x = input("add , exit or show")
       if x == "exit":
              break
       elif x == "show":
              for kontakt in kontakty:
                     print("imie: ",kontakt["imie"],", nazwisko ",kontakt["nazwisko"],", numer telefonu ",kontakt["numer telefonu"])
       elif x == "add":
              print("imie, nazwisko, numer telefonu - kolejność")
              kontakt = {"imie":"","nazwisko":"","numer telefonu":0}
              for el in range(3):
                     
                     y = input()
                     if el == 3:
                            y = int(y)
                     keyss = list(kontakt.keys())
                     kontakt[keyss[el]] = y
              
              kontakty.append(kontakt)
                     




