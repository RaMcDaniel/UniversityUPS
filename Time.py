import DeliveryAlgorithm
import datetime


class Timing:
    def __init__(self, truck_route, city_map_matrix):
        self.truck_route = truck_route
        self.city_map_matrix = city_map_matrix
        self.trip_leg_times = []

    # def get_distance_between_addresses(self, package1, package2):
    #    if package1 == "hub":
     #       package1 ="4001 South 700 East"
     #   if package2 == "hub":
     #       package2 = "4001 South 700 East"
     #   distance = self.city_map_matrix.distance_between_addresses[package1, package2]
     #   return distance

    def convert_time_to_time_object(self, time):
        today_date = "01-24-2022 "
        seconds = "00"
        combo_time = today_date + time + seconds
        print(combo_time)
        time_obj = datetime.datetime.strptime(combo_time, '%m-%d-%Y %H%M%S')
        # print(date_obj)
        return time_obj.strftime('%H:%M')

    def convert_distance_to_time(self, distance):
        print(distance)
        time_in_min = distance/0.3  # 18 miles per hour= 0.3 miles/min
        print(time_in_min)
        minutes = round(time_in_min % 60)
        print(f"minutes {minutes}")
        hours = round((time_in_min - minutes)/60)
        print(f"hours {hours}")
        time_string = f"{hours}{minutes}"
        print(time_string)
        time_object = self.convert_time_to_time_object(time_string)
        print(time_object)
        return time_object
        # time = distance/18 # 18mph, answers is in hours

    def truck3_start_time(self, truck1_end_time, truck2_end_time):
        if truck1_end_time < truck2_end_time:
            return truck1_end_time
        else:
            return truck2_end_time

    def get_delivery_times(self, nearest_neighbor, report_time_object):
        report_time = report_time_object
        print(nearest_neighbor.ordered_distance_dict)
        print(self.truck_route)

        distance_piece_time_sum = 0
        for key in nearest_neighbor.ordered_distance_dict:
            distance_piece = nearest_neighbor.ordered_distance_dict[key]
            distance_piece_time = self.convert_distance_to_time(distance_piece)
            distance_piece_time_sum += distance_piece_time
            print(distance_piece)
            # print(distance_piece_time)
            print(distance_piece_time_sum)

        time_sum = self.convert_distance_to_time(distance_piece_time_sum)
        print(time_sum)






        # do a thing with list from self.truck_route
        # add all delivery times to hashtable
        # update list of trip  leg times
        # return self.trip_leg_times - will be list called truck?_times_list

    def route_end_time(self, trip_leg_times):
        pass
        # sum up trip leg times
        # then calculate delta from start time
        # return truck end time and mileage - will be in variable of datetime object called truck?_end_time
