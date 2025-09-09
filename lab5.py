# 1. Reverse a given list
print("Task 1: Reverse a list")
lst1 = [1, 2, 3, 4, 5]
print("Original list:", lst1)
print("Reversed list:", lst1[::-1])
print()

# 2. Sort a list of numbers by descending absolute value
print("Task 2: Sort list by absolute value (descending)")
def list_sort(lst):
    return sorted(lst, key=abs, reverse=True)

lst2 = [3, -7, 2, -9, 5, -1]
print("Original list:", lst2)
print("Sorted list:", list_sort(lst2))
print()

# 3. Swap first and last elements of a list
print("Task 3: Swap first and last elements")
def change(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

lst3 = [10, 20, 30, 40, 50]
print("Original list:", [10, 20, 30, 40, 50])
print("Changed list:", change(lst3))
