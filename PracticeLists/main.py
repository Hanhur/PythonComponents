# 1
# def people_by_height(people, heights):
#     people_height = {}
#     for i in range(len(people)):
#         people_height[heights[i]] = people[i]
#
#     result = []
#     heights.sort(reverse = True)
#
#     for key in heights:
#         result.append(people_height[key])
#
#     return result
#
# people = ["Mary", "John", "Emma", "Din", "Jonathan"]
# heights = [180, 165, 170, 185, 175]
#
# print(people_by_height(people, heights))

# 2
def numIdenticalPairs(nums):
    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    return count

nums = [1, 2, 3, 1, 1, 3]
print(numIdenticalPairs(nums))
