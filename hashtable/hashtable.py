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
            #hash &= 0xFFFFFFFF
        return hash + 0xFFFFFFFF

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
        #hash key for indexing
        index = self.hash_index(key)

        #make key, value a node
        node = HashTableEntry(key, value)

        if self.storage[index] is None:
            #if nothing in index add node
            self.storage[index] = node
            #update size attribute for resize comparison resize
            self.size += 1
            #run resize function to check if table needs resizing
            self.resize()
        elif self.storage[index].next:
            #if a value exists at index, go through sll and add at end
            cur = self.storage[index]
            while cur is not None:
                cur = cur.next
                #after adding, check if resize is necessary
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
        #find hash for key
        index = self.hash_index(key)

        cur = self.storage[index]

        while cur is not None:
            if key == cur.key:
                #found the value, so return it
                return cur.value
            cur = cur.next
        return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        #if hashtable is over 70% capacity, double it
        if (self.size / self.capacity ) > 0.7:
            #create a temp hash at double the size
            self.capacity *= 2
            #create a temporary hashtable for copying
            t = [None] * self.capacity
        #if hashtable is under 20% capacity, halve it
        elif (self.size / self.capacity) < 0.2:
            self.capacity /= 2
            #create temporary hashtable for copying
            t = [None] * self.capacity
        else:
            return None

        for x in range(len(self.storage)):
            cur = self.storage[x]

            if cur is not None:

                y = cur.next
                while y is not None:
                    index = self.hash_index(self.storage[x].key)
                    node = HashTableEntry(y.key, y.value)
                    t[index] = node
                    if y.next:
                        t[index].next = y.next
                    y = y.next
                if y is None:
                    index = self.hash_index(cur.key)
                    node = HashTableEntry(cur.key, cur.value)
                    t[index] = node

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
