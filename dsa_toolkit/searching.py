def linear_search(items, target):
    """Return first matching index or -1. Time O(n), extra space O(1)."""
    for i, value in enumerate(items):
        if value == target: return i
    return -1

def binary_search(items, target):
    """Search ascending-sorted items. Time O(log n), extra space O(1)."""
    low, high = 0, len(items)-1
    while low <= high:
        mid = (low+high)//2
        if items[mid] == target: return mid
        if items[mid] < target: low = mid+1
        else: high = mid-1
    return -1
