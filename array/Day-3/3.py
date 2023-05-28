arr=[11,15,6,8,9,10]
s=16
min=float("inf")
max=0
left,right=0,0
for i in range(len(arr)):
    if min>arr[i]:
        min=arr[i]
        left=i
    if max<arr[i]:
        max=arr[i]
        right=i
print(min,max)
while left>right:
    if arr[left]+arr[right]==s:
        print(arr[left],arr[right])
        break
    left=(left+1)%(len(arr)-1)
    right=(right-1*(len(arr)-1))%(len(arr)-1)
