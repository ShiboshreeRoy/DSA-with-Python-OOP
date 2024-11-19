def fibonacci(n, memo={}):
    """
    Compute the nth Fibonacci number using memoization.

    Parameters:
        n (int): The position in the Fibonacci sequence to compute.
        memo (dict): A dictionary to store previously computed Fibonacci numbers (used for memoization).

    Returns:
        int: The nth Fibonacci number.
    """
    # If the value is already computed, return it from the memo dictionary.
    if n in memo:
        return memo[n]

    # Base case: The first two Fibonacci numbers are 1.
    if n <= 2:
        return 1

    # Otherwise, compute the Fibonacci number and store it in the memo dictionary.
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]
if __name__ == "__main__":
    # Compute the 10th Fibonacci number
    result = fibonacci(10)
    print(f"The 10th Fibonacci number is: {result}")
