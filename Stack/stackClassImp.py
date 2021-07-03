from stack import *

#Create the Class  Object
s=Stack()


print(s.isEmpty())

s.push(4)
s.push('dog')
s.push('Cat')
s.push(8.4)

print('\nAfter Pushing the Data')
print('How Many Item in Stack : ',s.size())
sh = s.show()
print(s.pop())
print(s.pop())
print('\nHow Many Item in Stack : ',s.size())
sh = s.show()
print(s.pop())
print(s.pop())
sh = s.show()

