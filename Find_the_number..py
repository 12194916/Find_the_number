import random


def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"I thought a number from 1 to {x}, can you find it? ", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print("Wrong. My number is bigger than it. Please try again:", end="")
        elif taxmin > tasodifiy_son:
            print("Wrong. My number is smaller than it. Please try again:", end="")
        else:
            break

    print(f"Congratulations. You have found with {taxminlar} tries")
    return taxminlar


def pc(x=10):
    input(f"Guess a number from 1 to {x}. I will try to find it.")
    bottom=1
    up=x
    guesses=0
    while True:
        guesses+=1
        if bottom!=up:
            guess=random.randint(bottom,up)
        else:
            guess=bottom
        answer=input(f"That number is {guess}: Correct(c), that number is bigger than it(+), that number is smaller than it(-)".lower())
        if answer =="-":
            up=guess-1
        elif answer =="+":
            bottom=guess+1
        else:
            break
    print(f"I have found with {guesses} tries!")
def play(x=10):
    more=True
    while more:
        print(sontop(x))
        print(pc(x))
        more=int(input("Do we play more? Yes(1) No(0)"))
play()


