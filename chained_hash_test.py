from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['append','remove','search','dump','exit'])

def select_menu() -> Menu:
    s = ['({0}) {1}'.format(m.value, m.name) for m in Menu]

    while True:
        print(*s, sep = '  ', end = '')
        n = int(input(':  '))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = ChainedHash(13)

while True:
    menu = select_menu()

    if menu == Menu.append:
        key = int(input('추가할 키를 입력하세요.: '))
        val = input('추가할 값을 입력하세요.: ')
        if not hash.add(key, val):
            print('추가에 실패했습니다.')
    elif menu == Menu.remove:
        key = int(input('삭제를 키를 입력하세요.: '))
        if not hash.remove(key):
            print('삭제에 실패했습니다.')
    elif menu == Menu.search:
        key = int(input('검색할 키를 입력하세요.: '))
        t = hash.search(key)
        if t is not None:
            print('검색한 키를 갖는 값은 {} 입니다.'.format(t))
        else:
            print('검색할 데이터가 없습니다.')
    elif menu == Menu.dump:
        hash.dump()
    else:
        break;