# 문제4
# 단어들이 들어있는 리스트에서 길이가 5 이상인 단어를 리스트에 들어있는 순서대로 이어 붙이려 합니다.

# 예를 들어 리스트가 다음과 같은 경우

# ["my", "favorite", "color", "is", "violet"]

# "favoritecolorviolet"을 만들면 됩니다.

# 단어들이 들어있는 리스트 words가 solution 함수의 매개변수로 주어질 때, 길이가 5 이상인 단어를 순서대로 이어 붙인 문자열을 return 하도록 solution 함수를 완성해주세요.

# ---
# #####매개변수 설명
# 단어들이 들어있는 리스트 words가 solution 함수의 매개변수로 주어집니다.

# * words의 길이는 1 이상 100 이하입니다.
# * words에 들어있는 각 단어의 길이는 1 이상 10 이하이며, 알파벳 소문자로만 이루어져 있습니다.

# ---
# #####return 값 설명
# 길이가 5 이상인 단어를 순서대로 이어 붙여 return 해주세요.
# * 만약 return 할 문자열이 빈 문자열이면 "empty"를 return 해주세요.


def solution(a):
    b = ""
    for i in range(len(a)):
        if len(a[i]) >= 5:
            b += a[i]
    if b == "":
        b = "empty"
    print(b)


a = ["my", "favorite", "color", "is", "violet"]
solution(a)
