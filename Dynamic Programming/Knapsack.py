def knapsack(weights, values, capacity):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.

    Parameters:
        weights (list[int]): A list of weights of the items.
        values (list[int]): A list of values of the items.
        capacity (int): The maximum weight capacity of the knapsack.

    Returns:
        int: The maximum value that can be achieved within the given capacity.
    """
    n = len(weights)  # Number of items
    # Initialize a DP table with 0s. dp[i][w] represents the maximum value that can be obtained
    # using the first i items and a capacity of w.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):  # Loop over each item
        for w in range(1, capacity + 1):  # Loop over each possible weight capacity
            if weights[i - 1] <= w:  # If the item can fit in the current capacity
                # Either include the item or exclude it, and choose the better option
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # If the item can't fit, don't include it
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]  # The bottom-right cell contains the maximum value for the full capacity
if __name__ == "__main__":
    # Define item weights and values
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    # Find the maximum value that can be obtained within the given capacity
    result = knapsack(weights, values, capacity)
    print(f"The maximum value that can be obtained is: {result}")
