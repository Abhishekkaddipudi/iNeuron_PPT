"""
return element which is repeated more n/2 
"""

Freq=dict()
arr=[1,2,3,4,3,3,3,3,3]
n=len(arr)

for i in arr:
    if i in Freq:
        Freq[i]+=1
        if Freq[i]>(n/2):
            ans=i
            break
    else:
        Freq[i]=1

print(ans)
