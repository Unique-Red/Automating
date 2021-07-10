#program to make a simple calculator

#this function adds two numbers
def add(x,y):
    return x + y

#this function subtracts two numbers
def subtract(x,y):
    return x-y

#this function divides two numbers
def division (x,y):
    return x/y

#this functions multiplies two numbers
def multiply(x,y):
    return x*y

print("select operation")
print("1.add")
print("2.subtract")
print("3.divide")
print("4.multiply")

while True:
    #take input from the user 
    choice = input("enter choice (1/2/3/4)")
    if choice in ('1','2','3','4'):
        num1 = float(input("enter first number : "))
        num2 = float(input("enter second number : "))

        if choice == '1':
            print(num1, '+' ,num2 , "=" , add(num1,num2))
        elif choice == '2':
            print(num1 , '-' , num2 , " =" , subtract(num1,num2))
        elif choice == '3':
            print(num1 ,'/',num2, '=', division(num1,num2))
        elif choice == '4':
            print(num1,'*',num2,'=',multiply(num1,num2))
        break
    else:
        print("invalid output")
