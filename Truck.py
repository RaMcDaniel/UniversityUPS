import datetime
# This file will create a truck class and load packages into them manually.


class Truck:
    def __init__(self, report_time_object, size=16):
        self.report_time_object = report_time_object
        self.size = size
        # These are the manually sorted trucks.
        self.truck1_set = [1, 2, 8, 13, 14, 15, 16, 19, 20, 26, 29, 37, 40]  # Packages with early deadlines, leaves @ 8
        self.truck2_set = [3, 6, 11, 12, 17, 18, 23, 25, 30, 31, 34, 35, 36, 38]  # Goes out @ 0905
        self.truck3_set = [4, 5, 7, 9, 10, 21, 22, 24, 27, 28, 32, 33, 39]  # Packages that must leave later,

    # This function adds dates and seconds to make complete datetime objects.
    def convert_time_to_time_object(self, time):
        today_date = "01-22-2022 "
        seconds = "00"
        combo_time = today_date + time + seconds
        # This converts strings to datetime objects with specified formatting.
        time_obj = datetime.datetime.strptime(combo_time, '%m-%d-%Y %H%M%S')
        return time_obj

    # This method updates the hashmap with the truck each package is on. It references a different truck list
    # depending on which truck_num you created the object with.
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

    # This method updates the hashmap with the package status when truck leaves the hub.
    def truck_start_time(self, truck_num, hashmap, start_time):
        if truck_num == 1:
            truck_set = self.truck1_set
        elif truck_num == 2:
            truck_set = self.truck2_set
        else:
            truck_set = self.truck3_set

        # start_time can be a string or a datetime object. If it is a string, this converts it to an object.
        if type(start_time) is str:
            start_time = self.convert_time_to_time_object(start_time)

        # When the truck leaves (when start_time is before the user report time), status is updated in the hashtable.
        if start_time <= self.report_time_object:
            for package in truck_set:
                # 9 corresponds to the index of status information in package data
                hashmap.update(package, 9, f"On truck, left at: {start_time}")
        return start_time

    # This is another status update method, except this one updates to "Package delivered." It is called by a different
    # function later that handles package delivery times.
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

