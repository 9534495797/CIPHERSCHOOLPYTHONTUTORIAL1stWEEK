x=input("take value b/w 1 to 100")
x=int(x)
winning_number =27
if x==winning_number:
    print("congrats you win")
else:
    if x < winning_number:
        print("lower value")
    else:
        print("too high")