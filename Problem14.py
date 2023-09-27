def even_cal(n):
    return n // 2


def odd_cal(n):
    return 3 * n + 1


nums = {}
longest_chain = []
longest_chain_num = 0
for i in range(1, 1000000, 1):
    chain = [i]
    current_num = i
    next_num = 0

    while current_num != 1:
        if current_num % 2 == 0:
            next_num = even_cal(current_num)
        else:
            next_num = odd_cal(current_num)

        chain.append(next_num)
        current_num = next_num

    if len(chain) > len(longest_chain):
        longest_chain_num = i
        longest_chain = chain

    print(i, ": ", chain)
    nums[i] = chain

# for key, val, in nums.items():
#     print(key, len(val), val)

print(longest_chain_num, ":", len(longest_chain), ":", longest_chain)
