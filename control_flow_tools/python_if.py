"""
The if statement evaluates a Boolean condition. If the condition is True, 
its corresponding block of code runs once. 
If it is False, the code block is skipped.
"""
#basic syuntax:

x = 15

if x>20:
    print("it is greater than 20")

elif x> 10:
    print("x is greatere than 10 but else less than 20")

else:
    print("it  is very small mannn")

#now we will start focusing on the if, for and while loops:

age = 25
has_ticket = True
is_banned = False
if age>= 18 and has_ticket and not is_banned:
    print("entry allowed")
else:
    print("YOU ARE not allowed")

#chained comparison(python superpowers):

x = 15
print(10<x<20)

age = 30
if 18<= age <= 65:
    print("This employee falls in working age")



name = ""

if not name:
    print("the name is empty")

cart = ["milk", "bread"]
if cart:
    print("cart has", len(cart), "items")


#nested items:

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("login success")
    else:
        print("wrong password")

else:
    print("unknown user")


def check_login(username, password):
    if username != "admin":
        print("unkown user")

    if password != "1234":
        print("invalid credentials")

    return "login success"

print(check_login("admin", "12234"))
print(check_login("admin", "1234"))

#Ternary (one-line if/else):

age = 17
status = "adult" if age >= 17 else "minor"
print(status)

n = -4
print("abs value :", n if n >= 0 else -n)

# matching case:
def describe(day):
    match day:
        case "Sat"| "Sun":
            return "weekend"

        case "Mon"|"Tue"|"Wed"|"Thu"|"Fri":
            return "weekday"

        case _:
            return "not a day"

print(describe("Sat"))
print(describe("gbfugbufweufhu"))