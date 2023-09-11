import math

def solution(n):
    a = str(n)  #n을 문자형으로 변환해서 a에 저장
    a = list(a) #a를 리스트형으로 변환
    a.reverse() #a의 요소들을 뒤집음
    b=''    #b변수에 에 빈 문자열을 저장
    for i in a:    
       if i != '0':     #a배열에서 인덱스가 0이 아닐 때 b에 그 인덱스 값을 더함 
            b+=str(i)
    b = int(b)  #b를 정수형으로 변환
    sum=int(math.sqrt((n-b)**2))    #음수가 나올 수 있으므로 처음 n값과 b의 값의 차를 제곱한 후 제곱근을 하여 sum값에 저장
    print(sum)

n= 120
solution(n)