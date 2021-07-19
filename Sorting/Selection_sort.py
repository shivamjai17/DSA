#Programe for slection sort
arr=[3,2,4,5,1,]
n = len(arr)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if (arr[j]<arr[min_index]):
            min_index=j
    arr[min_index],arr[i]=arr[i],arr[min_index]
print(arr)            