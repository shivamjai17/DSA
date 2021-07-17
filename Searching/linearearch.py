#Linear Search Programe
arr=[10,20,80,30,60,50,110,100]
print('Enter number to be search')
x=int(input())
flag=False
index=0
for i in range(len(arr)):
    if x== arr[i]:
        flag=True
        index=i
        break
    else:
        flag=False
if flag==True:
    print('Number present at index',index)
else:
    print('Number Not Present')            
