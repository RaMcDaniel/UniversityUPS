# This file will create a truck class and load packages.

#    i.     Prioritization Algorithm
# 1. Create an algorithm that will look at the package data ONLY (no distances)
# and will figure out which package goes on which truck.
# (OPTION 2.1)
#   a.This typically means creating a list that stores the package ids associated with each truck
# i.     Later, you can use the hash table.lookup(package id) method to access that package associated
# with each package id.
# ii.     The hash table should be a primary table for the latest information about the packages.
# iii.     Do not duplicate the package objects outside of the hash table. This will lead to synchronization
# issues later on.


# You want to end this with 3 loaded truck objects
# truck objects are loaded with package objects from elsewhere
