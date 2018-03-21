def sum_numbers(numbers=None):
    if numbers:
        return sum(numbers)
    else:
        return sum(range(1,101))

sum_numbers(10)