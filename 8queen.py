pos = [0] * 8
flag_a = [False] * 8
flag_b = [False] * 15
flag_c = [False] * 15
#print(pos)

def put() -> None:
    '''각 열에 배한 퀸의 위치를 출력'''
    for j in range(8):
        #print('{:2}'.format(pos[i]), end = ' ')
        for i in range(8):
            print('◼︎' if pos[i] == j else '◻︎', end=' ')
        print()
    print()

def set(i: int) -> None:
    '''i 열에 퀸을 배치'''
    for j in range(8):
        if (    not flag_a[j]   # j행에 퀸을 배치 않았다면
            and not flag_b[i + j]
            and not flag_c[i - j + 7]):
            pos[i] = j
            if i == 7:
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False

set(0)