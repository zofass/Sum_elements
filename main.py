def calculate_sum(numbers):
    if len(numbers) == 0:
        return 0

    sum_cause = sum(numbers[::2])
    last_element = numbers[-1]
    result = sum_cause * last_element
    return result

numbers_1 = [0, 1, 7, 2, 4, 8]
numbers_2 = [1, 3, 5]
numbers_3 = [6]
numbers_4 = []

print(calculate_sum(numbers_1))
print(calculate_sum(numbers_2))
print(calculate_sum(numbers_3))
print(calculate_sum(numbers_4))