def solution(num_apple, num_carrot, k):
    if (num_apple - k) // 3 > num_carrot:
        num_apple -= k
    else:
        num_carrot -= k
    num_apple = num_apple // 3
    if num_apple < num_carrot:
        k = num_apple
    else:
        k = num_carrot
    return k


num_apple = 9
num_carrot = 8
k = 4
print(solution(num_apple, num_carrot, k))
