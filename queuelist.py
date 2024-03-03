#list as queue
from collections import deque
list=["apple","mango","orange"]
queue=deque(list)
queue.append("pineapple")
print(queue)
queue.popleft()
print(queue)
