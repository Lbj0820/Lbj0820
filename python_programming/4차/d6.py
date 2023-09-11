def solution(password):
    a=b=c=0
    for i in range(len(password)):
        if password[i] >= 'A' and  password[i] <= 'Z':      #비밀번호에 대문자 알파벳이 들어갈 경우 a에 +1을 함
            a+=1
        elif password[i] >= 'a' and  password[i] <= 'z':    #비밀번호에 소문자 알파벳이 들어갈 경우 b에 +1을 함
            b+=1
        elif password[i] >= '1' and  password[i] <= '9':    #비밀번호에 숫자가 들어갈 경우 c에 +1을 함
            c+=1
    if a>=1 and b>=2 and c>=2:      #a가 1 이상 b가 2이상 c가 2이상일 경우 true를 반환
            return True
    else:       #위 경우가 아닐 경우 false반환
         return False

password = "Hello123"
print(solution(password))