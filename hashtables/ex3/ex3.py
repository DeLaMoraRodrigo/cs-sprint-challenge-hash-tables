def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # O(n^2)
    cache = dict()

    for arr in arrays:
        for num in arr:
            cache[num] = cache.get(num, 0) + 1
    result = [count[0] for count in cache.items() if count[1] == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
