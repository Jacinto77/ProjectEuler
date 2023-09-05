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


def get_lcm_range(rng):
    pass



# first_num = 10
# sec_num = 24
#
# lcm = []
# for i in range(10, 2, -1):
#     lcm.append(get_least_common_multiple(i, i - 1))
#
# print(lcm)
#
# new_lcm = []
# counter = 2
# for i in lcm:
#     new_lcm.append(get_least_common_multiple(i, counter))
#     counter += 1
#
# print(new_lcm)
#
#
# for i in range(10, 1, -1):
#     print(2520 / i)
#
# for i in range(10, 1, -1):
#     print(get_least_common_multiple(2520 / i, i))

newest_lcm = 2
lcms = []
for i in range(20, 2, -1):
    newest_lcm = get_least_common_multiple(i, newest_lcm)

print(newest_lcm)

for i in range(20, 2, -1):
    if newest_lcm % i != 0:
        print("WRONG")
        break
    else:
        print("good for now")
