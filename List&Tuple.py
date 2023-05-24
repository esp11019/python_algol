lst1 = [1,2,3,4,5]
lst2 = [1,2,3,4,5]
print(lst1 is lst2)

lst2 = lst1
print(lst1 is lst2)

lst1[2] = 9
print(lst1)
print(lst2)
print()


# 리스트 스캔 실습

### 실습 2C-1 : 원소 수를 len()함수롤 미리 알아내서 0에서 원소 수 -1까지 반복합니다.
x = ['John', 'George', 'Paul', 'Ringo']
for i in range(len(x)):
    print('x[{0}] = {1}'.format(i, x[i]))
print()

### 실습 2C-2 : 인덱스와 원소를 짝지어 enumerate() 함수로 반복해서 꺼냅니다.
for i, name in enumerate(x):
    print('x[{0}] = {1}'.format(i, name))
print()

### 실습 2C-3 : 실습 2C-2와 같지만 1부터 카운트 합니다.
for i, name in enumerate(x, 1):
    print('x[{}] = {}'.format(i, name))
print()

### 실습 2C-4 : 인덱스 값을 사용하지 않고 in을 사용해서 원소를 처음부터 순서대로 꺼냅니다.
for name in x:
    print(name)
print()    