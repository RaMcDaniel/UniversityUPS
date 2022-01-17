from Address import Addresses
from Package import *
from HashTable1 import HashTable
from DistanceMatrix import *

# Create instance of packages class
todays_packages = Packages()

# This obtains the number of packages from CSV file.
number_packages = todays_packages.get_number_of_packages("WGUPS Package File.csv")

# This creates hashtable object with size corresponding to number of packages
package_hashtable = HashTable(number_packages)


# This populates hashtable with rows from csv
todays_packages.create_package_objects("WGUPS Package File.csv", package_hashtable)
# These lines test that individual packages made it to the hashmap
# package_hashtable.get(1)
# package_hashtable.get(40)

# This creates an AddressMatrix object to hold addresses and distances from csv file
city_map_matrix = AddressMatrix()

# This creates an instance of the Addresses class to utilize those methods
todays_addresses = Addresses()

# This part iterates over the distances csv and adds the first item of each row,
# which is the addresses, to the address_map. These are the nodes of the graph.
todays_addresses.put_addresses_in_city_map_matrix("WGUPS Distance File Cleaned.csv", city_map_matrix)
# This tests that addresses were added to hashmap correctly
# print(city_map_matrix.address_map)

# This function completes the address_map by adding the distance vertices
# This takes two steps:
# 1. extract distances from csv to a 2D array

distance_array = todays_addresses.put_distances_in_array("WGUPS Distance File No Addresses.csv")
# This line tests the contents of the distance_array. It is correct with added ' ' at end of lines.
# print(distance_array)

# 2. create a loop that populates the distance data using the
# city_map_matrix.add_distance(address1, address2, distance) method
# address 1 comes from todays_addresses.address_list
# address 2 comes from todays_addresses.address_list with fancy counters
# distances come from distance_array
# **** Probably not to above lines. ***REWORKING***
todays_addresses.put_distances_in_city_map_matrix(distance_array, city_map_matrix)

# This tests that all distance vertexes are loaded properly
# print(city_map_matrix.distance_between_addresses)
# print(todays_addresses.address_list)


# FINALLY
# Call the damn algorithm

# Make a user interface



