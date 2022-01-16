import csv


# The Address file stores address information and the functions that obtain it from the CSV.


class Addresses:
    def __init__(self):
        # This list is useful in other methods
        self.address_list = []
        self.address_distances = [[]]

    def put_addresses_in_city_map_matrix(self, address_csv, address_matrix):
        with open(address_csv, "r") as csv_file:
            distances_csv = csv.reader(csv_file)

            # next skips the header row in csv file to get to first row of data.
            next(distances_csv)
            for line in distances_csv:
                address_matrix.add_address(line[0].lstrip())
                self.address_list.append(line[0].lstrip())

    def put_distances_in_array(self):
        pass
        # this method returns the array to distance_array variable in main
        # figure out how to move distances to array

    def put_distances_in_city_map_matrix(self, distance_array, distances_matrix):
        pass

        # for address in address list
            # while i < 27 i=0, from index 0 to index  i, i++
                # ?????
        # This method does fancy loops to pass info to the
        #***** distances_matrix.add_distance(address1, address2, distance) method*****
        # **** scratch that!? Create Node objects with weighted vertices?*****





        # This tests that addresses were added to hashmap correctly
        # print(address_matrix.address_map)

        # This tests that the address list populates properly
        # print(self.address_list)
