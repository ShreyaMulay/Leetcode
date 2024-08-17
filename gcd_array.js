// Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

// The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 

// Example 1:

// Input: nums = [2,5,6,9,10]
// Output: 2
// Explanation:
// The smallest number in nums is 2.
// The largest number in nums is 10.
// The greatest common divisor of 2 and 10 is 2.
// Example 2:

// Input: nums = [7,5,6,8,3]
// Output: 1
// Explanation:
// The smallest number in nums is 3.
// The largest number in nums is 8.
// The greatest common divisor of 3 and 8 is 1.
// Example 3:

// Input: nums = [3,3]
// Output: 3
// Explanation:
// The smallest number in nums is 3.
// The largest number in nums is 3.
// The greatest common divisor of 3 and 3 is 3.



/**
 * @param {number[]} nums
 * @return {number}
 */
var findGCD = function(nums) {
    console.log("nums",nums)  
    let max= nums[0]
    let min= nums[0]
    for(let i=0;i<nums.length;i++)
    {
      if(nums[i]>max)
      {
          max = nums[i]
      }
      if(nums[i]<min)
      {
          min = nums[i]
      }
  
    }
    console.log("max",max)  
    console.log("min",min)  
  
    while(max !=0)
    {
      let temp = max;
      max = min % max;
      min = temp
    }
     return min
  
  };


console.log(findGCD([2,5,6,9,10]))
console.log(findGCD([7,5,6,8,3]))
console.log(findGCD([3,3]))





let a= {a:1,b:3,c:3}
let b= 'b'

for(let k in a)
    {
        if((a[k] != null || a[k] != undefined ) && b == k)
        {
            console.log("lkj",a[k]);
        }
    }