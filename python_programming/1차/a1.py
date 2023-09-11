def solution(x):
    b = [0,0,0,0,0,0]
    for i in range(len(x)):
        if (x[i] == "XS"):
            b[0]+=1
        elif (x[i] == "S"):
            b[1]+=1
        elif (x[i] == "M"):
            b[2]+=1
        elif (x[i] == "L"):
            b[3]+=1
        elif (x[i] == "XL"):
            b[4]+=1 
        else:
            b[5]+=1 
    return b

shirt_size = ["XS", "S", "L","L", "XL","S"]
ref = solution(shirt_size)

print(ref, end = " ")