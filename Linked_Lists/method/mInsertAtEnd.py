from mNodeClass import *

def insert_at_end(self,data):
    
    if self.head.next is None:
        node = Node(data,None)
        self.head.next = node
        return
    current_node = self.head
    while current_node. next != None:
        current_node = current_node.next
    
    current_node.next = Node(data,None)
    