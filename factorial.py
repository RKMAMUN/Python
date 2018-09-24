fact = 1
num1 = int(input("Enter a Number: "))

if(num1<=0):
    print("Error")
else:
    for i in range(1,(num1+1)):
        fact = fact*i
    print("The factorial of",num1,"is: ",fact)
