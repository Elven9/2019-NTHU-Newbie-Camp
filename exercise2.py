# If else, Input(), Int() Learning.

# TASK 1: Take values of length and breadth of a rectangle from user 
# and check if it is square or not.

width = int(input("Rectangle width: "))
height = int(input("Rectangle height: "))

if width == height:
    print("Yes, the rectangle is square.")
else:
    print("Oops, it is not square.")

# TASK 2: Take two int values from user and print greatest among them.
input1 = int(input("Input 1: "))
input2 = int(input("Input 2: "))

if input1 > input2:
    print(input1)
elif input1 < input2:
    print(input2)
else:
    print("Two inputs are equal.")