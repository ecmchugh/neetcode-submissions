class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const m = new Map();
        for (let i = 0; i < nums.length; i++) {
            let difference = target - nums[i];
            if (m.has(difference)) {
                return [m.get(difference), i];
            } else { 
                m.set(nums[i], i);
            }
        }
    }
}
