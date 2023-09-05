"""A palindromic number reads the same both ways. The
largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 x 99

Find the largest palindrome made from the product of two
3-digit numbers."""


def reverse_string(string):
    temp = []
    for n in string:
        temp.insert(0, n)
        # print(temp)
    return "".join(temp)


def is_palindromic(in_num):
    """Takes in a number as a string, returns True if the num
    is a palindrome

    num is a string of integers"""
    if len(in_num) % 2 != 0:
        return False

    first = output_first_half(in_num)
    # print(first)

    sec_half = output_sec_half(in_num)
    second = reverse_string(sec_half)
    # print(second)

    if first == second:
        return True
    else:
        return False


def get_largest_palindrome(max_factor, min_factor, step):
    """returns a list including the factors and the product of the largest palindrome
    made by the product of two 3-digit numbers

    """
    palindromes = []
    out_results = []

    for num_i in range(max_factor, min_factor, step):
        for num_j in range(max_factor, min_factor, step):
            product = num_i * num_j
            print(num_i)
            print(num_j)
            print(product)
            if is_palindromic(str(product)):
                palindromes.append(str(product))
                out_results.append([num_i, num_j])

    return [out_results, palindromes]


def output_first_half(s):
    # print(s[:len(s) // 2])
    return s[:len(s) // 2]


def output_sec_half(s):
    # print(s[len(s) // 2:])
    return s[len(s) // 2:]


max_value = 999
stop_value = 100
step = -1
results = get_largest_palindrome(max_value, stop_value, step)


largest_palindrome = max(results[1])
print(largest_palindrome)

# for result in results[1]:
#     print("--------")
#     print(result)
#     #print(palindromes)
#     print("--------")
#
# print("factors: ", results[0], "\nproduct: ", results[1])



