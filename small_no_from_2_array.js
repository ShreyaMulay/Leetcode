// 2605. Form Smallest Number From Two Digit Arrays
// Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.
 

// Example 1:

// Input: nums1 = [4,1,3], nums2 = [5,7]
// Output: 15
// Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.
// Example 2:

// Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
// Output: 3
// Explanation: The number 3 contains the digit 3 which exists in both arrays.


var minNumber = function(nums1, nums2) {
    console.log("nums1 :"+nums1+" nums2 :"+nums2)

    let min1 = Math.min(...nums1)
    let min2 = Math.min(...nums2)

    console.log("min1",min1)
    console.log("min2",min2)

    // for(let i=0;i<nums1.length;i++)
    // {
    //     // if(nums1[i] == nums2[j])
    //     // {
    //     //     return nums1[i]
    //     // }
    //     if(nums2.includes(nums1[i])) 
    //     {
    //         break
    //         return nums1[i]; 
    //     }
    // }

    
   

    let m1= parseInt(min1.toString() + min2.toString())
    let m2 = parseInt(min2.toString() + min1.toString())

    console.log("1 : ",m1)
    console.log("2:",m2)
    if(m1 == m2)
        return min1

    let smallestCombinedNumber = Math.min(m1, m2);

    return smallestCombinedNumber;

};


// console.log(minNumber([4,1,3],[5,7]))
// console.log(minNumber([3,5,2,6],[3,1,7]))
// console.log(minNumber([3,8,4,2,6,1],[4,7,8,5,2,3,6]))
console.log(minNumber([6,4,3,7,2,1,8,5],[6,8,5,3,1,7,4,2]

))


