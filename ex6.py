#show ticket pricing
# 1 to 3 free 
# 4 to 10 100 
# 10 to 15 150 
# 15 above 200

age=input("enter your age :  ")
age = int(age)
if 1<=age<=3:
    print("free")
elif 4<=age<=10:
    print("100")
elif 10<=age<=15:
    print("150")
else:
    print("200")
