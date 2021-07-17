def binarysearch(arr,l,r,x):
    if r>=l:
        mid=l+(r-1)//2
        if arr[mid]==x:
            return mid
        elif x<arr[mid]:
            return binarysearch(arr,l,mid-1,x)
        else:
            return binarysearch(arr,mid+1,r,x)
    else:
        return -1                

arr=[10,20,40,60,70,90]
print("Enter Number to be saerch")
x=int(input())
result=binarysearch(arr,0,len(arr)-1,x)
if result != -1:
    print('Number is present at',result)
else:
    print('Number is Not present') 