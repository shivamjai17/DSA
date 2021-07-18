#programe of bubble sort
arr=[5,1,4,2,3]
n=len(arr)
for i in range(n):
    for j in range(i,n-1):
        if(arr[j+1]<arr[j]):
            arr[j+1],arr[j]=arr[j],arr[j+1]
print(arr)            