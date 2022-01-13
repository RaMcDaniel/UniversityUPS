import csv

from UniversityUPS.HashTable1 import HashTable


# Read CSV file to get number of packages
counter = list(csv.reader(open("WGUPS Package File.csv")))
package_count = len(counter)
# print(len(counter))

# create hashtable object with size corresponding to number of packages
package_hashtable = HashTable(package_count)
package_hashtable.put(1, ["hello", "there"])
package_hashtable.get(1)
