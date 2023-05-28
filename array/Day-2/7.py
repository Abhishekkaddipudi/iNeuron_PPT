"""
merge to make palindrome
"""

arr=[1,4,5,1]
if arr==arr[::-1]:
    print(True)
i=0
j=len(arr)
while i <=j:
    if arr[i]==arr[j]:
        i+=1
        j+=1
    elif arr[i]<arr[j]:
        arr[i]=arr[i]+arr[i+1]
        
        
