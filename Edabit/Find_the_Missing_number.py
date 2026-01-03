# First Method

# def missing_num(lst):
#     for num in range(1, 11):
#         if num not in lst:
#             return num
# print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))

# second Method 

def missing_num(lst):
    return 55 - sum(lst)

print(missing_num([1, 2, 3, 4, 5, 7, 8, 9, 10]))