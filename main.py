from Address import Addresses
from Package import *
from HashTable1 import HashTable
from DistanceMatrix import *
from Truck import *
from DeliveryAlgorithm import *
from Time import *

# C1: Rebecca McDaniel, Student ID: 001426057

# B3 Total: Overall Time Complexity: O(n log n^2) - O(n^2)
# Best case scenario, only a subset of the packages (within a specific truck), so through nested loops, which
# O(n log n^2). Worst case scenario, if there is a single search for a package that is not present in the hashmap,
# the entire hashmap list will be in a nested loop, which brings it to O(n^2).
# Overall Space Complexity: O(n log n^3)
# There is one function where 2 temporary dictionaries are created each loop, and a permanent one is created throughout.
# These dictionaries only consist of a subset of N though (just 1 truck), no it's not as bad as O(n^3).

# B3.1 Space complexity: O(1)
# This interface part holds a constant five variables at all times.
# B3.1 Time Complexity: 0(1)
# Run time does not change no matter what time the user enters, and is unrelated to other parts of program.

# This is the user interface. This sets up the scenario and explains the permitted responses.
# The f string formatting centers the printed strings.
print(f"{'Welcome to WGUPS Package Management System' : ^125}")
print(f"{'You are auditing the system from 1/22/2022' : ^125}")
print(f"{'Enter a time between 0800 and 1800 in HHMM format' : ^125}")

# The next set of lines asks the user for the time they'd like to run the audit for.
# combo_time adds additional information to create a complete datetime object using strptime.
# datetime objects are necessary for timekeeping throughout.
# This program could be improved in the future by making the date changeable.
report_time = (input(f"{'Time:' : ^80}"))
today_date = "01-22-2022 "
seconds = "00"
combo_time = today_date + report_time + seconds
report_time_obj = datetime.datetime.strptime(combo_time, '%m-%d-%Y %H%M%S')

# Create instance of packages class
todays_packages = Packages()

# B3.2 Space complexity: O(n)
# The size of the CSV and the list is creates is as big as the number of packages.
# B3.2 Time Complexity: O(n)
# It loops through each package in the CSV once.
# This obtains the number of packages from CSV file. This number is used in later functions.
number_packages = todays_packages.get_number_of_packages("WGUPS Package File.csv")

# This creates hashtable object with size corresponding to number_packages above.
package_hashtable = HashTable(number_packages)

# B3.3 Space complexity: O(n)
# objects created corespond to number of packages
# B3.3 Time Complexity: O(n)
# It is usually O(1), but could get to O(n) if the .put() method referenced loops all the way through
# This populates hashtable with rows from csv
todays_packages.create_package_objects("WGUPS Package File.csv", package_hashtable)

# This creates an instance of AddressMatrix, to hold addresses and distances from CSV file.
city_map_matrix = AddressMatrix()

# This creates an instance of the Addresses class to utilize methods pertaining to the addresses.
todays_addresses = Addresses()

# B3.5 Space complexity: O(n)
# It stores information once per address in list.
# B#.5 Time Complexity: O(n)
# It formats and adds an address once for each address given.
# This part iterates over the distances csv and adds the first item of each row, the addresses, to the address_map.
todays_addresses.put_addresses_in_city_map_matrix("WGUPS Distance File Cleaned.csv", city_map_matrix)

# B3.6 Space complexity: O(n)
# One array is created scaling with size of package list
# B3.6 Time Complexity: O(n)
# It creates an array based on each line in address CSV
# This Part completes the address_map by adding the corresponding distances.
# This takes two steps:
# 1. extract distances from csv to a 2D array
distance_array = todays_addresses.put_distances_in_array("WGUPS Distance File No Addresses.csv")

# B3.7 Space complexity: O(n)
# This creates one dictionary based on number of addresses and packages
# B3.7 Time Complexity: O(n^2)
# This is a nested loop that runs through the matrix, and then again for each entry in it.
# 2. create a loop that populates the distance data into city_map_matrix, using the address list and distances array.
todays_addresses.put_distances_in_city_map_matrix(distance_array, city_map_matrix)

# This creates an instance of the truck class. It needs the report_time_obj chosen by user to calculate package times.
trucks = Truck(report_time_obj)

# B3.8 Space complexity: O(1)
# This does not vary based on number of packages or addresses.
# B3.8 Time Complexity: O(1)
# This does not vary based on number of packages or addresses.
# The following lines address package #9 and its wrong address. If the user enters a time before 1020, #9 gets keeps
# its incorrect address, but if the time given is after 1020, the user is informed the package is updated, via
# the print statements, and the package object in the hashtable is updated via package_hashtable.update.
# It is on truck #3, which doesn't leave until after 1020, so the object's truck interaction is fine without change.
# The convert_time_to_time_object method is necessary to turn 1020 into an object that can be compared against.
update_time = "1020"
update_time_object = trucks.convert_time_to_time_object(update_time)

if report_time_obj >= update_time_object:
    package_hashtable.update(9, 0, "410 S State St")
    package_hashtable.update(9, 3, "84111")
    print("UPDATE: at 10:20, the address for package #9 was corrected.")
    print("It has been changed from '300 State St., Salt Lake City, UT	84103' to \n"
          "'410 S State St., Salt Lake City, UT 84111'. \nLuckily, that truck hadn't left yet.\n")

# B3.9 Space complexity: O(n)
# Worst case scenario, if the truck was bigger, it could hold each package once.
# B3.9 Time Complexity: O(log(n))
# Each truck will only ever loop through a subset of total packages
# This updates the package information in hashmap to include the truck number.
# These 3 functions loop through the items in each individual truck and add truck numbers.
trucks.update_truck_in_hashmap(1, package_hashtable)
trucks.update_truck_in_hashmap(2, package_hashtable)
trucks.update_truck_in_hashmap(3, package_hashtable)

# B3.10 Space complexity: O(n)
# It adds information to the hash table once per package.
# B3.10 Time Complexity: O(n)
# It adds to the hashmap once per package.
# The following two calls gives trucks 1 and 2 their start times.
# These methods take convert the string times (0800, 0905) to datetime objects, add those to the hashtable,
# and return the objects for later use.
truck1_start_time = trucks.truck_start_time(1, package_hashtable, "0800")
truck2_start_time = trucks.truck_start_time(2, package_hashtable, "0905")

# This makes an instance of NearestNeighbor class.
# NearestNeighbor is the main algorithm, and needs to know the specific truck, city_map_matrix, address list,
# and hashtable is it working with, which is why all the arguments.
nearest_neighbor = NearestNeighbor(trucks, 1, city_map_matrix, todays_addresses, package_hashtable)

# B3.11 Space complexity: O(n log n^3)
# This creates two temporary dictionaries each outer loop, so it holds a subset of n 3 times.
# B3.11 Time Complexity: O(n log n^2)
# This loops through each package for each package in the truck list, but the list is only a subset of n.
# This method implements a type of nearest neighbor algorithm on the 1st truck
# 'hub' is appended for later use in calculating times
truck1_route = nearest_neighbor.get_ordered_list()
truck1_route.append("hub")

# This makes a second instance of the NearestNeighbor class for truck 2
nearest_neighbor2 = NearestNeighbor(trucks, 2, city_map_matrix, todays_addresses, package_hashtable)

# B3.11 Space complexity: O(n log n^3)
# This creates two temporary dictionaries each outer loop, as well as 2 permanent data structures
# just once at the end.
# B3.11 Time Complexity: O(n log n^2)
# This loops through each package for each package in the truck list, but the list is only a subset of n
# B3.12 and B3.13 are called within, but those both have complexities of O(1), so don't add much.
# Space and time complexity: See B3.11. This is the same for the second truck.
# This method implements a type of nearest neighbor algorithm for the 2nd truck
truck2_route = nearest_neighbor2.get_ordered_list()
truck2_route.append("hub")

# This makes a third instance of the NearestNeighbor class for truck 3
nearest_neighbor3 = NearestNeighbor(trucks, 3, city_map_matrix, todays_addresses, package_hashtable)

# Space and time complexity: See B3.11. This is the same for the third truck.
# This method implements a type of nearest neighbor algorithm for the 3rd truck
truck3_route = nearest_neighbor3.get_ordered_list()
truck3_route.append("hub")

# Creates an instance of timing class for truck 1
# The timing class gets ordered lists of package distances and handles time stamps.
timing_truck1 = Timing(truck1_route, city_map_matrix, truck1_start_time, package_hashtable)

# B3.14 Space complexity: O(log(n))
# several variables are created once each loop for a subset of n
# B3.14 Time Complexity: O(log(n))
# One loop occurs for each in a subset of n
# This method adds individual delivery times to hashtable,
# and returns the time object when truck 1 makes it back to hub
truck1_return_time = timing_truck1.get_delivery_times(nearest_neighbor, report_time_obj)

# Creates an instance of timing class for truck 2
timing_truck2 = Timing(truck2_route, city_map_matrix, truck2_start_time, package_hashtable)

# Space and time complexity: See B3.14, this is the same for Truck 2.
# This method adds individual delivery times to hashtable,
# and returns the time object when truck 2 makes it back to hub
truck2_return_time = timing_truck2.get_delivery_times(nearest_neighbor2, report_time_obj)

# B3.15 Space complexity: O(1)
# It holds one variable regardless of package number.
# B3.15 Time Complexity: O(1)
# It compares two numbers once regardless of package number.
# This method compares the first two truck return times, and
# returns the time of the fastest truck.
truck3_start_time = timing_truck2.truck3_start_time(truck1_return_time, truck2_return_time)

# Space and time complexity: See B3.10, this is the same for Truck 3.
# Truck 3 leaves when the first other truck arrives back at the hub.
truck3_start_time = trucks.truck_start_time(3, package_hashtable, truck3_start_time)

# Creates an instance of timing class for truck 3
timing_truck3 = Timing(truck3_route, city_map_matrix, truck3_start_time, package_hashtable)

# Space and time complexity: See B3.14, this is the same for Truck 3
# This method adds individual delivery times to hashtable,
# and returns the time object when truck 3 makes it back to hub
truck3_return_time = timing_truck3.get_delivery_times(nearest_neighbor3, report_time_obj)

# B3.16 Space complexity: O(1)
# This stores one variable each time it is called regardless of package number.
# B3.16 Time Complexity: O(1)
# Only 1 variable is created regardless of package number.
# Each truck mileage is specific to the truck.
# It is obtained from the sum of dictionary values in the nearest neighbor class.
truck1_mileage = nearest_neighbor.truck_mileage
truck2_mileage = nearest_neighbor2.truck_mileage
truck3_mileage = nearest_neighbor3.truck_mileage

# B3.17 Space complexity: O(1)
# # This stores one variable each time it is called regardless of package number.
# B3.17 Time Complexity: O(1)
# Only 1 variable is created regardless of package number.
# This sums the mileages to get a total.
total_mileage = truck1_mileage + truck2_mileage + truck3_mileage

# B3.18 Space complexity: O(1)
# A set number of things are done stored regardless of package number, and nothing is created/stored
# B3.18 Time Complexity: O(n)
# It loops through the hashtable once, which is the size of the package number.
# This is a header for the package information table
print("Num. Address                   City             St  Zip      Due at      LB     Truck    Delivery Time                           Status")

# This prints the formatted package information
for id_num in range(1, number_packages+1):
    package_hashtable.get(id_num)

# These print truck return times to ensure the last truck arrives back during business hours.
print("\n")
print(f"truck 1 returned at: {truck1_return_time}")
print(f"truck 2 returned at: {truck2_return_time}")
print(f"truck 3 returned at: {truck3_return_time}")

# This prints the total mileage.
print("\n")
print(f"The total miles for all 3 trucks at the end of the day: {total_mileage}\n")
