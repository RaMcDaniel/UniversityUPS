class HashTable(object):

    # The hashtable is the data structure holding all package information.
    # Two parallel arrays hold the keys (package #), and the values (package data).
    # A hashtable is ultimately a set of empty buckets you can store data in, so key_buckets can hold
    # package numbers, and data buckets can hold package information.
    # Since table size will always equal the number of rows in the package CSV, we don't need to account for collisions.
    def __init__(self, table_size):

        self.table_size = table_size
        self.key_buckets = [None] * self.table_size
        self.data_buckets = [None] * self.table_size

    # B3.20 Space complexity: O(1)
    # One variable is updated, regardless of package number
    # B3.20 Time Complexity: O(1)
    # Hash tables do not require loops to access.
    # This function can update a particular piece of data in the hashtable.
    # The place in the table is obtained by recreating the hashfunction of package_id, and then
    # the corresponding data_bucket index (index, for example, [0] would be address) is updated with updated_value.
    def update(self, package_id, index, updated_value):
        hash_value = self.hash_function(package_id, len(self.key_buckets))
        self.data_buckets[hash_value][index] = updated_value

    # B3.4 Space complexity: O(n)
    # The hash map corresponds to the size of the package list
    # B3.4 Time Complexity: O(1) - O(n)
    # No collisions is O(1), worst case scenario, with rehashes, it could reach O(n) before terminating.
    # This part adds packages to the hashtable. It provides a fix for collisions via the path under "else:", but
    # this shouldn't happen with this package set. It would be necessary if the hashfunction wasn't %number of packages.
    # Hashmap implementation help obtained from: ***REFERENCE***
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

    # B3.22 Space complexity: O(1)
    # One variable is created regardless of package number.
    # B3.22 Time Complexity: O(1)
    # One calculation is performed regardless of package number.
    # This is a simple remainder method modulo hash function. %package number is the bucket that package will go into.
    # This is super simple because table size = # of packages, and there is one bucket for each.
    def hash_function(self, key_package_id, table_size):
        return key_package_id % table_size

    # A secondary hash function is an attempt for find an empty bucket. This simple one just adds 1 to previous hash.
    def hash_again(self, previous_hash, size):
        return (previous_hash + 1) % size

    # B3.21 Space complexity: O(1)
    # This prints one line, regardless of number of packages in system.
    # B3.21 Time Complexity: O(n)
    # Worst case scenario, if the package is not present, it loops through the entire hashmap once.
    # This method obtains information already in the hashmap. It loops through the hashmap and finds the bucket that
    # isn't None (empty) and is found (the bucket == key).
    # else: gives an out of the loop. If you get back to start bucket, it means you've traversed the whole thing,
    # so that package must not be in the system. This would happen for any package not 1-40.
    # Hashmap implementation help obtained from (James, 2016).
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
                    data = "Package not in system"
                    break
        # This prints the package information for the user. The formatting is for readability. (GeeksforGeeks, 2020)
        # data[0][0:22] cuts long address short, and the .ljust methods pads each column for equal size.
        print(key, "\t", data[0][0:22].ljust(25), data[1][0:16].ljust(16), data[2], data[3], "\t", data[4][0:9].ljust(9)
              , "\t", data[5].ljust(8), data[7], "\t", data[8].ljust(35), "\t", data[9])
        return data
