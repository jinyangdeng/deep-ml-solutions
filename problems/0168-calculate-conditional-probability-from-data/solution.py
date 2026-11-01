def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    # Your code here
    numer = len([e for e in data if e == (x, y)])
    denom = len([e for e in data if e[0] == x])
    return numer / denom if denom != 0 else 0
