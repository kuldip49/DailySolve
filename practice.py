a = input("Enter your string")
v = "aeiouAEIOU"
for i in a:
    if i in v:
        print("vowel is : ",i,end='')