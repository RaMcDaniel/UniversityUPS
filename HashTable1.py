class HashTable(object):

    # table_size refers to size of list you will make into hash table.
    def __init__(self, table_size):

        self.table_size = table_size
        self.key_buckets = [None] * self.table_size
        self.data_buckets = [None] * self.table_size

    def put(self, package_id, package_data):

        hash_value = self.hash_function(package_id, len(self.key_buckets))

        if self.key_buckets[hash_value] is None:
            self.key_buckets[hash_value] = package_id
            self.data_buckets[hash_value] = package_data

        else:

            if self.key_buckets[hash_value] == package_id:
                self.data_buckets[hash_value] = package_data

            else:

                next_bucket = self.hash_again(hash_value, len(self.key_buckets))

                while self.key_buckets[next_bucket] is not None and self.key_buckets[next_bucket] != package_id:
                    next_bucket = self.hash_again(next_bucket, len(self.key_buckets))

                if self.key_buckets[next_bucket] is None:
                    self.key_buckets[next_bucket] = package_id
                    self.data_buckets[next_bucket] = package_data

                else:
                    self.data_buckets[next_bucket] = package_data

    def hash_function(self, key_package_id, table_size):
        # simple remainder method modulo hash function
        return key_package_id % table_size

    def hash_again(self, previous_hash, size):
        return (previous_hash + 1) % size

    def get(self, key):
        start_bucket = self.hash_function(key, len(self.key_buckets))
        data = None
        stop = False
        found = False
        position = start_bucket

        while self.key_buckets[position] is not None and not found and not stop:

            if self.key_buckets[position] == key:
                found = True
                data = self.data_buckets[position]

            else:
                position = self.hash_again(position, len(self.key_buckets))
                if position == start_bucket:
                    stop == True
        print(data)
        return data


h = HashTable(5)
print(h)

h.put(1, ["wer", "wef", "sdtgg"])
h.put(2, ["wer", "wef", "sdtgg", "sdfs"])
h.get(2)



