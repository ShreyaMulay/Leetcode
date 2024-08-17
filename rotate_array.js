// 189. Rotate Array

// Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

// Example 1:

// Input: nums = [1,2,3,4,5,6,7], k = 3
// Output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]
// Example 2:

// Input: nums = [-1,-100,3,99], k = 2
// Output: [3,99,-1,-100]
// Explanation: 
// rotate 1 steps to the right: [99,-1,-100,3]
// rotate 2 steps to the right: [3,99,-1,-100]


/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    // console.log("nums :",nums)

    // console.log("k :",k)

    if(k <= 0)
    {
        return
    }
    
    let arrlength = nums.length;
    let lastele = nums[arrlength - 1];

    console.log("lastele :",lastele)

    for(let i = arrlength-1 ;i > 0; i--)
    {
        nums[i] = nums[i - 1];

    }   
    nums[0] = lastele;

    // console.log("aft nums :  :"+nums)     
    
    rotate(nums,k-1) 

    return nums;  
    
};