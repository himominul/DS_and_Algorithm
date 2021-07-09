


def search(self,search_item):
    current_node = self.head.next
    while current_node != None:
        if current_node.data == search_item:
            print('Item is found in list')
            return
        current_node = current_node.next
    print('OPS! item not found')
     