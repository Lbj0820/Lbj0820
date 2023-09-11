def solution(ll, rl):
    lc = [0 for _ in range(11)]
    rc = [0 for _ in range(11)]
    for i in range(1,11):
        lc[i] = ll.count(i)
        rc[i] = rl.count(i)
    solution2(lc,rc)

def solution2(lc,rc):
    sum = 0
    for i in range(1,11):
        #sum +=min(lc[i],rc[i])
        if (lc[i] < rc[i]):
            sum+=lc[i]
        else:
            sum+=rc[i]
    print(sum)
   
left_gloves_lenght = [10,5,3,4,5,1,2] 
right_gloves_length = [10,2,5,3,7,5,6] 
solution(left_gloves_lenght,right_gloves_length)