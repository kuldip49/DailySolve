#20.
print("guess my number upto 50")
while i == True:
    num = int(input("enter your number: "))
    if num == 15:
        print(num,"correct guess")
        break
    elif num > 10 and num <= 14:
        print("its close")
    elif num > 16 and num < 20:
        print("its close")
    else:
        print("not even close")