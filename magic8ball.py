import random as rnd

question = input("Ask me anything?")

answer = rnd.randint(1, 8)
if answer == 1:
    print("It is certain")
elif answer == 2:
    print("Looks Good to me")
elif answer == 3:
    print("Better luck next time...")
elif answer == 4:
    print("Possible ")
elif answer == 5:
    print("Never in a million years")
elif answer == 6:
    print("Concentrate and maybe I'll answer")
elif answer == 7:
    print("The cosmos says no")
elif answer == 8:
    print("That is what you waste my magic on?")
print("The end or is it???")