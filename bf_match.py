def bf_match(txt: str, pat: str) -> int:
    '''브루트 포스법으로 문열 검색'''
    pt = 0  # txt를 따라가는 커서
    
    pp = 0  # pat를 따라가는 커서

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else :
            pt = pt - pp + 1
            pp = 0
    
    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')
    s2 = input('패턴을 입력하세요.: ')

    idx = bf_match(s1, s2)

    if idx == -1:
        print('Not exist pattern in text')
    else:
        print(f'The {(idx+1)}th character in text matches')
