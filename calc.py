# Write a program to do calc operations
 
def add(a,b):
    return a+b
def sub(a,b):
    return a-b    
def mul(a,b):
    return a*b
def div(a,b):
    return a/b   
def modulo(a,b):
    return a%b 
def getInput():
    print("Select your operation:")
    print("1: Add the number")
    print("2: Sub the number")
    print("3: Multiply the number")
    print("4: Divide number")
    print("5: Modulo of division")
    userInput=int(input("Enter your choice: "))
    if(userInput>5 or userInput<1):
        print("check ur eyes")
        return
    a=int(input("Enter ur first num: "))
    b=int(input("Enter ur second num: "))
    if(userInput==1):
        print("Your addition is ",add(a,b))
    elif(userInput==2):  
        print("Your subtraction is ",sub(a,b))  
    elif(userInput==3):
        print("Your multiplication is ",mul(a,b))
    elif(userInput==4):
        print("Your division is ",div(a,b))
    elif(userInput==5):
        print("Your division is",modulo(a,b))

def main():
    getInput()


main()