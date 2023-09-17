import math
import timeit
import time

number = """7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"""


def get_largest_adj(lst):
    highest_val = 0
    prod_and_adj = []
    for i in lst:
        prod = get_adjacent_product(i)
        print(i, prod)
        if prod > highest_val:
            prod_and_adj.clear()
            highest_val = prod
            prod_and_adj = [prod, i]

    return prod_and_adj


def get_adjacent_product(lst):
    nums = []
    for i in lst:
        if i == 0:
            return 0
        nums.append(int(i))

    return math.prod(nums)


def get_adjacent_values(num, amount):
    print(len(num))
    adjacents = []
    temp_lst = []
    i = 0
    while i < len(num) - amount + 1:
        adjacents.append(num[i: i + amount])
        i += 1

    return adjacents


def remove_newlines(input_string):
    res = []
    for sub in input_string:
        if sub == "\n":
            continue
        else:
            res.append(sub)

    return str(res)


timeit.timeit()
start_time = time.localtime().tm_sec
number_parsed = int(number)


lst_of_adjacent = get_adjacent_values(number, 13)

print(lst_of_adjacent)
largest_adjacents = get_largest_adj(lst_of_adjacent)
print(largest_adjacents)

end_time = time.localtime().tm_sec

print(end_time - start_time)

