# This is where the main nearest neighbor implementation goes.
# the 3 individual trucks go through this algorithm separately

# 1.      Loop through the packages assigned to the truck (since the order was determined by the algorithm above)
# a.      For each package, have the truck figure out what the next best address is to go to (shortest distance)
# i.     Nearest neighbor algorithm works well for this and will come in under 140 miles

# 2.      Deliver the package by timestamping it in the hash table.
# a.      NOTE: Don’t be afraid to add an additional timestamp field within the package class.
# 3.      Keep track of the distance traveled starting from the hub
# 4.      Display total round-trip distance once all packages have been delivered.
# a.      This needs to include the distance back to the hub when the truck is finished
class NearestNeighbor:
    def __init__(self, trucks, truck_num, city_map_matrix, todays_addresses, package_hashtable):
        self.package_hashtable = package_hashtable
        self.city_map_matrix = city_map_matrix
        self.todays_addresses = todays_addresses
        self.node = ""
        self.start_node = "4001 South 700 East"
        self.min_distance = 50  # arbitrary large distance
        self.ordered_traversal_list = ["hub"]
        self.already_traversed = []
        self.ordered_distance_dict = {}
        self.truck_mileage = 0

        if truck_num == 1:
            self.truck_set = trucks.truck1_set
        elif truck_num == 2:
            self.truck_set = trucks.truck2_set
        else:
            self.truck_set = trucks.truck3_set

    def get_address(self, package):
        if package == 40:
            current_address = self.package_hashtable.data_buckets[0][0]
            return current_address
        else:
            current_address = self.package_hashtable.data_buckets[package][0]
            return current_address

    def get_distance_between_addresses(self, address1, address2):
        distance = self.city_map_matrix.distance_between_addresses[address1, address2]
        return distance

    def get_ordered_list(self):
        # print(self.truck_set)
        length = len(self.truck_set)
        # print(length)

        current_package = self.start_node
        for i in range(0, len(self.truck_set)):
            if i == 0:
                temp_dict = {}
                for package in self.truck_set:
                    if package not in self.ordered_traversal_list:
                        package_address = self.get_address(package)
                        if package_address != self.start_node:
                            value = self.get_distance_between_addresses(self.start_node, package_address)
                            # print(value)
                            temp_dict[package] = float(value)
                            # print(temp_dict)
                # print(temp_dict)
                sorted_temp_dict = dict(sorted(temp_dict.items(), key=lambda item: item[1]))
                # print(sorted_temp_dict)
                current_package = list(sorted_temp_dict)[0]
                    # next(iter(sorted_temp_dict))
                # current_package_address = self.get_distance_between_addresses(self.start_node, current_package)
                # print(current_package)
                self.ordered_traversal_list.append(current_package)
                self.ordered_distance_dict[current_package] = sorted_temp_dict.get(current_package)
                # self.ordered_distance_dict[current_package] = current_package_address
                # print(self.ordered_traversal_list)
                # current_package = closest package you determined
            else:
                temp_dict = {}
                # print(current_package)
                for package in self.truck_set:
                    if package not in self.ordered_traversal_list:
                        package_address = self.get_address(package)
                        current_address = self.get_address(current_package)
                        if package_address != current_address:
                            value = self.get_distance_between_addresses(current_address, package_address)
                            temp_dict[package] = float(value)
                            # print(temp_dict)
                            sorted_temp_dict = dict(sorted(temp_dict.items(), key=lambda item: item[1]))
                            # print(sorted_temp_dict)
                current_package = list(sorted_temp_dict)[0]
                # print(f"what's this? {current_package}")
                if current_package not in self.ordered_traversal_list:
                    self.ordered_traversal_list.append(current_package)
                    self.ordered_distance_dict[current_package] = sorted_temp_dict.get(current_package)
                        # print(self.ordered_traversal_list)
        hub_address_string = self.get_distance_between_addresses((self.get_address(current_package)), self.start_node)
        self.ordered_distance_dict["hub"] = float(hub_address_string)
        # print(self.ordered_traversal_list)
        # print(self.ordered_distance_dict)
        # print(self.ordered_distance_dict)
        self.truck_mileage = sum(self.ordered_distance_dict.values())
        # print(self.truck_mileage)
        return self.ordered_traversal_list







