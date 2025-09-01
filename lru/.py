class Node:
    """Represents a node in the doubly linked list."""
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    """
    An LRU Cache implementation using a dictionary and a doubly linked list.
    The dictionary provides O(1) lookups, and the doubly linked list allows
    for O(1) removal and addition of nodes.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        # The dictionary stores key-to-node mappings for quick access.
        self.cache = {}
        # We use sentinel head and tail nodes to simplify edge cases
        # (e.g., adding to an empty list or removing the last element).
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node):
        """Removes a node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.cache[node.key]

    def _add_to_head(self, node):
        """Adds a node to the front of the linked list."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.cache[node.key] = node

    def get(self, key):
        """
        Retrieves a value from the cache. If the key exists, the node is
        moved to the front to mark it as most recently used.
        """
        if key in self.cache:
            node = self.cache[key]
            # Remove the node from its current position.
            self._remove_node(node)
            # Add it back to the head to mark it as most recently used.
            self._add_to_head(node)
            return node.val
        return -1

    def put(self, key, value):
        """
        Inserts or updates a key-value pair in the cache.
        If the cache is at capacity, the least recently used item is removed.
        """
        if key in self.cache:
            # If the key already exists, update its value and move to the front.
            node = self.cache[key]
            self._remove_node(node)
            new_node = Node(key, value)
            self._add_to_head(new_node)
        else:
            # Check if the cache is full.
            if len(self.cache) >= self.capacity:
                # Remove the least recently used node from the tail.
                lru_node = self.tail.prev
                self._remove_node(lru_node)

            # Add the new key-value pair to the cache.
            new_node = Node(key, value)
            self._add_to_head(new_node)
            
# Example usage to demonstrate a working cache:
obj = LRUCache(2)
print("Putting (1, 1)...")
obj.put(1, 1)

print("Putting (2, 2)...")
obj.put(2, 2)

print("Getting key 1 (should return 1)...")
# Accessing key 1 makes it the most recently used.
print("Result:", obj.get(1))

print("Putting (3, 3)...")
# Cache is full, and key 2 is now the least recently used, so it should be evicted.
obj.put(3, 3)

print("Getting key 2 (should return -1)...")
print("Result:", obj.get(2))

print("Getting key 3 (should return 3)...")
print("Result:", obj.get(3))
