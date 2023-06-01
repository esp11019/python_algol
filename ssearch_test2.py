from ssearch_while import seq_search

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print('{}에서 5.6의 인덱스는 {} 입니다.'.format(t, seq_search(t, 5.6)))
print('{}에서 "n"의 인덱스는 {} 입니다.'.format(s, seq_search(s, 'n')))
print('{}에서 5.6의 인덱스는 {} 입니다.'.format(a, seq_search(a, 'DTS')))