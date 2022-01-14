# This file contains the classes involved in creating an adjacency matrix
# for distance information. Modeled from ZyBooks ch. 6.6.

class AddressVertex:
    def __init__(self, address):
        self.address = address


class AddressMatrix:
    def __init__(self):
        self.address_map = {}
        self.distance_between_addresses = {}

    def add_address(self, new_address):
        self.address_map[new_address] = []

    def add_distance_one_direction(self, address1, address2, distance=1):
        self.distance_between_addresses[(address1, address2)] = distance
        self.address_map[address1].append(address2)

    def add_distance(self, address1, address2, distance=1):
        self.add_distance_one_direction(address1, address2, distance)
        self.add_distance_one_direction(address2, address1, distance)


# slc = AddressMatrix()
# slc.add_address("123 street")
# slc.add_address("124 road")
# slc.add_address("934 ave")

# slc.add_distance("123 street", "124 road", 5)
# slc.add_distance("124 road", "934 ave", 7)
# slc.add_distance("123 street", "934 ave", 10)
# print(slc.address_map)
