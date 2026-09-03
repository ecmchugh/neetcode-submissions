class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.count = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.count:
            n = self.count[key]
            res = n.value
            self.remove(n)
            self.addToTail(n)
            return res
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.count: 
            n = self.count[key]
            n.value = value
            self.remove(n)
            self.addToTail(n)
        else:
            self.count[key] = Node(key, value)
            self.addToTail(self.count[key])
            if len(self.count) > self.capacity:
                rem = self.head.next.key
                self.count.pop(rem)
                self.remove(self.head.next)

    def addToTail(self, temp):
        store = self.tail.prev
        self.tail.prev = temp
        temp.next = self.tail
        store.next = temp
        temp.prev = store

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
            
        
        
