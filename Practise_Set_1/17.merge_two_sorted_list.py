def merge_sorted_lists(list1, list2):
    merged_list = sorted(list1 + list2)
    return merged_list


list_a = [1,3,5,7]
list_b = [2,4,6,8]
print(merge_sorted_lists(list_a,list_b))