winning_number=56
number=int(input("enter number :"))
if number==winning_number:
    print("You WIN !!!!")
elif number>winning_number:
    print("too high")
else:
    print("too low")