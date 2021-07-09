

class mQueue:

    def __init__(self):
        
        self.queue =[]

    def is_Empty(self):
        if  len(self.queue) <1:
            return '\nQueue Is Empty'
    
    def enqueue(self,item):
        self.queue.append(item)
    
    def dequeue(self):

        if  self.is_Empty:
            return '\nQueue is Empty'
        return self.queue.pop()

    def show_queue(self):

        print(self.queue)
        
    def size(self):
        return len(self.queue)


    def line(self):
        a = print('\n-------------------')
        return a 