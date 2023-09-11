def solution(people):
    size =[0,0,0,0]
    for i in range(len(people)):
        if people[i] <95:   #옷 사이즈가 95미만인 사람 수당 size[0]에 +1을 해줌
            size[0]+=1
        elif people[i] >=95 and people[i] <100:     #옷 사이즈가 95이상 100 미만인 사람 수당 size[1]에 +1을 해줌
            size[1]+=1
        elif people[i] >=100 and people[i] <105:    #옷 사이즈가 100이상 105 미만인 사람 수당 size[2]에 +1을 해줌
            size[2]+=1
        else:
            size[3]+=1      #나머지 사람들은 size[3]에 +1을 해줌
    print(size)


people = [97, 102, 93, 100, 107]
solution(people)

