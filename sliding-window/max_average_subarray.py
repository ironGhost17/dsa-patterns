def find_max_average(nums, k):
    """
    Returns the maximum average of any contiguous subarray of size k.
    """

    # Initial window sum
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k
