# This file will create a truck class and load packages.

#    i.     Prioritization Algorithm
# 1. Create an algorithm that will look at the package data ONLY (no distances)
# and will figure out which package goes on which truck.
# (OPTION 2.1)
#   a.This typically means creating a list that stores the package ids associated with each truck
# i.     Later, you can use the hash table.lookup(package id) method to access that package associated
# with each package id.
# ii.     The hash table should be a primary table for the latest information about the packages.
# iii.     Do not duplicate the package objects outside of the hash table. This will lead to synchronization
# issues later on.


# You want to end this with 3 loaded truck objects
# truck objects are loaded with package objects from elsewhere

class Truck:
    def __init__(self, size=16):
        self.size = size
        self.truck1_set = [1,8, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40] # packages with early deadlines
        self.truck2_set = [3, 4, 7, 10, 11, 12, 17, 18, 19, 21, 22, 23, 24, 26, 36, 38] # truck goes out simultaneously with #1
        self.truck3_set = [2, 5, 6, 9, 25, 27, 28, 32, 33, 35, 39] # packages that must leave later, 6 and 25 must be near start
                            # 9 can't be del until 1020

    def update_truck_in_hashmap(self, truck_num):
        pass
    # find way to update 8th index of list in hashtable, for given key, to truck number.

    def truck_start_time(self, truck_num, start_time):
        pass
    # update status of objects in hashtable, index 10, to in transit
    # return start_time? for time delta later
