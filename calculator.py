print("----Welocome to the mini arithmatic calculator!----")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

while True:
    Operator = int(input("Enter operator: \n1-for addition \n2-for subtraction \n3-for division \n4-for multiplication\n5-for closing calculator\n"))

    if Operator==1:
        print("Addition of 2 number is: ",num1+num2)

    elif Operator==2:
        print("Subtraction of 2 number is: ",num1-num2)

    elif Operator==3:
        print("Division of 2 number is: ",num1/num2)

    elif Operator==4:
        print("Multiplication of two number is: ",num1*num2)
    
    elif Operator==5:
        print("---Calculator Closed!---")
        break

    else:
        print("Please Enter Valid Input!")    
