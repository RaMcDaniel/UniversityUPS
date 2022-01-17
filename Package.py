import csv

# The package file stores package information and the functions that extract it from the CSV


class Packages:
    def __init__(self):
        self.package_list = []

    # This method gets # of lines from CSV, and returns that to make the hashmap the right size.
    # This can contribute to re-usability from day to day, since the hashmap can easily change sizes.
    def get_number_of_packages(self, packages_csv):
        counter = list(csv.reader(open(packages_csv)))
        package_count = len(counter)
        return package_count
        # print(len(counter))

    # This method puts packages from csv into hashmap
    def create_package_objects(self, packages_csv, hashmap):
        with open(packages_csv, "r") as csv_file:
            package_list = csv.reader(csv_file)

            for line in package_list:
                i = int(line[0])
                status = "at hub"
                time_stamp = None
                truck_num = None
                hashmap.put(i, [line[1], line[2], line[3], line[4], line[5], line[6], line[7], truck_num, time_stamp, status])


