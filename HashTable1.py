class HashTable(object):

    # table_size refers to size of list you will make into hash table.
    def __init__(self, table_size):

        self.table_size = table_size
        self.key_buckets = [None] * self.table_size
        self.data_buckets = [None] * self.table_size

    def put(self, key, data):

        hash_value = self.hash_function(key, len(self.key_buckets))

        if self.key_buckets[hash_value] is None:
            self.key_buckets[hash_value] = key
            self.data_buckets[hash_value] = data

        else:

            if self.key_buckets[hash_value] == key:
                self.data_buckets[hash_value] = data

            else:

                next_slot = self.rehash(hash_value, len(self.key_buckets))

                while self.key_buckets[next_slot] is not None and self.key_buckets[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.key_buckets))

                if self.key_buckets[next_slot] is None:
                    self.key_buckets[next_slot] = key
                    self.data_buckets[next_slot] = data

                else:
                    self.data_buckets[next_slot] = data

    def hash_function(self, key, size):
        # simple remainder method modulo hash function
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.key_buckets))
        data = None
        stop = False
        found = False
        position = start_slot

        while self.key_buckets[position] is not None and not found and not stop:

            if self.key_buckets[position] == key:
                found = True
                data = self.data_buckets[position]

            else:
                position = self.rehash(position, len(self.key_buckets))
                if position == start_slot:
                    stop == True
        return data


h = HashTable(5)

h[1] = "one"
h[2] = "two"
h[3] = "three"
h[4] = "four"
h[5] = "five"

print(h[3])

