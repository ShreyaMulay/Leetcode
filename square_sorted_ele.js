// 977. Squares of a Sorted Array
// Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

// Example 1:

// Input: nums = [-4,-1,0,3,10]
// Output: [0,1,9,16,100]
// Explanation: After squaring, the array becomes [16,1,0,9,100].
// After sorting, it becomes [0,1,9,16,100].
// Example 2:

// Input: nums = [-7,-3,2,3,11]
// Output: [4,9,9,49,121]


var sortedSquares = function(nums) {
    console.log("nums :",nums)
    let sorttedArr1=[]
    let sorttedArr=[]

    // for(let i=0;i<nums.length;i++)
    // {
    //     sorttedArr.push(nums[i]*nums[i])
    // }

    //sort array
    // for(let i=0;i<sorttedArr.length;i++)
    // {
    //     for(let j=0;j<sorttedArr.length;j++)
    //     {
    //          if(sorttedArr[i] < sorttedArr[j])
    //         {
    //             let s3 = sorttedArr[i];
    //             sorttedArr[i] = sorttedArr[j]
    //             sorttedArr[j] = s3
    //         }
    //     }

    // }


    let sortedArr = nums.map(num => num * num);

    sortedArr.sort((a, b) => a - b);

    return sortedArr;
    
    // return sorttedArr;
};


console.log(sortedSquares([-4,-1,0,3,10]))
console.log(sortedSquares([-7,-3,2,3,11]))