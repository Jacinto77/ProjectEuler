import random
"""If we list all the natural numbers below 10
 that are multiples of 3 or 5 , we get 3, 5, 6, and 9 .
 The sum of these multiples is 23

Find the sum of all the multiples of
3 or 5 below 1000."""


def sum_of_multiples(max):
    """Finds the sum of all numbers from 0-max that are a multiple of 3 or 5

    max defines the range of numbers to check for multiples of 3 or 5
    """

    list_nums = []
    for i in range(max):
        if i % 3 == 0 or i % 5 == 0:
            list_nums.append(i)
            # print(i)

    res = 0
    for i in list_nums:
        res += i

    return res


iterations = random.randint(0, 1000000)


print(sum_of_multiples(1000))
