#문제3
#서로 다른 두 자연수 N과 M이 매개변수로 주어질 때, N부터 M까지의 자연수 중에서 짝수들의 제곱의 합을 return 하도록 solution 함수를 완성해주세요.

def solution(n,m):
    sum=0
    for i in range(n,m):
        if (i%2==0):
            sum +=i*i
    print(sum)

n=4
m=7
solution(n,m)