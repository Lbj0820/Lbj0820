def solution(weight, boxes):
    sum=0
    for i in boxes:     
        if i < weight*0.9 or i > weight*1.1:    #오차범위 10퍼센트까지가 정상으로 취급하므로 그 범위안에 해당 무계가 들어맞을 경우 sum값에 1을 더함 
            sum+=1 
    print(sum)


weight = 600
boxes = [653, 670, 533, 540, 660]
solution(weight, boxes)