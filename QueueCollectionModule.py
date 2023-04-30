import collections

queue = collections.deque()
# HERE ADDING ELEMENT LEFT TO RIGHT
# queue.appendleft(10)
# queue.appendleft(20)
# queue.appendleft(30)
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())

#HERE ADDING THE DATA RIGHT TO LEFT 

queue.append(10)
queue.append(20)
queue.append(30)
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue)

