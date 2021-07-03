
def create_stack():
    stack = []
    return stack

def  is_Empty(stack):
    return len(stack) == 0

def push (stack,item):
    stack.append(item)
    print('item Pushed',item)

def pop(stack):
    if is_Empty(stack):
        return ' Stack Is Empty'
    return stack.pop()



stack = create_stack()
push(stack,str(1))
push(stack,str(2))
push(stack,str(9))
push(stack,str(5))
print('-------------------')
print(str(stack))
print('\n_____After POP----')
pop(stack)
print(stack)

