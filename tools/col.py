def myzip(it1, it2):
    # Find the length of the shortest iterable
    min_length = min(len(it1), len(it2))

    # Create tuples by zipping corresponding elements
    result = tuple((it1[i], it2[i]) for i in range(min_length))

    return result


