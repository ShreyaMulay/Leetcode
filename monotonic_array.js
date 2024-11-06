// 896. Monotonic Array

// An array is monotonic if it is either monotone increasing or monotone decreasing.

// An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

// Given an integer array nums, return true if the given array is monotonic, or false otherwise.


// Example 1:

// Input: nums = [1,2,2,3]
// Output: true
// Example 2:

// Input: nums = [6,5,4,4]
// Output: true
// Example 3:

// Input: nums = [1,3,2]
// Output: false


/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMonotonic = function(nums) {
    
    console.log("nums",nums)

    let asc= [...nums]

    let desc= [...nums]


    let ascsort = asc.sort((a,b)=>a-b)

    let descscsort = desc.sort((a,b)=>b-a)

    if(JSON.stringify(nums) == JSON.stringify(ascsort) || JSON.stringify(nums) == JSON.stringify(descscsort))
    {
        return true
    }
    else{
        return false

    }

};

isMonotonic([1,2,2,3])

console.log("456",isMonotonic([6,5,4,4]))

isMonotonic([1,3,2])
