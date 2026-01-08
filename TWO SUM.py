class Solution:
    def twosum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    print("THE TWO VALUE INDICES ARE:")
                    return i, j
        return "No solution"


s = Solution()

print("-----TWO SUM-----")

nums = []


print("Enter the numbers:")
for i in range(5):
    nums.append(int(input()))
target = int(input("Enter the target: "))
result = s.twosum(nums, target)
print(result)

