#Make a simple calculator with basic arithmetic operations.Prompt the user to input two numbers and an operation choice.Perform the calculation and display the result.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
choice=int(input("Enter the operation you want to perform\nPress 1 for sum\nPress 2 for subtraction\nPress 3 for multiplication\nPress 4 for division\nPress 5 for floor division\nPress 6 for exponential power\n"))
match choice:
  case 1:
    print("The sum of the numbers is",a+b)
  case 2:
    choice=int(input("Press 1 for a-b\nPress 2 for b-a\n"))
    match choice:
      case 1:
        print("The subtraction of a and b is",a-b)
      case 2:
        print("The subtraction of b and a is",b-a)
  case 3:
    print("The multiplication of a and b is",a*b)
  case 4:
    choice=int(input("Press 1 for a/b\nPress 2 for b/a\n"))
    match choice:
       case 1:
         if(b!=0):
           print("The division of a by b is",a/b)
         else:
           print("Division by 0 is not valid operation")
       case 2:
         if(a!=0):
           print("The division of b by a is",b/a)
         else:
           print("Division by 0 is not valid operation")
  case 5:
    choice=int(input("Press 1 for a//b\nPress 2 for b//a\n"))
    match choice:
       case 1:
         if(b!=0):
           print("The floor division of a by b is",a//b)
         else:
           print("Floor division by 0 is not valid operation")
       case 2:
         if(a!=0):
           print("The floor division of b by a is",b//a)
         else:
           print("Floor division by 0 is not valid operation")
  case 6:
     choice=int(input("Press 1 for a**b\nPress 2 for b**a"\n))
     match choice:
       case 1:
         print("The exponential of a to b is",a**b)
       case 2:
         print("The exponential of b to a is",b**a)
  case _:
     print("Invalid Choice")
    
        
