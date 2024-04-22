def maximum_value(max_weight, items):
    """
    Computes the maximum value achievable with a given maximum weight limit using dynamic programming.

    Args:
        max_weight (int): The maximum weight limit.
        items (list): A list of dictionaries representing items, where each dictionary has keys "weight" and "value".

    Returns:
        int: The maximum value achievable with the provided weight limit.
    """
    n = len(items)
    # Initialize a 2D array to store maximum values for different combinations of items and weight limits
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, max_weight + 1):
            # Decide whether to include or exclude the current item based on weight
            if items[i - 1]["weight"] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1]["weight"]] + items[i - 1]["value"])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][max_weight]
