class LRUCache:
    class _Node:
        def __init__(self, key: int = 0, value: int = 0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.head = self._Node()
        self.tail = self._Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        node = self.nodes.get(key)
        if node is None:
            return -1
        self._remove(node)
        self._add_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.nodes.get(key)
        if node is not None:
            node.value = value
            self._remove(node)
            self._add_front(node)
            return

        if len(self.nodes) == self.capacity:
            oldest = self.tail.prev
            self._remove(oldest)
            del self.nodes[oldest.key]

        node = self._Node(key, value)
        self.nodes[key] = node
        self._add_front(node)
