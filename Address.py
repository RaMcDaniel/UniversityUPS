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

    def put_distances_in_array(self, address_csv_plain):
        distance_array = []
        with open(address_csv_plain, "r") as csv_file:
            distances_csv_plain = csv.reader(csv_file)

            for line in distances_csv_plain:
                distance_array.append(line)
                # The array created here has unnecessary ' ' at end of lines. These need to be filtered out
                # when moving array to city_map_matrix
        return distance_array

        # this method returns the array to distance_array variable in main
        # figure out how to move distances to array

    def put_distances_in_city_map_matrix(self, distance_array, distances_matrix):

        for i in range(0, 27):
            for j in range(0, i):
                distances_matrix.add_distance(self.address_list[i], self.address_list[j], distance_array[i][j])
                j = j + 1
            i = i + 1


