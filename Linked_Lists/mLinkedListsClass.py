from mNodeClass import *

class LinkedList:

    def __init__(self):
        self.head = Node()

    def get_length(self):
        cnt = 0
        current_node = self.head
        while current_node:
            cnt += 1
            current_node = current_node.next
        return cnt

    def insert_at_begining(self, data):
        # node = Node(data,next address)
        node = Node(data,self.head.next)
        self.head.next = node 
        
    def insert_at(self,location,data):
        if location <0 or location >self.get_length():
            print ('Invalid Address')
            return
        if self.head.next == None:
            self.insert_at_begining(data)
            return

        cnt = 0 
        current_node = self.head
        while current_node:
            if cnt == location - 1:
                node = Node(data,current_node.next)
                current_node.next = node
                break
            current_node  = current_node.next
            cnt +=1

    def insert_at_end(self,data):

        if self.head.next is None:
            node = Node(data,None)
            self.head.next =node
            return

        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next

        current_node.next = Node(data,None)
    
    def search_item(self,search_item):
        current_node = self.head.next
        while current_node != None:
            if current_node.data == search_item:
                print('Item is Found in List : --',current_node.data)
                return
            current_node = current_node.next

        print('OPS! Item is not Found')
    
    def remove_item(self,remove_item):
        pre = self.head
        c_n = pre.next

        while c_n != None:
            if c_n.data == remove_item:
                break
            pre = c_n
            c_n = c_n.next

        pre.next = c_n.next


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


# ll = LinkedList()
# ll.print_LinkedList() 
# ll.insert_at_begining(10)
# ll.insert_at_begining(20)
 
# ll.print_LinkedList()
# ll.get_length()
# ll.insert_at_end(100)
# ll.insert_at_end(200)
# ll.print_LinkedList()
# ll.insert_at(3,300)
# ll.insert_at(4,400)
# ll.print_LinkedList()
