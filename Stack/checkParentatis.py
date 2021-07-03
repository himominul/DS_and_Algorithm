from stack import *

stk = Stack()

class CheckPar:
        
    def check(obj, mList):

        left = '('
        right = ')'

        for item in mList:
            if item == left:
                stk.push(item)
            elif( item == right ):
                if stk.isEmpty():
                    return False

                if right.index(item) != left.index(stk.pop()):
                 return False
                    
        if stk.isEmpty():
            return 'Its Matched : '
        else:
            return 'Its Not Matched : '
