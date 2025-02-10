def check_sorted(lst):
    if lst == sorted(lst):
        return "Ascending"
    elif lst == sorted(lst, reverse=True):
        return "Descending"
    else:
        return "Not Sorted"


lst1 = [1, 2, 3, 4, 5]
lst2 = [5, 4, 3, 2, 1]
lst3 = [1, 3, 2, 4, 5]

print(check_sorted(lst1)) 
print(check_sorted(lst2))  
print(check_sorted(lst3))  



