import datetime
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
    def __init__(self, report_time_object, size=16):
        self.report_time_object = report_time_object
        self.size = size
        # These are the manually sorted trucks
        self.truck1_set = [1, 2, 8, 13, 14, 15, 16, 19, 20, 26, 29, 37, 40]  # packages with early deadlines
        self.truck2_set = [3, 6, 11, 12, 17, 18, 23, 25, 30, 31, 34, 35, 36, 38]  # truck goes out @ 905
        self.truck3_set = [4, 5, 7, 9, 10, 21, 22, 24, 27, 28, 32, 33, 39]  # packages that must leave later, 6 and 25 must be near start

    def convert_time_to_time_object(self, time):
        today_date = "01-22-2022 "
        seconds = "00"
        combo_time = today_date + time + seconds
        time_obj = datetime.datetime.strptime(combo_time, '%m-%d-%Y %H%M%S')
        return time_obj
        # return time_obj.strftime('%H:%M')

    # This method updates hashmap with the truck each package is on.
    def update_truck_in_hashmap(self, truck_num, hashmap):
        if truck_num == 1:
            truck_set = self.truck1_set
        elif truck_num == 2:
            truck_set = self.truck2_set
        else:
            truck_set = self.truck3_set

        for package in truck_set:
            # 7 corresponds to the index of truck number in package data
            hashmap.update(package, 7, truck_num)

    # This method updates hashmap with the package status when truck leaves the hub.
    def truck_start_time(self, truck_num, hashmap, start_time):
        if truck_num == 1:
            truck_set = self.truck1_set
        elif truck_num == 2:
            truck_set = self.truck2_set
        else:
            truck_set = self.truck3_set

        if type(start_time) is str:
            start_time = self.convert_time_to_time_object(start_time)
        # print(f"start time object: {start_time}")
        # print(f"report time object: {self.report_time_object}")

        if start_time <= self.report_time_object:
            for package in truck_set:
                # 9 corresponds to the index of status information in package data
                hashmap.update(package, 9, f"On truck, left at: {start_time}")
                # print(start_time_object)
        return start_time

    def trucks_delivered(self, truck_num, hashmap):
        if truck_num == 1:
            truck_set = self.truck1_set
        elif truck_num == 2:
            truck_set = self.truck2_set
        else:
            truck_set = self.truck3_set

        for package in truck_set:
            # 9 corresponds to the index of status information in package data
            hashmap.update(package, 9, f"Package delivered.")
            # print(start_time_object)

