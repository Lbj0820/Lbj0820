def solution(a, b):
    sum = 0
    if b == "버스":
        adult_cost = 40000
        kids_cost = 15000
    elif b == "배":
        adult_cost = 30000
        kids_cost = 13000

    elif b == "비행기":
        adult_cost = 70000
        kids_cost = 45000
    if len(a) >= 10:
        adult_cost = adult_cost * 0.9
        kids_cost = kids_cost * 0.8

    for i in range(len(a)):
        if a[i] >= 20:
            sum += adult_cost
        else:
            sum += kids_cost
    print(sum)


member_age = [13, 33, 45, 11, 20]
transportation = "버스"
solution(member_age, transportation)
