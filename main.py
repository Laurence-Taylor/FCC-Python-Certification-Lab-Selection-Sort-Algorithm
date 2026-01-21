def selection_sort(list_items):
    #First Recursive 
    for i in range(len(list_items)):
        # Settin min Value
        min_value = list_items[i]
        # Setting found position (Old position)
        old_pos = -1
        # Second Recursive to find the next min value
        for j in range(i,len(list_items)):
            # If next value is less than min value
            if list_items[j] < min_value:
                # Change Values
                min_value = list_items[j]
                # Set old_pos
                old_pos = j
        # if found a new min_value
        if old_pos != -1:
            # Swaping new Minimum value 
            temp =  list_items[i]
            list_items[i] = list_items[old_pos]
            list_items[old_pos] = temp
    # Return Ordered_List
    return list_items

if __name__ == '__main__':
    print(selection_sort([33, 1, 89, 2, 67, 245]))