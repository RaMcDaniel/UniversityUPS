# This is where the main nearest neighbor implementation goes.
# the 3 individual trucks go through this algorithm separately

# 1.      Loop through the packages assigned to the truck (since the order was determined by the algorithm above)
# a.      For each package, have the truck figure out what the next best address is to go to (shortest distance)
# i.     Nearest neighbor algorithm works well for this and will come in under 140 miles

# 2.      Deliver the package by timestamping it in the hash table.
# a.      NOTE: Don’t be afraid to add an additional timestamp field within the package class.
# 3.      Keep track of the distance traveled starting from the hub
# 4.      Display total round-trip distance once all packages have been delivered.
# a.      This needs to include the distance back to the hub when the truck is finished
