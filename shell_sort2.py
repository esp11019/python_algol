from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    '''셀 정렬'''
    n = len(a)

    h = 1

    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >=0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
        h //= 3

if __name__ == '__main__':
    print('셀 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input('x[{}]: '.format(i)))

    shell_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print('x[{}] = {}'.format(i, x[i]))