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

    def create_package_objects(self, packages_csv, individual_packages):
        with open(packages_csv, "r") as csv_file:
            package_list = csv.reader(csv_file)

# !!!REWORK!!!
# Don't put info directly into hashmap
# this function will create package objects.
# Create a package class and populate it
# This package class will need a timekeeping method
            for line in package_list:
                # i = int(line[0])
                status = "at hub"
                individual_packages.all_individual_packages.append(
                    [line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], status])
                # hashmap.put(i, [line[1], line[2], line[3], line[4], line[5], line[6], line[7]])


class Package:
    def __init__(self,):
        self.all_individual_packages = []
# will need to somehow add timekeeping to each object
# this class will represent 40 packages, will have 40 members
# add 2(?) parameters, definitely the hashmap it's going to, and then the 7 things from csv
# it needs a method to add each package object to
