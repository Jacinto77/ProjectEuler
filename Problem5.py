""" is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from
1 to 20?"""


def get_least_common_multiple(num_a, num_b):
    multiple = 1
    while True:
        mult_a = num_a * multiple
        mult_b = num_b * multiple

        # print("multiple: ", multiple, "num_A: ",  mult_a)
        # print("multiple: ", multiple, "num_B: ",  mult_b)

        if mult_a % num_b == 0:
            print(mult_a)
            result = mult_a
            break

        if mult_b % num_a == 0:
            print(mult_b)
            result = mult_b
            break

        multiple += 1

    print("The least common multiple of: ", num_a, "and", num_b,
          "is ", result)

    return result


newest_lcm = 2
lcms = []
for i in range(20, 2, -1):
    newest_lcm = get_least_common_multiple(i, newest_lcm)

print(newest_lcm)

# testing result
for i in range(20, 2, -1):
    if newest_lcm % i != 0:
        print("WRONG")
        break
    else:
        print("good for now")
