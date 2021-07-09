
class Node:

    def __init__(self, data='Head', next = None ):
        self.data = data
        self.next = next


class LinkedList:
     

    def  __init__(self):
        self.head = Node()

    def get_length(self):
        cnt =0
        current_node = self.head
        while current_node:
            cnt +=1
            current_node = current_node.next
        return cnt

    def insert_at_begining(self,data):
        #node = Node(Data,nextAddress)
        node = Node(data,self.head.next)
        self.head.next = node
        print('Insert Done')

    def insert_at (self, index,data):
        if index <0 or index >self.get_length():
            print('Invalid index')
            return
        
        if index == 0:
            self.insert_at_begining(data)
            return

        cnt =0
        current_node = self.head
        while current_node:
            if cnt == index - 1:
                node = Node(data,current_node.next)   
                current_node.next = node
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

    def insert_at_end(self,data):

        if self.head.next is None:
            node = Node(data,None)
            self.head.next = node
            return
        
        cruent_node = self.head
        while cruent_node.next != None:
            cruent_node = cruent_node.next 
        
        cruent_node.next = Node(data,None)



ll = LinkedList()

ll.print_LinkedList() 
# ll.insert_at(1,100)
# ll.insert_at(2,200)
# ll.insert_at(3,300)
# ll.insert_at(4,400)

# ll.print_LinkedList()
# ll.insert_at(2,100)
# ll.print_LinkedList()
# ll.insert_at(20,1100)
# ll.print_LinkedList()

ll.insert_at_end(200)
ll.print_LinkedList

