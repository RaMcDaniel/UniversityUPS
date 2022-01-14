# This file contains the classes involved in creating an adjacency matrix for distance information.

class AddressVertex:
    def __init__(self, address):
        self.address = address


class AddressMatrix:
    def __init__(self):
        self.address_map = {}

    def add_address(self, new_address):
        self.address_map[new_address] = []