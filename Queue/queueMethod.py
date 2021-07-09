def __init__(self) -> None:
        
        self.queue =[]

def is_Empty(self):
    if  len(self.queue) <1:
        return 'Queue Is Empty'
    
def enqueue(self,item):

    self.queue.append(item)
    
def dequeue(self):

    if  self.is_Empty:
        return None
    return self.queue.pop(0)

def show_queue(self):

    print(self.queue)
        
def size(self):
    return len(self.queue)