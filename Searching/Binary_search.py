def binarysearch(arr,l,r,x):
    while l<=r:
        mid=l+(r-1)//2
        if x==arr[mid]:
            return mid
        elif x>arr[mid]:
            l=mid+1
        else:
            r=mid-1
    return -1                
arr=[10,20,40,60,70,90]
print("Enter Number to be saerch")
x=int(input())
result=binarysearch(arr,0,len(arr)-1,x)
if result != -1:
    print('Number is present at',result)
else:
    print('Number is Not present')    