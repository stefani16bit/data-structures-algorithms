
class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    def isEmpty(self):
        return len(self.queue) == 0
    
    def isFull(self):
        return len(self.queue) == self.capacity

    def enqueue(self, values):
        if self.capacity > len(self.queue) + len(values):
            for value in values:
                self.queue.append(value)
        else:
            raise Exception("Error: Exceeded capacity")
    
    def dequeue(self):
        if not self.isEmpty():
            self.queue.pop(0)

    def front(self):
        if not self.isEmpty():
            return self.queue[0]

    def back(self):
        if not self.isEmpty():
            return self.queue[len(self.queue) - 1]
    
queue = Queue(10)
queue.enqueue([2,5,3,8])
print(queue.isEmpty()) #False
print(queue.isFull()) #False
queue.dequeue()
print(queue.queue) #[5,3,8]
print(queue.front()) #[5]
queue.enqueue([9])
print(queue.back()) #[9]



