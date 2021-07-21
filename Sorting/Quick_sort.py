def partition(arr,start,end):
    partion_index=start
    pivot=arr[start]
    while start<end:
        while start<end and arr[start]<=pivot:
            start+=1
        while arr[end]>pivot:
            end-=1
        if start<end:
            arr[start],arr[end]=arr[end],arr[start]
    arr[end],arr[partion_index]=arr[partion_index],arr[end] 
    return end
def quick_sort(arr,start,end):
    if start<end:
        p=partition(arr,start,end)
        quick_sort(arr,start,p-1)
        quick_sort(arr,p+1,end)               
arr=[20,10,34,22,4,2]
start=0
end=len(arr)-1
quick_sort(arr,start,end)
print(arr)