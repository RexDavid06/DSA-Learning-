# A Queue is a First In First Out Data structure...........FIFO
'''
Two functions in QUEUE

Enqueue- add an item to the end of a line

Dequeue- remove an item from the front of the line

'''
from collections import deque # Double Ended Queue

my_queue = deque()
my_queue.append(50)
my_queue.append(5)
my_queue.append(60)
my_queue.appendleft(809)
# my_queue.pop()
my_queue.popleft()
print(my_queue)