// 283. Move Zeroes
// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

// Note that you must do this in-place without making a copy of the array.

 

// Example 1:

// Input: nums = [0,1,0,3,12]
// Output: [1,3,12,0,0]
// Example 2:

// Input: nums = [0]
// Output: [0]


/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    // console.log("nums",nums)
    let count=0
    for(let i=0;i<nums.length;i++)
    {
        if(nums[i]==0)
        {
            count +=1;
            nums.splice(i,1);
            i--
        }
    }
    console.log("count",count)
    console.log("nums aft",nums)
    for(let i=0;i<count;i++)
    {
        nums.push(0)
    }

    // console.log("nums end",nums)
    return nums;
};

console.log(moveZeroes([0,1,0,3,12]))
console.log(moveZeroes([0]))
console.log(moveZeroes([0,0,1]))

