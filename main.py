import csv

from UniversityUPS.HashTable1 import HashTable
from DistanceMatrix import *


# Read CSV file as list to get number of packages
counter = list(csv.reader(open("WGUPS Package File.csv")))
package_count = len(counter)
# print(len(counter))

# create hashtable object with size corresponding to number of packages
package_hashtable = HashTable(package_count)

# populate hashtable with rows from csv

with open("WGUPS Package File.csv", "r") as csv_file:
    package_list = csv.reader(csv_file)

    for line in package_list:
        i = int(line[0])
        package_hashtable.put(i, [line[1], line[2], line[3], line[4], line[5], line[6], line[7]])
        # package_hashtable.get(i)


# Create an AddressMatrix object to hold addresses and distances from csv file
city_map_matrix = AddressMatrix()

# This part iterates over the distances csv and adds the first row,
# which is the addresses, to the address_map
with open("WGUPS Distance File Cleaned.csv", "r") as csv_file:
    distances_csv = csv.reader(csv_file)

    # next skips the header row in csv file.
    next(distances_csv)
    for line in distances_csv:

        city_map_matrix.add_address(line[0])

print(city_map_matrix.address_map)

