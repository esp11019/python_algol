
from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        '''초기화'''
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:
    '''체인법으로 해시 클래스를 구현'''
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key:Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        '''sha256 알고리즘 : hashlib에서 제공하는 RSA의 FIPS 알고리즘을 바탕으로 하며 
           주어진 바이트 문자열의 해시값을 구하는 해시 알고리즘의 생성자임'''
        '''encode() 함수 : hashlib.sha256에는 바이트 문자열 인수를 전달해야 하므로
           key를 str 형 문자열로 변환한 뒤 그 문자열을 encode() 함수에 전달하여 바이트 문자열을 생성함'''
        '''hexdigest() 함수 : sha256 알고리즘에서 해시값을 16진수 '문자열'로 꺼낸다.'''
        '''int() 함수 : hexdigest() 함수로 꺼낸 문자열을 16진수 문자열로 하는 int형으로 변환한다.'''
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16)% self.capacity)
    
    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key ==  key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False

    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end = ' ')
            while p is not None:
                print(' ->{0} ({1})'.format(p.key, p.value), end = ' ')
                p = p.next
            print()

