#8/2/2020
"""
Problem Statement:
Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out)
data structure with the following methods: enqueue, which inserts an element into the
queue, and dequeue, which removes it.
"""
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        poppedItem = self.items.pop()
        return poppedItem
        
s1 = Stack()
s2 = Stack()

class QueueUsingTwoStacks:
    def __init__(self):
        pass
        #Could probably add globals function here to create 2 stacks when creating queue, then
        #remove s1,s2 = Stack() lines above. This would allow for multiple queues to be used
        #at the same time. Something like:
        #globals()[str(queueName) + "_s1"]= Stack()  --> Create first stack for each queue created
        #globals()[str(queueName) + "_s2"]= Stack()  --> Create second stack for each queue created
        
    def enqueue(self, item):
        s1.push(item) #Simply store enqueued items in stack 1 until dequeued. Second stack not needed yet.
    
    def dequeue(self):
        for i in range(0, len(s1.items), 1): #Transfer all of stack 1 items into stack 2.
            transferItem = s1.pop()
            s2.push(transferItem)
        dequeuedItem = s2.pop() #Remove last item from stack 2 (which was originally first item in stack 1).
        for i in range(0, len(s2.items), 1): #Transfer all of stack 2 back into stack 1.
            transferItem = s2.pop()
            s1.push(transferItem)
        return dequeuedItem
            
#Verification:
q = QueueUsingTwoStacks()
q.enqueue(5)
q.enqueue(3)
q.enqueue(9)
print(vars(s1)) #Prints {'items': [5, 3, 9]}
print(q.dequeue()) #Prints 5
print(vars(s1)) #Prints {'items': [3, 9]}