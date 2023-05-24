from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    '''뮤터블 시퀀스 a의 원소를 역순으로 정렬'''
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

if __name__ == '__main__':
    print('배열 워노를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요.: '))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input('x[{}] 값을 입력하세요.: '))

    reverse_array(x)

    print('배열 원소를 역순으로 정렬했습니다.')

    for i in range(nx):
        print('x[{}] = {}'.format(i, x[i]))
    print()

    x = [1,2,3,4,5]
    x = list(reversed(x))
    for i in range(len(x)):
        print('x[{}] = {}'.format(i, x[i]))
    print()