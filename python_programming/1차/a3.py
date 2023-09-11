def solution(start_month, start_day, end_month, end_day):
    d = [0]*12
    s_sum = start_day
    e_sum = end_day
                                   
    for i in range(12):
        if (i ==2):
            d[i] = 28
        elif (i == 8 ):
            d[i] = 31
        elif (i%2 == 0):
            d[i] = 30
        elif (i%2 == 1):
            d[i] = 31
    gap_sum = d[start_month]-start_day+end_day
    for i in range(start_month-1):
        s_sum +=d[i]
        s_sum-=1 
    for i in range(end_month-1):
        e_sum +=d[i]
    for i in range(start_month, end_month-1):
        gap_sum+=d[i] 
    print(start_month,"월", start_day,"일은 1월 1일로부터", s_sum ,"일만큼 지난 날입니다")
    print(end_month,"월", end_day,"일은 1월 1일로부터", e_sum ,"일만큼 지난 날입니다")
    print(start_month,"월", start_day,"일과",end_month,"월",end_day,"일은",gap_sum ,"일만큼 떨어져 있습니다.")

start_month = int(input("시작 달을 입력해주세요"))
start_day = int(input("시작 일을 입력해주세요"))
end_month= int(input("끝 달을 입력해주세요"))
end_day= int(input("끝 일을 입력해주세요"))

solution(start_month, start_day, end_month, end_day)
