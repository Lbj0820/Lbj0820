def solution(a):
    a1 = []
    sum = 0
    for i in range(3):
        for j in range(a[i][0], a[i][-1]):
            a1.append(j)
    b = a1.copy()
    b = set(b)
    b = list(b)
    for i in b:
        if a1.count(i) >= 2:
            sum += 1
    print(sum)


a = [[1, 3], [3, 5], [3, 7]]
solution(a)
