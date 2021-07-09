from  nodeClass import *


def insert_at_begining(self,data):

    #node = Node(Data,nextAddress)
    node = Node(data,self.head.next)
    self.head.next = node
    

    