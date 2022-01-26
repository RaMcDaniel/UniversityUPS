import csv


# The package file stores package information and the functions that extract it from the CSV
class Packages:
    def __init__(self):
        self.package_list = []

    # This method gets # of lines from CSV, and returns that to make the hashmap the right size.
    # CSV reader is imported from the standard library to read the files.
    # This can contribute to re-usability from day to day, since the hashmap can easily change sizes.
    def get_number_of_packages(self, packages_csv):
        counter = list(csv.reader(open(packages_csv)))
        package_count = len(counter)
        return package_count

    # This method uses CSV reader to read each line, which corresponds to information for one package.
    # index 0-7 correspond to the provided information. Truck_num, time_stamp and status are added for status tracking.
    def create_package_objects(self, packages_csv, hashmap):
        with open(packages_csv, "r") as csv_file:
            package_list = csv.reader(csv_file)

            # putting i in the first slot makes the numbers correspond with packages instead of starting at 0.
            for line in package_list:
                i = int(line[0])
                status = "at hub"
                time_stamp = "Pending"
                truck_num = None
                hashmap.put(i, [line[1], line[2], line[3], line[4], line[5], line[6], line[7], truck_num, time_stamp,
                                status])
