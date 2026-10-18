def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    samples.sort()
    N = len(samples)
    result = []
    counter = 0
    for idx, num in enumerate(samples):
        counter += 1
        if idx == N - 1 or samples[idx + 1] != samples[idx]:
            result.append((num, counter / N))
            counter = 0

    return result