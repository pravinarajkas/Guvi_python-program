num=int(input("Enter an integer:"))
count=0
while num>0:
    r=num%10
    count=count+1
    num=num//10
print("Count:",count)
