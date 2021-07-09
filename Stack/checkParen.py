from checkParenthesesClass import *

#Create CheckPar  class Object
ch =CheckPar()

while True:

    pw =input('Enter your Parentatis : ')

    if ch.check(pw):
        print('\nParentheses Is  Mathced : ',pw,'\n')
    else:
        print('\nParentheses Is not Mathced : ',pw,'\n')
