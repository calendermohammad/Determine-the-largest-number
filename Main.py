# function definition
def prin_maximum(num01, num02, num3):
    if num01 > num02 and num01 > num3:
        result = num01
    elif num02 > num01 and num02 > num3:
        result = num02
    else:
        result = num3
    print("Max number between %d, %d and %d is %d" %(num01, num02,num3, result))
# function call
num01 = int(input("Please Enter Number 1: "))
num02 = int(input("Please Enter Number 2: "))
num3 = int(input("Please Enter Number 3: "))
printmaximum(num01, num02, num3)
 
