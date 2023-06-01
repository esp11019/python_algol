from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', '인큐 디큐 피크 검색 덤프 종료')

def selected_menu() -> Menu:
    s = ['({0}) {1}'.format(m.value, m.name) for m in Menu]
    
    while True:
        print(*s, sep = ' ', end = '')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
        
q = FixedQueue(64)

while True:
    print('현재의 데이터 개수 : {} / {}'.format(len(q), q.capacity))
    menu = selected_menu()

    if menu == Menu.인큐:
        x = int(input('인큐할 정수 데이터를 입력하세요.: '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('큐가 가득 찼습니다.')
    elif menu == Menu.디큐:
        try:
            x = q.deque()
            print('디큐한 데이터는 {} 입니다.'.format(x))
        except FixedQueue.Empty:
            print('큐가 비어 있습니다.')
    elif menu == Menu.피크:
        try:
            x = q.peek()
            print('피크한 데이터는 {} 입니다.'.format(x))
        except FixedQueue.Empty:
            print('큐가 비어 있습니다.')
    elif menu == Menu.검색:
        x = int(input('찾을 정수값을 입력하세요.: '))
        if x in q:
            print('{} 개 포함되고, 맨 앞의 위치는 {} 입니다.'.format(q.count(x), q.find(x)))
        else:
            print('찾는 정수값이 없습니다.')
    elif menu == Menu.덤프:
        q.dump()
    else:
        break

