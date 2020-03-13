#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # go through the array
    for weight_i in range(length):
        # create a pair by retrieving from the tabel and subtracting limit
        pair = hash_table_retrieve(ht, limit - weights[weight_i])
        # if pair found return pair
        if pair is None:
            hash_table_insert(ht, weights[weight_i], weight_i)

    # if/n continue trying using insert
    else:
        return (weight_i, pair)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
