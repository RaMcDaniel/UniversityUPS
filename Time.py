import datetime


# This class handles times. It updates statuses and delivery times of packages based on comparison with the times
# given by the user and/or distances traveled by truck.
class Timing:
    def __init__(self, truck_route, city_map_matrix, truck_start_time, package_hashtable):
        self.package_hashtable = package_hashtable
        self.truck_start_time = truck_start_time
        self.truck_route = truck_route
        self.city_map_matrix = city_map_matrix

    # Times are calculated based on distance. MPH is given by instructor.
    # MPH is converted to time in minutes.
    # Minutes modulo 60 leaves the minutes as a remainder.
    # Minutes - that modulo and then divided by 60 is the hours.
    # A timedelta is created using the datetime library and those minutes and hours.
    # A timedelta is returned that can be added to the truck start time to get a time at each stop.
    def convert_distance_to_timedelta(self, distance):
        time_in_min = distance / 0.3  # 18 miles per hour= 0.3 miles/min
        minutes = time_in_min % 60
        hours = (time_in_min - minutes) / 60
        time_delta = datetime.timedelta(hours=hours, minutes=minutes)
        return time_delta

    # Truck 3 leaves when the first of truck 1 or 2 arrives back. This is determined by comparing the datetimes
    # of trucks' 1 and 2 returns.
    def truck3_start_time(self, truck1_end_time, truck2_end_time):
        if truck1_end_time < truck2_end_time:
            return truck1_end_time
        else:
            return truck2_end_time

    # This method puts the individual package delivery time of each package into the hashmap as the algorithm unfolds.
    # The hashmap is pre-populated with "Pending", so this method just changes that when appropriate.
    def get_delivery_times(self, nearest_neighbor, report_time_object):
        # This is when the truck leaves. All delivery times are calculated against this one.
        current_time = self.truck_start_time
        # For each entry in the ordered_distance_dictionary (Key is the destination, and value is miles to get there)...
        for key in nearest_neighbor.ordered_distance_dict:
            # the distance to that destination is obtained (distance_piece)
            distance_piece = nearest_neighbor.ordered_distance_dict[key]
            # And, that piece is converted to a timedelta
            distance_piece_time = self.convert_distance_to_timedelta(distance_piece)
            # Those time deltas for each loop are summed, and each loop's sum is the next loop's start time.
            new_time = current_time + distance_piece_time
            # If that new_time (the time the particular package arrived), is before the report time from user...
            if new_time <= report_time_object:
                if key != "hub":
                    # ... The status index of the package in hashtable is updated.
                    # And the delivery time index is also update with this sum, new_time.
                    # 9 corresponds to the index of status information in hashtable.
                    self.package_hashtable.update(key, 9, f"Package delivered.")
                    # 8 corresponds to the index of delivery time information in hashtable.
                    self.package_hashtable.update(key, 8, f"Delivered at: {new_time}.")
            current_time = new_time
        # It is also returned at the very end of the loops. This total sum is when the truck returns to the hub.
        return current_time



