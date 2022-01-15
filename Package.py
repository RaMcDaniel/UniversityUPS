import csv

# The package file stores package information and the functions that extract it from the CSV


class Packages:
    def __init__(self):
        self.package_list = []

    def get_number_of_packages(self, packages_csv):
        # Read CSV file as list to get number of packages
        counter = list(csv.reader(open(packages_csv)))
        package_count = len(counter)
        return package_count
        # print(len(counter))

    def put_packages_in_hashmap(self, packages_csv, hashmap):
        with open(packages_csv, "r") as csv_file:
            package_list = csv.reader(csv_file)

            for line in package_list:
                i = int(line[0])
                hashmap.put(i, [line[1], line[2], line[3], line[4], line[5], line[6], line[7]])
                # hashmap.get(i) # This statement tests contents of packages
