class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        lists = [];
        j = 0;
        length = len(nums);
        for i in range(length):
            residual = target - nums[i];
            j = i;
            while j < length - 1:
                j += 1;
                if (residual == nums[j]):
                    lists.append(i);
                    lists.append(j);
                    return (lists);
