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
        self.end_node = "4001 South 700 East"
        self.min_distance = 50  # arbitrary large distance
        self.ordered_traversal_list = ["hub"]

        if truck_num == 1:
            self.truck_set = trucks.truck1_set
        elif truck_num == 2:
            self.truck_set = trucks.truck2_set
        else:
            self.truck_set = trucks.truck3_set

        self.length = len(self.truck_set)
        self.i = 1

    def get_ordered_list(self):
        current_address = self.start_node
        min_distance = self.min_distance
        packages_left = self.truck_set
        print(packages_left)

        i = 0
        for i in range(len(packages_left)):
            package_info = self.package_hashtable.get(packages_left[i])
            package_address = package_info[0]
            distance_btwn_node_package = self.city_map_matrix.distance_between_addresses[current_address, package_address]
            print(packages_left[i])
            print(min_distance)
            if float(distance_btwn_node_package) < min_distance:
                min_distance = float(distance_btwn_node_package)
                current_package = packages_left[i]
                print(packages_left[i])
                print(min_distance)
                print(current_package)

        print(current_package)
        print(min_distance)








        #
        # node = self.start_node
        # truck_set_clone = self.truck_set.copy()
        # min_distance = self.min_distance
        # for package in truck_set_clone: # This clone you'll be removing 1st item from and can use in outer loop
          #  print(f"package = {package}")
           # package_info = self.package_hashtable.get(package)
            # package_address = package_info[0]
            #print(f"package_address = {package_address}")
            # if node != package_address:
              #  for inner_package in self.truck_set:
               #     print(f"package = {inner_package}")
                #    package_info = self.package_hashtable.get(inner_package)
                 #   package_address = package_info[0]
                  #  print(f"package_address = {package_address}")
                   # distance_btwn_node_package = self.city_map_matrix.distance_between_addresses[node, package_address]
                   # print(node)
                   # print(distance_btwn_node_package)
                   # if float(distance_btwn_node_package) < min_distance:
                    #    min_distance = float(distance_btwn_node_package)
                     #   print(min_distance)
                # node = package_address
                # print(node)
                # while distance btwn node and package is less than self.min_distance
                    # node = address of package
                    # self.min_distance = distance between node and package


               # truck_set.remove(package)
        #self.ordered_traversal_list.append("hub")
        #print(self.ordered_traversal_list)
        # return self.ordered_traversal_list


