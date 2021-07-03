from stack import *

class Stack:

    def __init__(self):
        
        self.items = []

    def isEmpty(self):
       if self.items == []:
           return '\nStack Is Empty'

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            print("Empty")
        return  self.items.pop() 

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def top(self):
       if self.isEmpty:
           return False
       return self.data[-1]

    def show(self):
        if self.isEmpty !=[]:
            print(str(self.items))
                    
        
        
       

