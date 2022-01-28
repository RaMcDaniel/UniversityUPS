# This is a version the nearest neighbor algorithm. From each destination, it loops through the distances available to
# any given next destination, records those distances in a temporary dictionary, sorts that dictionary, and then
# chooses the first one (which is the shortest) to follow. The process is then repeated with the next set of potentials.
# the 3 individual trucks go through this algorithm separately.

class NearestNeighbor:
    def __init__(self, trucks, truck_num, city_map_matrix, todays_addresses, package_hashtable):
        self.package_hashtable = package_hashtable
        self.city_map_matrix = city_map_matrix
        self.todays_addresses = todays_addresses
        self.start_node = "4001 South 700 East"  # This is the hub.
        self.min_distance = 50  # arbitrary large distance to start the process.
        self.ordered_traversal_list = ["hub"]
        self.already_traversed = []
        self.ordered_distance_dict = {}
        self.truck_mileage = 0

        # The algorithm loops through a different set of packages based on what truck_num you gave it.
        if truck_num == 1:
            self.truck_set = trucks.truck1_set
        elif truck_num == 2:
            self.truck_set = trucks.truck2_set
        else:
            self.truck_set = trucks.truck3_set

    # B3.12 Space complexity: O(1)
    # It holds one variable
    # B3.12 Time Complexity: O(1)
    # Accessing a hash map goes straight to value, no loops required
    # This retrieves addresses from the hashmap. It would be a straight forward match with the values in this class,
    # except for package #40. The modulo function would have put it in bucket 0.
    def get_address(self, package):
        if package == 40:
            current_address = self.package_hashtable.data_buckets[0][0]
            return current_address
        else:
            current_address = self.package_hashtable.data_buckets[package][0]
            return current_address

    # B3.13 Space complexity: O(1)
    # It holds one variable
    # B3.13. Time Complexity: O(1)
    # Accessing a dictionary requires no loops.
    # This retrieves distances between addresses specified from the dictionary and returns them.
    def get_distance_between_addresses(self, address1, address2):
        distance = self.city_map_matrix.distance_between_addresses[address1, address2]
        return distance

    # For the package list given for one truck, this method returns an ordered list for the truck to traverse.
    def get_ordered_list(self):
        current_package = self.start_node
        for i in range(0, len(self.truck_set)):
            # This time it just loops once, for the first leg of the trip, because you have to account for the hub.
            if i == 0:
                # The temp_dict holds distances between current address and all potential others.
                temp_dict = {}
                for package in self.truck_set:
                    # Meaning, that address isn't already visited.
                    if package not in self.ordered_traversal_list:
                        # This gets the address associated with that package.
                        package_address = self.get_address(package)
                        # Meaning, the address is not where you currently are. This is important because the distance
                        # between the address and itself in not in the matrix, and will return a key error.
                        if package_address != self.start_node:
                            value = self.get_distance_between_addresses(self.start_node, package_address)
                            # This distance retrieved is cast as a float and put in temp_dict.
                            temp_dict[package] = float(value)
                # This sorts the dictionary so the first item (the shortest next distance) can be easily chosen (AskPython, 2021).
                # Information about lambda function retrieved from: (Pawnadeep, 2021)
                sorted_temp_dict = dict(sorted(temp_dict.items(), key=lambda item: item[1]))
                # The destination of the shortest next path is now your current position for the next loop.
                # Dictionaries aren't iterable, so to get the 1st item you have to make a list of it.
                # To avoid excessive complexity, a list of just one item, the first, is created.
                current_package = list(sorted_temp_dict)[0]
                # This newly discovered stop is added to the ordered_traversal_list.
                self.ordered_traversal_list.append(current_package)
                # And, the distance of that particular stop is added to ordered_distance_dict.
                self.ordered_distance_dict[current_package] = sorted_temp_dict.get(current_package)

            # Else is for all iteration of the loop except the 1st.
            # This part is identical to the last, except you have to retrieve both addresses, you can't just reference
            # the start.node address assigned above. Current_address is updated each loop.
            else:
                temp_dict = {}
                for package in self.truck_set:
                    if package not in self.ordered_traversal_list:
                        package_address = self.get_address(package)
                        current_address = self.get_address(current_package)
                        if package_address != current_address:
                            # Current address was assigned in the first loop - the first destination post-hub.
                            value = self.get_distance_between_addresses(current_address, package_address)
                            temp_dict[package] = float(value)
                            sorted_temp_dict = dict(sorted(temp_dict.items(), key=lambda item: item[1]))
                # Here, current_package is reassigned to the first address of the sorted dictionary. This represents
                # the truck moving to the next stop. The next loop will compare each stop left with this current one.
                current_package = list(sorted_temp_dict)[0]
                # Continue to add each new, nearest, stop to the ordered_traversal_list and corresponding distance
                # to the ordered_distance_dict.
                if current_package not in self.ordered_traversal_list:
                    self.ordered_traversal_list.append(current_package)
                    self.ordered_distance_dict[current_package] = sorted_temp_dict.get(current_package)

        # At the end of this set of nested loops, you have an ordered_traversal_list, but it is lacking the
        # return of the truck from the last stop to the hub.
        # hub_address_string obtains the address from last stop back to the hub address (start.node), and
        # adds it to the end of the ordered_distance_dict.
        hub_address_string = self.get_distance_between_addresses((self.get_address(current_package)), self.start_node)
        self.ordered_distance_dict["hub"] = float(hub_address_string)
        # This dictionary in order to sum the distance values. Total mileage can be calculated from this.
        self.truck_mileage = sum(self.ordered_distance_dict.values()) # (phihagphihag, n.d.)
        # The ordered_traversal_list is returned to main to be used in the timing class that handles time stamps.
        return self.ordered_traversal_list






