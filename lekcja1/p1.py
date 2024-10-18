liczby = []
for x in range (1,101):
    if x % 3 == 0 and x % 5 == 0:
        liczby.append("FizzBuzz")
    elif x % 3 == 0:
        liczby.append("Fizz")
    elif x % 5 == 0:
        liczby.append("Buzz")
    else:
        liczby.append(x)


print(liczby)






