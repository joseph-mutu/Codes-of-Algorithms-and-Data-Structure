import collections
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if not nums:
            return False
        duplicate = collections.defaultdict(list)
        for idx,num in enumerate(nums):
            if num in duplicate:
                if idx - duplicate[num][-1] <= k:
                    return True
            duplicate[num].append(idx)
        return False

s = Solution()
print(s.containsNearbyDuplicate([1,0,1,1],1))

