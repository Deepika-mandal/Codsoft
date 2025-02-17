print("...WELCOME TO PASSWORD GENERATOR...")
for p in range(3):
    import random
    a=int(input("Enter length of Password:"))
    print("Your desired length of Password is:",a)
    print("Hence, your auto generated password is: ")
    ch='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&'
    pw=""
    for i in range(a):
        pw=pw+random.choice(ch)
    print(pw)
    ag=input("Would you like to try it again? (YES/NO): ")
    if ag=="YES" or ag=="yes":
        continue
    elif ag=="NO" or ag=="no":
        print("**Thanks for using Password Generator**")
        break
    else:
        print("Invalid Response.")
        break
