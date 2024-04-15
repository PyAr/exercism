def maximum_value(maximum_weight, items):
    n = len(items)
    dp = [[0] * (maximum_weight + 1) for _ in range(n + 1)]  # Create a 2D array to store the maximum values

    for i in range(1, n + 1):
        for j in range(1, maximum_weight + 1):
            if items[i - 1]["weight"] <= j:  # If the weight of the current item is less than or equal to the current weight limit
                # Choose the maximum value between including the current item and excluding the current item
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1]["weight"]] + items[i - 1]["value"])
            else:
                # If the weight of the current item is greater than the current weight limit, exclude the item
                dp[i][j] = dp[i - 1][j]

    return dp[n][maximum_weight]  # Return the maximum value that can be achieved with the given weight limit