


def get_length (self):
    cnt =0 
    current_node = self.head
    while current_node:
        cnt += 1
        current_node = current_node.next
    return cnt 
    
