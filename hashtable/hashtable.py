class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable():
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = 8):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.head = None
        self.size = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
            hash &= 0xFFFFFFFF
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        node = HashTableEntry(key, value)
        print("[put] index:", index)
        print("[put] capacity", self.capacity, "length", len(self.storage))
        if self.storage[index] is None:
            self.storage[index] = node
            self.size += 1
            self.resize()
        elif self.storage[index].next:
            print('collision')
            cur = self.storage[index]
            while cur is not None:
                cur = cur.next
                self.resize()
            cur = node
            self.size += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        cur = self.storage[index]
        if cur is None:
            return
        else:
            if cur.key ==  key:
                cur = cur.next
                self.size -= 1
                self.resize()
            else:
                while cur is not None:
                    if cur.key == key:
                        cur = cur.next
                        prev.next = cur
                        self.size -= 1
                        self.resize()
                        return
                    prev = cur
                    cur = cur.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        cur = self.storage[index]
        while cur is not None:
            if key == cur.key:
                return cur.value
            cur = cur.next
        return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        print("[size] self.size", self.size)
        if (len(self.storage) / self.size) > 0.7:
            #create a temp hash at double the size
            print("[resize] self.capacity", self.capacity)
            self.capacity *= 2
            print("[resize] self.capacity", self.capacity)
            t = [None] * self.capacity
            print('length of t', len(t))
        elif (len(self.storage) / self.size) < 0.2:
            self.capacity /= 2
            print("[resize] self.size", self.size)
            # if self.capacity < 8:
            #     self.capacity = 8
            t = [None] * self.capacity
        else:
            return None

        for x in range(len(self.storage)):
            cur = self.storage[x]
        
            if cur is not None:
                y = cur.next
                while y is not None:
                    index = self.hash_index(self.storage[x].key)
                    t[index].key, t[index].value, t[index].next = y.key, y.value, y.next
                    y = y.next
        self.storage = t

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
