def find_max_min_brute_force(arr):
    """Brute Force
        we only count the number of comparisons of array elements
    """
    if not arr:
        return None, None, 0

    max_val = arr[0]
    min_val = arr[0]
    comparisons = 0

    for i in range(1, len(arr)):
        comparisons += 1
        if arr[i] > max_val:
            max_val = arr[i]

        comparisons += 1
        if arr[i] < min_val:
            min_val = arr[i]

    return max_val, min_val, comparisons


def find_max_min_dac(arr):
    """Divide and Conquer: return max, min, number_of_comparisons
        we only count the number of comparisons of array elements
    """

    def dac(low, high):
        if low == high:
            return arr[low], arr[low], 0

        if high == low + 1:
            comparisons = 1  
            if arr[low] > arr[high]:
                return arr[low], arr[high], comparisons
            else:
                return arr[high], arr[low], comparisons

        mid = (low + high) // 2

        left_max, left_min, left_comp = dac(low, mid)
        right_max, right_min, right_comp = dac(mid + 1, high)

        comparisons = left_comp + right_comp
        comparisons += 1  
        overall_max = left_max if left_max >= right_max else right_max

        comparisons += 1  
        overall_min = left_min if left_min <= right_min else right_min

        return overall_max, overall_min, comparisons

    return dac(0, len(arr) - 1)


if __name__ == "__main__":
    # arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, -10, 25]
    arr = [7, 3, 8, 2, 9, 1, 6, 4, 5, 10, -5, 12]

    print(f"Array with ({len(arr)} elements): {arr}\n")

    # bruteforce
    max1, min1, comp1 = find_max_min_brute_force(arr)
    print("bruteforce:")
    print(f"   Max = {max1}")
    print(f"   Min  = {min1}")
    print(f"   Comparsions = {comp1}\n")

    # Divide and Conquer
    max2, min2, comp2 = find_max_min_dac(arr)
    print("Divide and Conquer:")
    print(f"   Max = {max2}")
    print(f"   Min  = {min2}")
    print(f"   Comparsions = {comp2}")

    print(f"\nEfficiency: DAC uses {(comp1 - comp2)/comp1*100:.1f}% fewer comparisons")
