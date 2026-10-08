#basic syntax fo these codes:

for n in range(2,10):
    for x in range(2,n):
        if n%x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

print()

for num in range(2,20):
    if num%2 == 0:
        print(f"found an even number : {num}")
        print()
        continue
    print(f"found an odd number {num}")
    print()

"else clause on the loops : "

#else clause app:

for n in range(2,20):
    for x in range(2,n):
        if n % x == 0:
            print(n, "equals", x, "*", n//x)
            break
    else:
        print(n , "it is a prime number")

# pass statements:

"""
this is used whn we want the code but no actions on it 
for examples:

"""

while True:
    pass

class MyWEmptyclaSS:
    pass

def initlog(*args):
    pass

#match statements

def Http_error(status):
    match status:
        case 400:
            return "bad request"
        case 404:
            return "not found broo"

        case _:
            return "something wrong with the internet"

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("enter your choices of red, blue and green: "))

match color:
    case Color.RED:
        print(" i see red")

    case Color.GREEN:
        print("i see green")

    case Color.Blue:
        print("i see blue")


def ask_ok(prompt, retries = 4, reminder = 'please try again'):
    while True:
        reply = input(prompt)
        if replies in {'y', 'yes'}:
            return True
        if reply in {'n', 'no'}:
            return False
        retries = retries - 1
        if retries< 4:
            raise ValueError(' invalid user response ')
        print(reminder)

#keyword arguements = *kwargs 


def parrot(voltage, state = ' a stiff', action = 'voom', type = 'norweigan Blue'):
    print("--this parrot would'nt", action, end = " ")
    print("if you put ", voltage, "volts through it.")
    print("--lovely plumage, the", type)
    print("--its state", state, "!")

parrot(1000)
parrot(voltage = 1000)
parrot(voltage = 1000, action = "vooooom")
parrot("a thousand ", state = "pushing up the daisies")


