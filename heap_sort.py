from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    ''' 힙 정렬 '''
    
    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        
        temp = a[left]  # 왼쪽이라고 되어 있지만 사실상 부모 노드의 값을 임시 저장한다.

        parent = left   # 입력된 배열의 왼쪽을 부모노드가 되는 것으로 간주한다.
        while parent < (right + 1) // 2:    # 만일 부모의 인덱스가 전체 배열의 크기의 반을 초과하면 중단한다.
            cl = parent * 2 + 1             # 부모 노드의 왼쪽 노드를 가리키는 배열 내의 인덱스
            cr = cl + 1                     # 부모 노드의 오른쪽 노드를 가리키는 배열 내의 인덱스
            
            # 오른쪽 노드의 인덱스가 배열의 오른쪽 인덱스 값보다 크거나 작고, 
            # 오른쪽 노드의 값이 왼쪽 노드의 값보다 크면 오른쪽 노드의 인덱스를 부모와 비교할 자식 인덱스로 잡고
            # 반대면 왼쪽 노드의 인덱스를 부모노드와 비교할 자식노드의 인덱스로 지정한다.  
            child = cr if cr <= right and a[cr] > a[cl] else cl

            # 부모노드의 값이 자식노드의 값보다 크면 pass하고
            # 아니면, 부모노의 자리에 자식노드의 값을 넣고
            # 향후 비교를 위해 자식노드 인덱스를 부모노드 인덱스로 지정해 놓는다.
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        # 비교가 다 끝나면 애초의 부모노드 값을 변화된 (변경된) 부모노드 인덱스에 배열 위치에 넣어준다. 
        a[parent] = temp
    
    n = len(a)

    ''' 힙 정렬을 실행한다.'''
    for i in range((n - 1) // 2, -1, -1):
        down_heap(a, i, n - 1)

    '''힙 정렬 끝낸 것을 보여주기 위해 배열기준 오름차순 정렬한다.'''
    '''힙의 제일 큰 수치를 제일 마지막으로 보낸 후 그것을 제외하고 힙을 다시 정렬한다. 허나마나 한 짓?'''
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i-1)

if __name__ == '__main__':
    print('힙 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요...: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    heap_sort(x)

    print('오름차순으로 정렬했습니다.')

    for i in range(num):
        print(f'x[{i}] = {x[i]}')
        