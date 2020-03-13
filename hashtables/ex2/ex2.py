#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # go through tiks and insert the src and dest, into ha-tbl.
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

        current_location = "NONE"

    # we need to find the origin -> loop thru 
    for i in range(length):
    # find current location by retrieval of None in source, Start route
        route[i] = hash_table_retrieve(hashtable, current_location)
        current_location = route[i]
    # pop the last item in  arr to replace"NONE" with route arr
    route.pop()
    #return route
    return route