# 1부터 n까지 정수의 합 구하기

def sum_1ton(n):
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

if __name__ == '__main__':
    x = int(input('x의 값을 입력하세요.: '))
    print('1부터 {}까지의 정수의 합은 {} 입니다.'.format(x, sum_1ton(x)))
    