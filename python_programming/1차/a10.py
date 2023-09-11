def solution(a):
    r=0
    for i in range(len(a)):
        r += a[i]
    for i in range(len(a)):    
        if (a[i] < r/len(a)):
            print(a[i], end=" ") 

a = [1,2,3,4,5,6,7,8,9,10]
solution(a)