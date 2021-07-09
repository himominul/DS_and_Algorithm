from mNodeClass import *

class InsertBegining:

    def __init__(self): 
        self.head = Node()

    def  insert_at_begining(self,data):
        node = Node(data,self.head.next)
        self.head.next = node

    def  print_show(self):

        if self.head.next is None:
            print('Linked List is Empty')
            return
        current_node = self.head
        res_str = ''
        while current_node != None:
            res_str = res_str +str(current_node.data) + ' ---> '
            current_node = current_node.next
        print(res_str)



ib = InsertBegining()
ib.insert_at_begining(500)
ib.insert_at_begining(600)
ib.insert_at_begining(900)
print('\n----------------------\n')
ib.print_show()   
print('\n----------------------\n')

