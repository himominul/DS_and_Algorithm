from mNodeClass import *

class InsertAtEnd:

    def __init__(self):

        self.head = Node()

    def insert_at_end(self,data):

        
        if self.head.next is None:
            node = Node(data,None)
            self.head.next = node
            return
        
        cruent_node = self.head
        while cruent_node.next != None:
            cruent_node = cruent_node.next 
        
        cruent_node.next = Node(data,None)

    
     
    def show_list(self):
        if self.head.next is None:
            print('Linked list is Empty ')
            return 
        curent_mode = self.head
        res_str = ''
        while curent_mode  != None:
            res_str = res_str + str(curent_mode.data) + ' --> '
            curent_mode = curent_mode.next


        print(res_str)

ie = InsertAtEnd()

ie.show_list()
#ie.insert_at_end(400)
ie.show_list()
