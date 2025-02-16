print("---SIMPLE CALCULATOR---\n")

no1=float(input("Enter 1st number:"))
no2=float(input("Enter 2nd number:"))
print("\nFor Addition press 1.\nFor Subtraction press 2.\nFor Division press 3.\nFor Multiplication press 4.\n")
choice=int(input("Enter your choice from 1 to 4: "))
if choice==1:
    print(no1+no2)
elif choice==2:
    print(no1-no2)
elif choice==3:
    print(no1/no2)
elif choice==4:
    print(no1*no2)
else:
    print("INVALID INPUT CHOICE")

