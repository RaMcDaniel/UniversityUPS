import csv


# The Address file stores address information and the functions that obtain it from the CSV.


class Addresses:
    def __init__(self):
        self.address = ""

    def put_addresses_in_city_map_matrix(self, address_csv, address_matrix):
        with open(address_csv, "r") as csv_file:
            distances_csv = csv.reader(csv_file)

            # next skips the header row in csv file to get to first row of data.
            next(distances_csv)
            for line in distances_csv:
                address_matrix.add_address(line[0])

        # This tests that addresses were added to hashmap correctly
        # print(address_matrix.address_map)
