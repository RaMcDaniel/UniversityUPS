import datetime
from Address import Addresses
from Package import *
from HashTable1 import HashTable
from DistanceMatrix import *
from Truck import *
from DeliveryAlgorithm import *
from Time import *

print(f"{'Welcome to WGUPS Package Management System' : ^10}")
print("\n")
print(f"{'Enter a time between 0800 and 1800 in HHMM format' : ^10}")
report_time = (input('Time: '))
today_date = "01-24-2022 "
seconds = "00"
combo_time = today_date+report_time+seconds
report_time_obj = datetime.datetime.strptime(combo_time, '%m-%d-%Y %H%M%S')
# print(date_obj)
print(report_time_obj.strftime('%H:%M'))


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
# (distance_array)

# 2. create a loop that populates the distance data using the
# city_map_matrix.add_distance(address1, address2, distance) method
todays_addresses.put_distances_in_city_map_matrix(distance_array, city_map_matrix)

# This tests that all distance vertexes are loaded properly
# print(city_map_matrix.distance_between_addresses)
# print(city_map_matrix.distance_between_addresses["1060 Dalton Ave S", "4001 South 700 East"])
# print(todays_addresses.address_list)


# This creates an instance of the truck class
trucks = Truck()
# print(trucks.truck1_set)
# print(trucks.truck2_set)
# print(trucks.truck3_set)

# This updates the package information in hashmap to include the truck number
trucks.update_truck_in_hashmap(1, package_hashtable)
trucks.update_truck_in_hashmap(2, package_hashtable)
trucks.update_truck_in_hashmap(3, package_hashtable)

# The following two calls gives trucks 1 and 2 an 0800 start time
# adds 0800 to the hashtable for item in trucks 1 and 2
# and returns the start time for later use.

truck1_start_time = trucks.truck_start_time(1, package_hashtable, "0800")
truck2_start_time = trucks.truck_start_time(2, package_hashtable, "0800")

# Make an instance of NearestNeighbor class
nearest_neighbor = NearestNeighbor(trucks, 1, city_map_matrix, todays_addresses, package_hashtable)

# This method implements a type of nearest neighbor algorithm on the 1st truck
# 'hub' is appended for later use in calculating times
truck1_route = nearest_neighbor.get_ordered_list()
truck1_route.append("hub")

# Make a second instance of NearestNeighbor class for truck 2
nearest_neighbor2 = NearestNeighbor(trucks, 2, city_map_matrix, todays_addresses, package_hashtable)

# This method implements a type of nearest neighbor algorithm for the 2nd truck
truck2_route = nearest_neighbor2.get_ordered_list()
truck2_route.append("hub")

# Make a third instance of NearestNeighbor class for truck 3
nearest_neighbor3 = NearestNeighbor(trucks, 3, city_map_matrix, todays_addresses, package_hashtable)

# This method implements a type of nearest neighbor algorithm for the 3rd truck
truck3_route = nearest_neighbor3.get_ordered_list()
truck3_route.append("hub")

# This tests the route calculated by get_ordered_list for the 3 trucks
# print(truck1_route)
# print(truck2_route)
# print(truck3_route)

# ************YOU'RE HERE***************

# Creates an instance of timing class for truck 1
timing_truck1 = Timing(truck1_route, city_map_matrix)

# This method adds individual delivery times to hashtable,
# and returns a list of distances
truck1_distances = timing_truck1.get_delivery_times(nearest_neighbor, report_time_obj)

# This sums up the list of distances from truck 1 just obtained
# truck1_end_time = timing_truck1.route_end_time(truck1_distances)

# Creates an instance of timing class for truck 2
# timing_truck2 = Timing(truck1_route)

# This method adds individual delivery times to hashtable,
# and returns a list of distances for truck 2
# truck2_distances = timing_truck2.get_delivery_times()

# This sums up the list of distances from truck 1 just obtained
# truck2_end_time = timing_truck1.route_end_time(truck2_distances)




# This tests updates in hashmap
# for id_num in range(1, number_packages+1):
    # package_hashtable.get(id_num)









# FINALLY
# fix time stamp

# Make a user interface



