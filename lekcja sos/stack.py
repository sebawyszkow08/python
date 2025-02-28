import random

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        #try:
        #    item = int(item)
        #    if len(str(item)) == 9:
                self.stack.append(item)
        #except:
        #    pass
        

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    




    def is_palidrom(self,item):
        self.dlogosc = len(item)//2
        
        for i in range(self.dlogosc):
            if item[i] == item[-i-1]:
                print(f"{item[i]} == {item[-i-1]}  " , end="")
            else:
                print(f"{item[i]} != {item[-i-1]}  " , end="")
                return False    
        return True


stack = Stack()

print(stack.is_palidrom("kajak"))
print(stack.is_palidrom("nieee"))
print(stack.is_palidrom("mkljm"))
print(stack.is_palidrom("otomoto"))

'''


stack = Stack()

zmienna0 = stack.size()
print(zmienna0)

stack.push("a")
stack.push("b")
stack.push("123123123")
stack.push("334334567")

zmienna1 = stack.pop()
print(zmienna1)

zmienna2 = stack.peek()
print(zmienna2)

zmienna3 = stack.is_empty()
print(zmienna3)

zmienna4 = stack.size()
print(zmienna4)



class Hist:
    def __init__(self):
        self.hist = []

    def addhistory(self,item):
        self.hist.append(item)


    def previouspage(self):

        if len(self.hist) >2:
            
            self.hist.append(self.hist[-2])

        else:
            print("there is no previous page!!!")

    def clearhistory(self):
        self.hist = []

    def showhistory(self):
        print(self.hist)






hist = Hist()
strony = ["stronaA","gugle","jutjub","łikipedia","darmowegry","pracedomowe","fejsbuk"]
while True:
    print("type:  next , previous , clear or show")
    choice = input()
    match choice:

        case "next":
            hist.addhistory(random.choice(strony))

        case "previous":
            hist.previouspage()

        case "clear":
            hist.clearhistory()

        case "show":
            hist.showhistory()
            
'''


class BrowserHistory:
    def __init__(self):
        self.history = Stack()
        self.current_page = None
 
    def go_to_page(self,url):
        self.history.push(self.current_page)
        self.current_page = url
    def go_back(self):
        previous_page = self.history.peek()
        if previous_page is not None:
            self.current_page = previous_page
 
    def print_history(self):
        print("Current page:", self.current_page)
        print("History")
        for page in reversed(self.hstory.stack):
            print(page)
































