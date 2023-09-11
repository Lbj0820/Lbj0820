def solution(temperature, a, b):
    sum = 0
    for i in range(a,b):
        if temperature[i] > temperature[a] and temperature[i] > temperature[b]:     #a와 b보다 큰 수가 나왔을 때 sum값에 1을 더함
            sum+=1
    print(sum)




temperature = [3, 2, 1, 5, 4, 3, 3, 2]
a = int(input("a를 입력하세요: "))
b = int(input("b를 입력하세요: "))
solution(temperature, a, b)
