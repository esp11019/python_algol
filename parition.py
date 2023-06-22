from typing import MutableSequence

def partition(a: MutableSequence) -> None:
    '''배열을 나누어 출력'''
    n = len(a)
    pl = 0      # 왼쪽 커서
    pr = n - 1  # 오른쪽 커서

    x = a[n//2] # 피벗 원소(가운데 원소)

    while pl <= pr:
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    
    print(f'피벗은 {x} 입니다.')

    print('v피벗 이하인 그룹입니다.')
    print(*a[0 : pl])         # a[0] ~ a[pl-1]

    if pl > pr + 1:
        print('피벗과 일치하는 그룹입니다.')
        print(*a[pr + 1 : pl])  # a[pr+1] ~ a[pl-1]
    
    print('피벗 이상인 그룹입니다.')
    print(*a[pr + 1 : n])      # a[pr+1] ~ a[n-1]


if __name__ == '__main__':
    print('이진 삽인 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input('x[{}]: '.format(i)))

    partition(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print('x[{}] = {}'.format(i, x[i]))

