class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.tail = 0
        self.head = 1
        self.size = 0
        
#! head pointer increase by 1 for every append

    def append(self, item):
        if not self:
            return None
        else:
            if self.size == self.capacity:
                self.remove()
                self.append(item)
            else:
                self.tail = (self.tail + 1) % self.capacity
                self.queue[self.tail] = item
                self.size = self.size + 1
                
#!  tail pointer decrases by 1 for every read?

    def remove(self):
        if self.size == 0:
            return
        else:
            tmp = self.queue[self.head]
        #! # head - oldest data
        #! if max capacity is reached
        self.size = self.size - 1
        return tmp
        
#! pointers reset if exceed max capacity

    def get(self):
        if self.size is None:
            print("There's nothing in the queue")
        else:
            index = self.head
            vals= []
            for i in range(self.size):
                vals.append(self.queue[index])
                index = (index +1) % self.capacity
            return vals