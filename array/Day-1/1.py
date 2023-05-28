import sys
sys.stdin=open('input.txt','r')

""""
Q1. Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.


Algorithm:

1. Initiate min and max by 1st elem of array
2. traverse through array comparing next elements with current value of max and min
3. Return min and max


TC : O(n)
SC: O(n)
"""

def maxandmin(arr:list[int])->int:
    max=arr[0]
    min=arr[0]

    for i in arr:
        if min > i:
            min=i
        if max<i:
            max=i
    return (max,min)
if __name__=="__main__":
    max,min=maxandmin([-1,8,3,2,-5])
    print(f"max = {max} \nmin = {min}")


