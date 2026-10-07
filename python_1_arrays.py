import array as ar

#integer type array:

a= ar.array('i', [1,2,3])
print("the original array we just created is : ", end  = " ")
for i in range(0,3):
    print(a[i], end = " ")

print()
#double type:

b = ar.array('d', [2.5, 6.0, 7.8])
print("the original array is : ", end = "     ")
for i in range(len(b)):
    print(b[i], end = "  ")


#creating an empty arrays and filling it:
print()

empty_array = ar.array('i')
empty_array.append(1)
empty_array.append(2)
empty_array.append(3)

print(empty_array)

print()

arr = ar.array('i', [40, 50, 70, 80])
for i in range(len(arr)):
    print(arr[i])

print()

#slicing an array in python:

print(arr[1:3])

print(len(arr))

print(arr[-1])

#searching through an array:
#to searcxh using the index of the values:
#this means the values will be fetched based on the the postion on which that index value will be matched.
print(arr.index(40))