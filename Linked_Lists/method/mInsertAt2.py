from mNodeClass import *

class InsertAt:

    def __init__(self) :
        self.head = Node()


    def get_length(self):
        cnt =0
        current_node = self.head
        while current_node:
            cnt +=1
            current_node = current_node.next
        return cnt


    def insert_at(self,index,data):

        if index < 0 or index >self.get_length():
            print('Invalid Index')
            return

        if index == 0:
            node = Node(data,self.head.next)
            self.head.next = node
            return

        cnt = 0 
        current_node = self.head
        while current_node:
            if cnt == index -1:
                node = Node(data,current_node.data)
                current_node.next = current_node
                break
            current_node = current_node.next
            cnt += 1

    
    def print_LinkedList(self):
        if self.head.next is None:
            print('Linked list is Empty ')
            return 
        curent_mode = self.head
        res_str = ''
        while curent_mode  != None:
            res_str = res_str + str(curent_mode.data) + ' --> '
            curent_mode = curent_mode.next


        print(res_str)

        
ia = InsertAt()

ia.print_LinkedList()
ia.insert_at(0,200)
ia.print_LinkedList()
