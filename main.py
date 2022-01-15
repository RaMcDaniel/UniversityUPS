from Address import Addresses
from Package import *
from HashTable1 import HashTable
from DistanceMatrix import *

# Create instance of packages class
todays_packages = Packages()

number_packages = todays_packages.get_number_of_packages("WGUPS Package File.csv")

# create hashtable object with size corresponding to number of packages
package_hashtable = HashTable(number_packages)

# populate hashtable with rows from csv
todays_packages.put_packages_in_hashmap("WGUPS Package File.csv", package_hashtable)


# Create an AddressMatrix object to hold addresses and distances from csv file
city_map_matrix = AddressMatrix()

# This part iterates over the distances csv and adds the first row,
# which is the addresses, to the address_map

todays_addresses = Addresses()
todays_addresses.put_addresses_in_city_map_matrix("WGUPS Distance File Cleaned.csv", city_map_matrix)


