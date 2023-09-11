def solution(a):
    result = ""
    b = 0
    while a > 0:
        if a == 1 or a == 2:
            b = -1
            print(b)
            break
        a -= 3
        result += "RRR"
        if a == 1:
            b = -1
            print(b)
            break
        a -= 2
        result += "GG"
        if a == 0:
            break
        a -= 1
        result += "B"
    if b != -1:
        print(result)


a = 14
solution(a)
