# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the
# cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Example 1:
#
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4

class ListNode:
    def __init__(self, key, value):
        self.key =  key
        self.value = value
        self.next = None
        self.prev = None


class lru_cache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_map = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        curr_end = self.tail.prev
        curr_end.next = node
        node.prev = curr_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        if key not in self.key_map:
            return -1
        node = self.key_map[key]
        self.remove(node)
        self.add(node)
        return node.value

    def put(self, key, value):
        if key in self.key_map:
            old_node = self.key_map[key]
            self.remove(old_node)
        new_node = ListNode(key, value)
        self.add(new_node)
        self.key_map[key] = new_node

        if len(self.key_map) > self.capacity:
            node_at_front = self.head.next
            self.remove(node_at_front)
            del self.key_map[node_at_front.key]


if __name__ == "__main__":
    print(lru_cache())
