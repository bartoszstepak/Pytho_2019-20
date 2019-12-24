print("\n10.3")

class Stack:

    #stack can store values from 1 to size-1

    def __init__(self, size):
        self.stack = [None] * size
        self.stack_existing_status = [False] * size
        self.last_element = 0

    def __str__(self):
        return str(self.stack)

    def push(self, value):
        if self.last_element < len(self.stack) and not self.exist(value):
            self.stack[self.last_element] = value
            self.last_element += 1
            self.stack_existing_status[value] = True


    def pop(self):
        if self.last_element < 0:
            raise Exception('empty stack')
        else:
            last = self.stack[self.last_element - 1]
            self.stack[self.last_element - 1] = None
            self.last_element -= 1;
            return last

    def exist(self, value):
        if value < len(self.stack_existing_status):
            return self.stack_existing_status[value]
        else:
            self.stack_existing_status[False] * value


stack = Stack(10)

for i in range(8):
    stack.push(i)

stack.push(3)
print(stack)
x = stack.pop()
print("poped -", x)
print(stack)
stack.push(9)
print('pushed - 9')
print(stack)


print("\n10.6")

class PriorityQueue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        return self.items.pop(maxi)

    def increase(self, value):
        for i in range(1, len(self.items)):
            self.items[i] += value


priority_queue = PriorityQueue()
priority_queue.insert(2)
priority_queue.insert(8)
priority_queue.insert(5)
priority_queue.insert(3)
priority_queue.insert(1)

print ("Priority Queue: {}".format(priority_queue))

priority_queue.increase(2)
print ("Increase priority: {}".format(priority_queue))

priority_queue.insert(2)
priority_queue.insert(1)
print ("Add new items to queue: {}".format(priority_queue))

priority_queue.remove()
priority_queue.remove()
print ("Take off 2 items from queue by highest priority: {}".format(priority_queue))

print("\n10.8")

import random

class RandomQueue:

    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        if not self.is_empty():
            x = random.randint(0, len(self.items) - 1)
            value = self.items[x]
            if x is len(self.items) - 1:
                self.items.pop()
            else:
                self.items[x] = self.items.pop()
            return value

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False
    
    def clear(self):
        self.items = []

    def __str__(self):
        return str(self.items)


random_queue = RandomQueue()
random_queue.insert(1)
random_queue.insert(3)
random_queue.insert(2)
random_queue.insert(1)
random_queue.insert(6)
random_queue.insert(4)

print("Take off random items from queue {}: ".format(random_queue))
print(random_queue.remove())
print(random_queue.remove())
print(random_queue.remove())
print(random_queue.remove())

print("Queue after taking off random elements: {}".format(random_queue))
