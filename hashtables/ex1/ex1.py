#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """ 
# * What if we store each weight in the input list as keys? What would be a useful thing to store as the value for each key? 
# * If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for `limit - weight`. 
#   If it does, then we've found the two items whose weights sum up to the `limit`!
    """
    # insert in hash table
    # store each weight in the input list as keys
    for i in range(length):
            hash_table_insert(ht, weights[i], i)
    answer = None
    for i in range(length):
        # When we check if the difference in limit and weight is in the hash table, 
        # we should also make sure the hash table doesn't return the same number we are looking at.
        if (hash_table_retrieve(ht, limit - weights[i]) and hash_table_retrieve(ht, limit - weights[i]) != i):
            hash_index = hash_table_retrieve(ht, limit - weights[i])
            if hash_index > i:
                answer = (hash_index, i)
            else:
                answer = (i, hash_index)
    return answer



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
