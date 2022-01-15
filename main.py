import csv

from Package import *
from HashTable1 import HashTable
from DistanceMatrix import *


Packages.get_number_of_packages("WGUPS Package File.csv")

# create hashtable object with size corresponding to number of packages
package_hashtable = HashTable(Packages.get_number_of_packages())

# populate hashtable with rows from csv
Packages.put_packages_in_hashmap("WGUPS Package File.csv")

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

