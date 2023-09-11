def solution(money, price, n):
    sum=0
            
    while True:     
        if price> money:    #물건 가격이 내가 보유한 돈이 클 때 sum값을 출력하고 반복문 탈출
            print(sum)  
            break
        if money>0:     #보유 돈이 0보다 클 때 돈에서 물건가격을 빼고 sum값에 1을 더해감
            money-=price
            sum+=1
        if sum%n ==0:   #sum값을 n의 크기로 나누어 떨어질때 sum값에 1을 더함
            sum+=1

money = 13
price = 2
n = 2
solution(money, price, n)
