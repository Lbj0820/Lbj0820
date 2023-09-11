def solution(s):
    r=0
    for i in range(len(s)):
        if (s[i]> 650 and s[i]< 800):
            r+=1
    return r
score = [100,200,300,400,500,600,700,800,900,1000]
print(solution(score)) 