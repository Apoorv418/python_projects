"""
A while loop repeats its block as long as the condition is True. 
You use it when you do not
know in advance how many repetitions you need.
"""
count = 1
while count <= 10:
    print("count is ", count)
    count += 1
print("loop finished")

#counting patterns:

n = 5
while n> 0:
    print(n, end = " ")
    n -= 1
print("liftoff")

#poweers of 2 below 100:

p = 1
while p< 100:
    print(p, end = " ")
    p *= 2
print()

# sum of 1 ...................100

total = 0
i = 1
while i<=100:
    total += i
    i += 1

print('the sum is ', total)

#input validation:

age = int(input("Enter your age"))
while age< 1 or age> 120:
    print("invalid age")
    age = int(input("enter your age (1-120)"))
    print("valid age")

#break and continue:

"""
break:
Exit the loop immediately. Execution continues after the loop

continue":
Skip the rest of THIS iteration; jump back to the condition test
"""

# printing only odd numbers:

i = 0
while i<10:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end = " ")
print()

#while algorithms:

#digit sum and reversing a number:

n = 4279
digit_sum = 0
reversed_d = 0

while n > 0:
    d = n%10 #used to get the last digit in the number:
    digit_sum = digit_sum + d #or digit_sum += d
    reversed_d = reversed_d*10 + d
    n //= 10 #used to remove the last digit 

print(digit_sum)
print(reversed_d)

#binary search (guess a number between 1 to 100):

secret = 50
low = 1
high = 100
guesses = 0

while low<= high:
    mid = (low + high)//2
    guesses += 1
    if mid == secret:
        print(f"found {mid} in {guesses} guesses")
        break
    elif mid<secret:
        low = mid + 1
    else:

        high = mid - 1




    
    


