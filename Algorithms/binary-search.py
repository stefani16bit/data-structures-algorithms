def binary_search():

    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

    target = 23 

    start = 0
    end = len(list) - 1

    while start <= end:
        middle = (start + end) // 2

        if list[middle] > target:
            end = middle -1

        elif list[middle] < target:
            start = middle +1

        else:
            return middle
        
    return None
                
print(binary_search())
        

    