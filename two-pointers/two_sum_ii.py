def two_sum(numbers, target):
    """
    Returns 1-based indices of two numbers
    such that they add up to target.
    Assumes input array is sorted.
    """

    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []
