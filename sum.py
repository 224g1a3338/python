n=int(input())
even=0
odd=0
arr=list(map(int,input().split()))
for i in arr:
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
print(even,odd,end=" ")
        
        
