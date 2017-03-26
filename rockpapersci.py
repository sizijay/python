from random import randint

def game(choice):
    com=randint(1,3)
    if (choice==com):
        print("Oops.. Try Again..Same to Same!\n")
    elif (choice==1):
        if (com==2):
            print("You LOSE!!!!\tPaper covers Rocks.....(Computer choice=Paper)\n")
        else:
            print("You WON!!!!\tRock breaks Scissors.....(Computer choice=Scissor)\n")
    elif (choice==2):
        if (com==1):
            print("You WON!!!!\tPaper covers Rocks.....(Computer choice=Rock)\n")
        else:
            print("You LOSE!!!!\tScissor cuts Papers.....(Computer choice=Scissor)\n")
    else:
        if (com==1):
            print("You LOSE!!!!\tRock breaks Scissors.....(Computer choice=Rock)\n")
        else:
            print("You WON!!!!\tScissor cuts Papers.....(Computer choice=Paper)\n")
    print("\n\t\t***********************************\n")

print("\n\t\t---Welcome to ROCK-PAPER-SCISSOR Game---\n\nEnter your Choice(1,2,3)\n\t1 = Rock\n\t2 = Paper\n\t3 = Scissor\n\nEnter 'x' to TERMINATE")
a=["1","2","3"]
while True:
    cho=input(">>>")
    if (cho=="x"):
        exit()
    elif (cho==""):
        continue
    elif (cho in a):
        game(int(cho))
    else:
        print("\nPlease enter 1 or 2 or 3......\n")
        continue
