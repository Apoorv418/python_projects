#using liosts as stacks:

stack = [1,2,3]
stack.append(4)
stack.append(5)
stack
print(stack)

#using lists as queue:

from collections import deque

queue = deque(["eric", "johnson", "michael"])
queue.append("john")
queue.append("doe")

#to get the first elemeents we do :

queue.popleft
print(queue)

queue.popleft
print(queue)

#list comprehension = list comprehension provide a summarise way of writing functions when creating objects

squares = []

for x in range(10):
    squares.append(x**2)

print(squares)

#or we can sue lambda for these expressions:

squares_ = list(map(lambda x: x**2, range(12)))
print(squares_)