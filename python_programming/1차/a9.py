def solution(s):
    l=[s[0]]
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            l.append(s[i])
    print(l)

s = 'seer'
solution(s)
