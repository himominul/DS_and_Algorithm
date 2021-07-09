from nodeClass import *

def insert_at(self,location,data):

    if location <0 or location > self.get.length():
        print('Invalaid Location')
        return
    if self.head.next == None:
        node = Node(data,self.head.next)
        self.head.next = node
        return

    cnt =0 
    current_node = self.head.next
    while current_node != None:
        if cnt== location - 1:
            node = Node(data,current_node.next)
            current_node.next = node
            break
    current_node = current_node.next
    cnt += 1