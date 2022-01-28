import csv


# The Address file stores address information and the functions that obtain it from the CSV. (Lusby, 2022)
class Addresses:
    def __init__(self):
        # This list is useful in other methods
        self.address_list = []

    # This uses CSV reader to read just the addresses, and put them in the adjacency matrix.
    def put_addresses_in_city_map_matrix(self, address_csv, address_matrix):
        with open(address_csv, "r") as csv_file:
            distances_csv = csv.reader(csv_file)

            # next skips the header row in csv file to get to first row of data.
            # line[0] is the address in the addresses CSV, and this is added to first the adjacency matrix,
            # and then to the address_list.
            # .lstrip() removes extra spaces to avoid dictionary mismatches later.
            next(distances_csv)
            for line in distances_csv:
                address_matrix.add_address(line[0].lstrip())
                self.address_list.append(line[0].lstrip())

    # a separate distances CSV was created, address_csv_plain, that only kept the plain distance numbers, no addresses.
    # CSV reader loops takes each line and moves it to an array.
    # This array will next be added to the adjacency matrix, lines up with matching addresses.
    def put_distances_in_array(self, address_csv_plain):
        distance_array = []
        with open(address_csv_plain, "r") as csv_file:
            distances_csv_plain = csv.reader(csv_file)

            for line in distances_csv_plain:
                distance_array.append(line)
        return distance_array

    # This loop takes the address list above, and lines it up with the matching distances from the above distance_array.
    # This allows the individual entries to be added to the city_map_matrix object in main.
    def put_distances_in_city_map_matrix(self, distance_array, distances_matrix):

        for i in range(0, 27):
            for j in range(0, i):
                distances_matrix.add_distance(self.address_list[i], self.address_list[j], distance_array[i][j])
