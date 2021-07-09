from mLinkedListsClass import *

def line():
    l = print('------------------------')
    return l

#creating object in mLinkedListsClass

ll = LinkedList()


line()
ll.print_LinkedList()
line()

# insert Item at Begining 
ll.insert_at_begining(10)
ll.insert_at_begining(20)
ll.insert_at_begining(30)
print("\nAfter  Insert Item at Begining")
line()
ll.print_LinkedList()

#insert Item at End
ll.insert_at_end(100)
ll.insert_at_end(200)
ll.insert_at_end(300)
print("\nAfter  Insert Item at End")
line()
ll.print_LinkedList()
line()

#Searching  Item in list
print('Searching Item')
line()
ll.search_item(30)
ll.search_item(500)
line()

#insert Item at  spacific Position 
ll.insert_at(4,400)
ll.insert_at(5,500)
print('\nAfter Insert at 4 and 5 Position ')
line()
ll.print_LinkedList()

#Removing item in the List 
ll.remove_item(200)
ll.remove_item(20)
print('\nAfter Removing Item Item ')
line()
ll.print_LinkedList()
line()






