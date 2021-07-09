
def remove_item(self,remove_item):
    pre = self.head 
    c_n = pre.next

    while c_n != None:
        if c_n.data == remove_item:
            break
        pre = c_n
        c_n = c_n.next
    pre.next = c_n.next
    