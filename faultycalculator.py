# it is simple program to make faulty calculator
# In this some solution give wrong answer and rest of all give right answer
# like: 45*3=555 & 56+9=77 & 56/6=4 in this solution give only wrng answer
# after this its work like calculator

# enter here value
num1=int(input("Enter 1st number :"))
num2=int(input("Enter 2nd number :"))
opr=input("enter here +,-,/,* :")

if num1==45 and num2==3 and opr=='*': #given in heading 45*3=555
    print("Answer is :555")

elif num1==56 and num2==9 and opr=='+': ##given in heading 56+9=77
    print("Answer is :77")

elif num1==56 and num2==6 and opr=='/': ##given in heading 56/6=4
    print("Answer is :4")   
# from here its work like calculator without any fault
elif opr=='+': #addition
    total=num1+num2
    print("Answer is",total) 

elif opr=='-': #substraction
    total=num1-num2
    print("Answer is",total) 

elif opr=='*': #multiplication
    total=num1*num2
    print("Answer is",total) 

elif opr=='/': #division
    total=num1/num2
    print("Answer is",total)         