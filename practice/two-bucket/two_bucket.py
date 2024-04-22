""""
Water Bucket Problem - Measure the minimum number of moves required to achieve a specific goal volume of water using two buckets of different sizes.

Approach:
1. Initialize the buckets with their maximum capacities and current volumes.
2. Fill the specified start bucket to begin the process.
3. Check if the goal is already achieved. If yes, return the result.
4. Explore all possible moves by pouring, emptying, or filling the buckets, considering the constraints and avoiding redundant states.
5. Perform depth-first search (DFS) to find the minimum moves required to reach the goal.
6. Utilize a recursive approach to explore all possible move sequences, keeping track of visited states to avoid cycles.
7. Return the minimum move required to reach the goal.

Args:
    bucket_one (int): The maximum capacity of the first bucket.
    bucket_two (int): The maximum capacity of the second bucket.
    goal (int): The desired volume of water to measure.
    start_bucket (str): The bucket to start with, either "one" or "two".

Returns:
    tuple: A tuple containing the minimum number of moves required to achieve the goal and the corresponding bucket status upon reaching the goal.

Raises:
    ValueError: If the start_bucket is neither "one" nor "two".

Example:
    >>> measure(5, 7, 3, "one")
    (1, "one", 0)
"""

import copy

def measure(bucket_one, bucket_two, goal, start_bucket):
    """
    Measure the minimum number of moves required to achieve a specific goal volume of water.

    Args:
        bucket_one (int): The maximum capacity of the first bucket.
        bucket_two (int): The maximum capacity of the second bucket.
        goal (int): The desired volume of water to measure.
        start_bucket (str): The bucket to start with, either "one" or "two".

    Returns:
        tuple: A tuple containing the minimum number of moves required to achieve the goal and the corresponding bucket status upon reaching the goal.

    Raises:
        ValueError: If the start_bucket is neither "one" nor "two".
    """
    buckets = [{"max": bucket_one, "cur": 0}, {"max": bucket_two, "cur": 0}]
    fill(buckets, 0 if start_bucket == "one" else 1)

    result = is_done(buckets, goal)
    if result:
        return (1, *result)

    moves = []
    for i in range(6):
        _r = move(i, buckets, goal, start_bucket, 1, [buckets])
        if _r:
            moves.append(_r)

    return min(moves)

def is_done(buckets, goal):
    """Check if the goal is achieved."""
    if buckets[0]["cur"] == goal:
        return ("one", buckets[1]["cur"])
    if buckets[1]["cur"] == goal:
        return ("two", buckets[0]["cur"])
    return False

def move(index, buckets, goal, start_bucket, count, history):
    """Perform a move and explore subsequent moves recursively."""
    _buckets = copy.deepcopy(buckets)

    if index == 0:
        pour(_buckets, 0, 1)  # Pour from bucket one to bucket two
    elif index == 1:
        pour(_buckets, 1, 0)  # Pour from bucket two to bucket one
    elif index == 2:
        empty(_buckets, 0)     # Empty bucket one
    elif index == 3:
        empty(_buckets, 1)     # Empty bucket two
    elif index == 4:
        fill(_buckets, 0)      # Fill bucket one
    elif index == 5:
        fill(_buckets, 1)      # Fill bucket two

    if _buckets[0]["cur"] + _buckets[1]["cur"] == 0:
        return False

    first_bucket = 0 if start_bucket == "one" else 1
    second_bucket = 1 if start_bucket == "one" else 0

    if is_empty(_buckets, first_bucket) and is_full(_buckets, second_bucket):
        return False
    if _buckets in history:
        return False

    result = is_done(_buckets, goal)
    if result:
        return (count+1, *result)

    moves = []
    for i in range(6):
        if i == index:
            continue
        _r = move(i, _buckets, goal, start_bucket, count+1, [*history, _buckets])
        if _r:
            moves.append(_r)

    if moves:
        return min(moves)

def is_empty(buckets, which_bucket):
    """Check if a bucket is empty."""
    return buckets[which_bucket]["cur"] == 0

def is_full(buckets, which_bucket):
    """Check if a bucket is full."""
    return buckets[which_bucket]["cur"] == buckets[which_bucket]["max"]

def pour(buckets, from_bucket, to_bucket):
    """Pour water from one bucket to another."""
    left = buckets[to_bucket]["max"] - buckets[to_bucket]["cur"]
    if buckets[from_bucket]["cur"] > left:
        fill(buckets, to_bucket)
        buckets[from_bucket]["cur"] -= left
    else:
        buckets[to_bucket]["cur"] += buckets[from_bucket]["cur"]
        empty(buckets, from_bucket)

def empty(buckets, which_bucket):
    """Empty a bucket."""
    buckets[which_bucket]["cur"] = 0

def fill(buckets, which_bucket):
    """Fill a bucket."""
    buckets[which_bucket]["cur"] = buckets[which_bucket]["max"]
