def sum_list_elements(my_list):
    total = 0
    for i in range(len(my_list)):
        total += my_list[i]
    return total


sample_list = [1, 2, 3, 4, 5]

# Expected output: Sum of elements = 15
print("Sum of elements =", sum_list_elements(sample_list[:-1]))
