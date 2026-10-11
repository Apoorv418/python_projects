"""
A for loop takes each item of a sequence (iterable) one at a time and runs the block for it.
Python handles the counter and the stopping for you, which makes it safer than while.
"""
#basic syntax:
for fruit in ["apple", "banana", "cherry"]:
    print("i like fuits: ", fruit)

#looping by index vs byt value:

colors = ["red", "Blue", "Green"]
#by value:
for i in colors:
    print(i)

for i, c in enumerate(colors):
    print(i, c )

#enumerate with a custom start:

for i, c in enumerate(colors, start = 1):
    print(i, c  )

#power tools: enumerate, zip, reversed and sorted:

names = ["Apoorv", "Rohan", "Kashish", "Aryan"]
scores = [100, 90, 80, 70]

#zip functions is used to walk to list in parallel:

for n, s in zip(names, scores):
    print(f"{n} scored ",s)

#looping over dictionaries:

ages = {"Ana": 30, "Ben": 40, "Cara": 50}

 #to get keys:

 #key by default:

for key in ages:

    print(key, end = " ")
print()

#values by default:

for value in ages.values():
    print(value, end = " ")
print()   

for key, value in ages.items():
    print(f"{key} is {value}")


#Nested loops:

"""
A loop inside a loop.
The inner loop runs completely for every single pass of the outer loop. 
Total
runs = outer count × inner count.
"""
for i in range(1,4):
    for j in range(1,4):
        print(f"{i}x{j} = {i*j}", end = " ")
    print()

#pattern printing:

n = 5
for rows in range(1, n+1):
    print("*" * rows)

print()

#pyramid pattern:

for row in range(1, n+1):
    print(" " * (n-row) + "*" * (2* row - 1))
print()

#  tables formatted:

for i in range(1, 6):
    for j in range(1,11):
        print(f"{i*j}", end = " ")
    print()

#word frquency counter:

text = "the cat and the hat and the bat"
count = {}
for i in text.split(): 
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for k, v in count.items():
    print(f"{k} is {v} many times")






