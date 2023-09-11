#문제2
#자연수가 들어있는 리스트에 3의 배수와 5의 배수 중 어떤 수가 더 많은지 알아보려 합니다. 이를 위해 다음과 같이 프로그램 구조를 작성했습니다.

def solution(a):
    counter_3 = 0
    counter_5 = 0
    for i in range(len(a)):
        if (a[i]%3 == 0):
            counter_3 +=1
        if (a[i]%5 == 0):
            counter_5 +=1 
    if (counter_3 < counter_5):
        print("5의 배수가 훨신 더 많음")    
    elif (counter_5 < counter_3):
        print("3의 배수가 훨신 더 많음") 
    else:
        print("갯수가 같음")

a = [15,2, 3, 6, 9, 12, 15, 10, 20, 22, 25]
solution(a)