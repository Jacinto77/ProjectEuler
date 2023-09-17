def sum_squares(num_start, num_end, step):
    sum_sqr = 0
    for num in range(num_start, num_end + 1, step):
        sum_sqr += num * num

    return sum_sqr


def square_sums(num_start, num_end, step):
    sqr_sums = 0
    for num in range(num_start, num_end + 1, step):
        sqr_sums += num

    return sqr_sums * sqr_sums


sum_sq = sum_squares(1, 10000, 1)
sq_sum = square_sums(1, 10000, 1)

print("Sum of squares:", sum_sq)
print("Square of sums:", sq_sum)
print("Difference = ", sq_sum - sum_sq)
