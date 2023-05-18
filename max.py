from typing import Any, Sequence
# Any : 제약이 없는 임의의 자료형을 의미
# Sequence : 시퀀스형을 의미, 시퀀스형에는 list형, bytearray형, str형, tuple형, bytes형이 있음



def max_of(a: Sequence)->Any:
    # a: Sequence : 건네받는 매개변수 a의 자료형은 Sequence입니다.
    # -> Any : 반환하는 것은 임의의 자료형인 Any입니다.
    '''
        - 호출하는 쪽이 넘겨주는 실제 인수의 자료형은 뮤터블인 리스트, 이뮤터블인 튜플, 문자열 등 시퀀스형이라면 무엇이든 가능
        - 인수의 원소를 비교 연산자 > 로 값을 비교할 수 있다면 다른 형(int, float)이 섞여 있어도 괜춘
        - 최대값의 원소가 int형 원소이면 int형 값을 반환하고, float형 원소이면 float형 값을 반환한다.
    '''
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    '''
        - 스크립트 프로그램이 직접 실행될 때 변수 __name__은 '__main__'입니다.
        - 스크립트 프로그램이 임포트될 때 변수 __name__은 원래의 모듈 이름입니다.
    '''
    print('배열의 최대값을 구합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input('x[{0}] 값을 입력하세요.: '.format(i)))
    
    print('최대값은 {0} 입니다.'.format(max_of(x)))