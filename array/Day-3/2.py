arr=[1,5,8,4,5,6,7,1,3]
i=len(arr)-1
while i>0:
    if arr[i]>arr[i-1]:
        arr[-1],arr[i-1]=arr[i-1],arr[-1]
        break
    i-=1
print(arr)



def nextPerm(arr:list):
    for i in range(len(arr)):
        if arr[i]> arr[i-1]:
            pass