# def unique(lst):
#     index0= 0
#     index1= 1
#     for i in range(len(lst)):
#         if i[index0] != i[index1] :
#             return i
#         index0 += 1
#         index1 += 1

def unique(lst):
    for num in lst:
        if lst.count(num) == 1:
            return num
        
print(unique([3, 3, 3, 3, 11, 3]))