from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    '''단순 삽입 정렬'''
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[j]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

if __name__ == '__main__':
    print('단순 삽입 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input('x[{}]: '.format(i)))

    insertion_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print('x[{}] = {}'.format(i, x[i]))