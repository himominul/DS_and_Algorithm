
from mQueueClass import *

q = mQueue()


q.is_Empty()

q.enqueue(100)
q.enqueue(50)
q.enqueue(10)
q.enqueue(5)
print('After Enqueu ')
q.line()
q.size()
q.show_queue()
print('After DeQueue \n')
q.line()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.show_queue()
