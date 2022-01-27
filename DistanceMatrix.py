# This file contains the classes involved in creating an adjacency matrix.
# The adjacency matrix holds all the addresses and their distances from one another.
# for distance information. Modeled from ZyBooks ch. 6.6.

class AddressMatrix:
    def __init__(self):
        # The address_map holds individual addresses.
        self.address_map = {}
        # This dictionary has each set of two addresses as a key, with the distance between them as the value.
        self.distance_between_addresses = {}

    # B3.23 Space complexity: O(1)
    # One dictionary entry is created regardless of package number.
    # B3.23 Time Complexity: O(1)
    # Dictionary manipulation requires no search.
    # This populates the address_map dictionary.
    def add_address(self, new_address):
        self.address_map[new_address] = []

    # B3.24 Space complexity: O(1)
    # One dictionary entry is created regardless of package number.
    # B3.24 Time Complexity: O(1)
    # Dictionary manipulation requires no search.
    # This method takes two addresses as arguments and inerts them as key, with the distance between them as value.
    def add_distance_one_direction(self, address1, address2, distance=1):
        self.distance_between_addresses[(address1, address2)] = distance
        self.address_map[address1].append(address2)

    # B3.25 Space complexity: O(1)
    # One dictionary entry is created regardless of package number.
    # B3.25 Time Complexity: O(1)
    # Dictionary manipulation requires no search.
    # This method saves times by allowing address1 and address2, and vice versa, which should have identical values,
    # to be inserted at the same time. It just calls add_distance_one_direction twice.
    def add_distance(self, address1, address2, distance=1):
        self.add_distance_one_direction(address1, address2, distance)
        self.add_distance_one_direction(address2, address1, distance)
