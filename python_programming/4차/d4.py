def solution(cards):
    if cards[0][0] == cards[1][0] and cards[0][0] == cards[2][0] and cards[1][0] == cards[2][0]:    #3개의 카드 색이 모두 동일한 경우일 때 카드에 적힌 숫자를 모두 더하고 곱하기 3을 해주어 sum에 저장 
        sum = (cards[0][1] + cards[1][1] + cards[2][1])*3
    elif cards[0][0] == cards[1][0] or cards[0][0] == cards[2][0] or cards[1][0] == cards[2][0]:    #2개의 카드 색만 동일한 경우일 때 카드에 적힌 숫자를 모두 더하고 곱하기 2을 해주어 sum에 저장 
        sum = (cards[0][1] + cards[1][1] + cards[2][1])*2
    else:   #나머지 경우엔 카드값을 더하여 sum에 저장
        sum = cards[0][1] + cards[1][1] + cards[2][1]   
    print(sum)
    


cards = [["blue", 2], ["blue", 5], ["black", 3]] 
solution(cards)