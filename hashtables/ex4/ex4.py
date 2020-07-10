def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # O(n)
    cache = dict()
    result = list()

    for i in range(len(a)):
        cache[a[i]] = True
        if a[i] != 0 and -a[i] in cache:
            result.append(abs(a[i]))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
