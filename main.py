def selection_sort(list_items):
    for i in range(len(list_items)):
        min_value = list_items[i]
        old_pos = 0
        for j in range(1,len(list_items)):
            if list_items[j] < min_value:
                min_value = list_items[j]
                old_pos = j
        temp =  list_items[i]
        list_items[i] = list_items[old_pos]
        list_items[old_pos] = temp
    return list_items

if __name__ == '__main__':
    print(selection_sort([33, 1, 89, 2, 67, 245]))