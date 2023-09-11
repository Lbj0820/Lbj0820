def solution(a,b):
    r=[]
    for i in range(b-1, -1, -1):
        r.append(a[i])
    print(r)

v = int(input("배열을 크기를 입력하세요: "))
x=[]
for i in range(v):
    b = int(input("추가할 배열 요소를 입력하세요"))
    x.append(b)

solution(x,v)