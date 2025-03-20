first_number = float(input("enter the first number"))
second_number = float(input("enter second number"))
operator = input("enter the operator")
if operator =="+":
    answer = first_number + second_number
    print("the sum of ", first_number, "and ", second_number, "is : ", answer )
elif operator =="-":
   answer = first_number - second_number
   print("the difference of ", first_number, "and ", second_number, "is : ", answer )
elif operator =="*":
    answer = first_number * second_number
    print("the multiplication of ", first_number, "and ", second_number, "is : ", answer )
elif operator =="/":
     answer = first_number / second_number
     print("the division of ", first_number, "and ", second_number, "is : ", answer )
else:
    print("invalid operator")
