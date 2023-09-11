def solution(arr):
    a = arr
    a= set(a)
    a= list(a)
    a.sort()
    print(a)
    b =[0] * len(a) 
    arr.sort() 
    j = 0
    for i in range(1, len(arr)):
        b[j]+= 1
        if (arr[i] != arr[i-1]):
            j+=1
    s = a[b.index(max(b))] // a[b.index(min(b))]
    print(s)        

array = [2,6,6,6,4,4,4,4,4,65,34,4,63,43,5,345,63,43,5,345,5,1,1,1,1,1,1,1,1,1,1,1,1]
solution(array)