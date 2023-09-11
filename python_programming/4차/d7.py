def solutuion(money, chairs, desks):
    sum=0
    min= money - (chairs[0]+desks[0])       #min값에 보유 돈에서 chairs[0]+desks[0]의 값을 빼서 저장
    for i in chairs:
        for j in desks:
            if money-(i+j) >= 0 and min > money-(i+j):      
                #i+j를 더한값이 money에서 뺏을 때 그 값이 최소가 되는 값을 sum에 저장
                min = money-(i+j)
                sum = i+j
    print(sum)

money=7
chairs = [3]
desks = [5]

solutuion(money, chairs, desks)