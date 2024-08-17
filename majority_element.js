// 169. Majority Element

// Given an array nums of size n, return the majority element.

// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

// Example 1:

// Input: nums = [3,2,3]
// Output: 3
// Example 2:

// Input: nums = [2,2,1,1,1,2,2]
// Output: 2


/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let elementCount = {};
    for(let i=0;i<nums.length;i++)
    {
        if(elementCount[nums[i]])
        {
            elementCount[nums[i]] +=1
        }
        else
        {
            elementCount[nums[i]] = 1
        }
    }

    let max = 0
    let maxEle;
    for(let key in elementCount)
    {
        if(elementCount[key] > max)
        {
            maxEle = key;
            max = elementCount[key]
        }
    }

    console.log("::maxElement",maxEle);
    return maxEle;


};


console.log(majorityElement([3,2,3]))
console.log(majorityElement([2,2,1,1,1,2,2]))
