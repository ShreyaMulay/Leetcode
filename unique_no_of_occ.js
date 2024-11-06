// 1207. Unique Number of Occurrences


// Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

// Example 1:

// Input: arr = [1,2,2,1,1,3]
// Output: true
// Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
// Example 2:

// Input: arr = [1,2]
// Output: false
// Example 3:

// Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
// Output: true


/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    
    let count ={}

    for(let i in arr)
    {
        count[arr[i]] = count[arr[i]] ? count[arr[i]] +1 :1
    }

    console.log("count",count)
   
    let values = Object.values(count)
    let uniqueA= values.filter((value,index) => values.indexOf(value) !== index)
    if(uniqueA.length == 0)
        return true
    else
        return false
};



console.log(uniqueOccurrences([1,2,2,1,1,3]))

console.log(uniqueOccurrences([1,2]))

console.log(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
