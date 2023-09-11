# 문제6
# 하루 동안 엘리베이터가 멈춘 층이 순서대로 들어있는 리스트가 있습니다. 이때, 엘리베이터의 총 이동거리를 구하려 합니다.
#  단, 층과 층 사이의 거리는 1입니다.

# 예를 들어 리스트에 [1, 2, 5, 4, 2]가 들어있다면, 엘리베이터가 이동한 거리는 7입니다.

# 하루 동안 엘리베이터가 멈춰 선 층이 순서대로 들어있는 리스트 floors가 매개변수로 주어질 때,
# 엘리베이터의 총 이동 거리를 return 하도록 solution 함수를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.

# ---
# #####매개변수 설명
# 하루 동안 엘리베이터가 멈춘 층이 순서대로 들어있는 리스트 floors가 solution 함수의 매개변수로 주어집니다.
# * floors의 길이는 2 이상 100 이하입니다.
# * floors의 원소는 1 이상 100 이하의 자연수이며, 인접한 두 원소의 값이 같은 경우는 주어지지 않습니다.
# * floors의 첫 번째 원소는 엘리베이터의 처음 위치를 나타냅니다.

# ---
# #####return 값 설명
# 엘리베이터의 총 이동 거리를 return 해주세요.

# ---
# #####예시
# | floors          | return |
# |-----------------|--------|
# | [1, 2, 5, 4, 2] | 7      |


def solution(a):
    sum = 0
    for i in range(1,len(a)):
        if a[i] < a[i - 1]:
            sum += a[i - 1] - a[i]
        else:
            sum += a[i] - a[i - 1]
    print(sum)


a = [1, 2, 5, 4, 2]
solution(a)
