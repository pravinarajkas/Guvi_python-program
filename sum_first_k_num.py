N=int(input("Enter the N value:"))
K=int(input("Enter the K value:"))
a=[]
for i in range(1,N+1):
    
    a.append(i)
print(a)
c=0
for j in a:
    if j<=K:
        c=c+j
        j=j+1
        
print(c)

    
