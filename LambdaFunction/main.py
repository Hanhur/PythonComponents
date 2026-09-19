# numbers = ['1', '2', '3']
# print(list(map(int, numbers)))


# nums = [1, 2, 3, 4, 5, 6]
#
# nums = list(map(lambda x: x + 1, nums))
#
# for i in range(len(nums)):
#     nums[i] += 1
# print(nums)

# even_list = lambda lst: [x for x in lst if x % 2 == 0]
# print(even_list(nums))
# ----------------------------------------------------------------------
# strings = ["asffas", "ffhdgs", "dgsdgd", "asfbfdh"]
# strings_with_a = lambda lst: [string for string in strings if 'a' in string]
# print(strings_with_a(strings))
#  ---------------------------------------------------------------------
# nums = [1, 2, 3, 4, 8, 9, 10, 16, 25, 24]
# square_nums = lambda lst: [x for x in lst if int((x ** 0.5)) * (x ** 0.5) == x]
# print(square_nums(nums))
# ---------------------------------------------------------------------
# nums = [1, 2, 3, 5, 7, 5, 9, 15]
# higher_mean = lambda lst: [num for num in lst if num > sum(lst) / len(lst)]
# print(higher_mean(nums))
# ------------------------------------------------------------------------
names = ["Егор", "Маша", "Петя", "Ваня"]
heights = [185, 196, 178, 182]
data = list(zip(names, heights))
print(sorted(data, key = lambda x: x[1]))
# ------------------------------------------------------------------------
