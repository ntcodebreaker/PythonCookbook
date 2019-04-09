
arr = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9], 
    [10, 11, 12]
    ]

inv = [[r[col] for r in arr] for col in range(len(arr[0]))]

print(arr)

print(inv)