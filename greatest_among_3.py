x=int(input("Enter the input 1:"))
y=int(input("Enter the input 2:"))
z=int(input("Enter the input 3:"))
if x>y and x>z:
    print(x,"is greatest")
elif y>z and y>x:
    print(y,"is greatest")
else:
    print(z,"is greatest")
