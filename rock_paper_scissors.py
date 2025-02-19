print("Welcome to the game of\n --ROCK, PAPER AND SCISSORS!--")
for i in range(3):
    import random
    print("\nYour choices are-\n1 for ROCK\n2 for PAPER\n3 for SCISSORS\n")
    user_choice=int(input("Enter your choice:"))
    if user_choice>=3 or user_choice<=0:
        print("Invalid Choice!")
    elif user_choice==1:
        print("You chose ROCK")
    elif user_choice==2:
        print("You chose PAPER")
    elif user_choice==3:
        print("You chose SCISSORS")

    # computer's choice
    print("Now it's Computer's Turn--")
    computer_choice=random.randint(1,3)
    if computer_choice==1:
        print("Computer chose ROCK")
    elif computer_choice==2:
        print("Computer chose PAPER")
    elif computer_choice==3:
        print("Computer chose SCISSORS")
    # game starts
    if computer_choice==user_choice:
        print("It's a draw.")
    elif computer_choice==1 and user_choice==3:
        print("You Lose.")
    elif user_choice==1 and computer_choice==3:
        print("You win.")
    elif computer_choice>user_choice:
        print("You Lose.")
    elif user_choice>computer_choice:
        print("You Win.")
    print("Well Played!")
    ag=input("Would you like to play again? (yes/no): ")
    if ag=="YES"or ag=="yes":
        continue
    else:
        print("--THANK YOU FOR PLAYING--")
        break