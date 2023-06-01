from enum import Enum
from fixed_stack import FixedStack

#Menu = Enum('Menu',['Push', 'Pop', 'Peek', 'Find', 'Dump', 'Exit'])
Menu = Enum('Menu', 'Push Pop Peek Find Dump Exit')

def select_menu() -> Menu:
    s = ['({0}) {1}'.format(m.value, m.name) for m in Menu]
    while True:
        print(*s, sep = '  ', end ='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
        
s = FixedStack(64)

while True:
    print('현재 데이터 개수: {0} / {1}'.format(len(s),s.capacity))
    menu = select_menu()
    print('선택된 메뉴는 : {} 입니다.'.format(menu.name))
    
    if menu == Menu.Push:
        x = int(input('데이터를 입력하세요.: '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('스택이 가득 차 있습니다.')
    elif menu == Menu.Pop:
        try:
            x = s.pop()
            print(f'팝한 데이터는 {x} 입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')
    elif menu == Menu.Peek:
        try:
            x = s.peek()
            print(f'피크 데이터는 {x} 입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')
    elif menu == Menu.Find:
        x = int(input('검색할 데이터를 입력하세요.: '))
        if x in s:
            print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
        else:
            print('검색값을 찾을 수 없습니다.')
    elif menu == Menu.Dump:
        s.dump()
    else:
        break
