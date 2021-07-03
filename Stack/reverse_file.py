from stack import *

def reverse_File(filename):
        
    S = Stack()

    orginal = open(filename)

    for i in orginal:
        S.push(i.rstrip('\n'))
    orginal.close

    output = open(filename,'w')
    while not S.isEmpty():
        output.write(S.pop()+'\n')
    output.close


reverse_File('revData.txt')
print(" \n Reverse Done Check the File \n")

