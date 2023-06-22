from typing import MutableSequence

def binary_insertion_sort(a:MutableSequence) -> None:
    '''이진 단순 삽입 정렬'''
    n = len(a)

    for i in range(1, n):
        key = a[i]
        pl = 0
        pr = i - 1
        print('pl={}, pr={}, i={}, key={}'.format(pl, pr, i, key))
        for k in range(num):
            print('x[{}] = {}'.format(k, x[k]))
        input()
        while True:
            pc = (pl + pr) // 2
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break
        
        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key

if __name__ == '__main__':
    print('이진 삽인 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input('x[{}]: '.format(i)))

    binary_insertion_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print('x[{}] = {}'.format(i, x[i]))