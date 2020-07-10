# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # O(len(files) + (len(queries) * len(cache[query])))
    cache = dict()
    result = list()

    for file in files:
        split_file = file.split("/")
        filename = split_file[-1]
        
        if filename not in cache:
            cache[filename] = list()
        cache[filename].append(file)

    for query in queries:
        if query in cache:
            for i in cache[query]:
                result.append(i)

    return result


if __name__ == "__main__":
    # files = [
    #     '/bin/foo',
    #     '/bin/bar',
    #     '/usr/bin/baz'
    # ]
    # queries = [
    #     "foo",
    #     "qux",
    #     "baz"
    # ]
    files = []

    for i in range(500000):
        files.append(f"/dir{i}/file{i}")

    for i in range(500000):
        files.append(f"/dir{i}/dirb{i}/file{i}")

    queries = []

    for i in range(1000000):
        queries.append(f"nofile{i}")

    queries += [
        "file3490",
        "file256",
        "file999999",
        "file8192"
    ]
    print(finder(files, queries))
