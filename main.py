from calculator import *

selection = int( input("\nSelect your calculator operation: \
                        \n1. Addition\
                        \n2. Subtraction\
                        \n3. Multiplication\
                        \n4. Division\
                        \nOther. EXIT()\
                        \n\nChoice:"))

if 0<selection<5:
    num1, num2 = map(int, input("\nProvide your 2 values:").split(' '))

if selection == 1:
    print("The result is:" +str(add(num1,num2))+"\n")
elif selection == 2:
    print("The result is:" +str(subtract(num1,num2))+"\n")
elif selection == 3:
    print("The result is" +str(multiply(num1,num2))+"\n")
elif selection == 4:
    temp = divide(num1,num2)
    if temp != "Cannot divide by zero":
        print("The result is" +temp+"\n")
    else:
        print(temp+"\n")
else:
    print("\n\n This is the end of the program. HaHaHa\n\n")
    powerof()
