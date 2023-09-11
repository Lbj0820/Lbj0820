def solution(g, p):
    if g == 's':
        print(p,"원의 5%는",p*0.05,"원 입니다.",p-p*0.05,"=",p-p*0.05)
    elif g == 'g':
        print(p,"원의 10%는",p*0.1,"원 입니다.",p-p*0.1,"=",p-p*0.1)
    elif g == 'v':
        print(p,"원의 15%는",p*0.15,"원 입니다.",p-p*0.15,"=",p-p*0.15)
    else:
        print("해당 등급은 없는 등급입니다.")   

grade = input("등급이 s, g, v중에 어떤 등급입니까?")
price=int(input("가격이 얼마입니까?"))

solution(grade, price)