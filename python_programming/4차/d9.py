def solution(socks):
    b = socks.copy()    #socks를 복사하여 b의 저장
    b = list(set(b))    #b를 중복제거하고 리스트로 변환
    b.sort()    #b를 오름차순 정렬
    sum = 0
    for i in b:
        if socks.count(i)< 2:   #socks배열에서 i의 갯수가 2개 미만이면 넘어감
            continue
        else:
            sum+= int(socks.count(i)/2)     #2개 이상이면 sum값에 socks.count(i)의 값을 한 쌍이기 때문에 2로 나눈 값을 더해줌 
    print(sum)


socks=[1, 2, 1, 3, 2, 1]
solution(socks)