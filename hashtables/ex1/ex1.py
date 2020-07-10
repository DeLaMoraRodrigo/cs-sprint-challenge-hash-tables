def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # O(length + 2) - O(2(length))
    cache = dict()

    for i in range(length):
        cache[weights[i]] = i
    for i in range(length):
        supl = limit - weights[i]
        if supl in cache:
            return (cache[supl], weights.index(weights[i]))

    return None
