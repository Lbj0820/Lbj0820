def solution():
    str = ''
    a = 'nav  an'
    for c in a:
        if (c != ' ' and c !='.'):
            str +=c
    print(str)
    if str == 'navan':
        print(1)
    else:
        print(0)
solution()
