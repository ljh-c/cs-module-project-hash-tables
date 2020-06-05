class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'HashTableEntry: {repr(self.key)}, {repr(self.value)}'

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity: int = MIN_CAPACITY):
        self.capacity = capacity
        self.storage = [None for i in range(capacity)]
        self.total = 0


    """
    Load Factor:
    number of things stored in hash table / number of buckets in array
    
    Resize hash Table:
    1. Allocate new array of bigger size
    - typically double, or half down to some minimum
    2. Traverse old hash table - O(n) over number of elements in has table
    - For each of the elements:
    -- Find its bucket in the bigger, new array
    -- Put it there
    """

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.total / self.get_num_slots()


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    # why 5381 and 33? https://stackoverflow.com/a/31621312
    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        
        for char in key:
            hash = (hash * 33) + ord(char)
        
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        bucket = self.hash_index(key)

        if self.storage[bucket] is None:
            self.storage[bucket] = HashTableEntry(key, value)
            self.total += 1

            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)
        else:
            # COLLISION
            current = self.storage[bucket]

            while current.next is not None and current.key != key:
                current = current.next

            if current.key == key:
                # Overwrite
                current.value = value
            else:
                # Add if key does not exist
                current.next = HashTableEntry(key, value)
                self.total += 1

                if self.get_load_factor() > 0.7:
                    self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        bucket = self.hash_index(key)

        current = self.storage[bucket]

        if current is None:
            print('KEY WAS NOT FOUND!!!')
        elif current.key == key:
            self.storage[bucket] = current.next
            self.total -= 1
        else:
            # Look for key in next
            while current.next is not None and current.next.key != key:
                current = current.next

            if current.next.key == key:
                current.next = current.next.next
                self.total -= 1
            else:
                print('KEY WAS NOT FOUND!!!')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        bucket = self.hash_index(key)

        if self.storage[bucket] is not None:
            current = self.storage[bucket]

            while current is not None and current.key != key:
                current = current.next

            if current:    
                return current.value
            else:
                return None
        else: 
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        new_storage = [None for i in range(new_capacity)]

        # Traverse storage
        for l_list in self.storage:
            current = l_list

            while current is not None:
                bucket = self.hash_index(current.key)

                if new_storage[bucket] is None:
                    new_storage[bucket] = HashTableEntry(current.key, current.value)
                else:
                    new_current = new_storage[bucket]

                    while new_current.next is not None:
                        new_current = new_current.next
                    
                    new_current.next = HashTableEntry(current.key, current.value)

                current = current.next

        self.storage = new_storage


    def __repr__(self):
        return str(self.storage)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))
    
    # print(ht.total)

    # # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # print("")
