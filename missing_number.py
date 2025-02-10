def find_missing_formula(lst):
    n = max(lst)  
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

lst = [1, 2, 3, 5, 6, 7, 9, 8]
print(find_missing_formula(lst))  # Output: 4









