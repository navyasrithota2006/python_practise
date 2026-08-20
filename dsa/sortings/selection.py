'''selection sort :  select the minimum in an array and swap
tc - O(n^2) - not because of two for loops 
the i is ranging from 0 to n-1 -- > n 
the j is ranging from i to n-1 ---> 1--n-1,2--n-1....n-1
n+1+2+...+n-1===sum of n numbers
soo o(n^2)
'''

n= int(input())
l = list(map(int,input().split()))
for i in range(n-1):
    mini = i
    for j in range(i,n):
        if l[j] < l[mini]:
            mini = j
    l[mini],l[i] = l[i],l[mini]
print(*l)
