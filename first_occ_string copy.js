// 28. Find the Index of the First Occurrence in a String

// Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

// Example 1:

// Input: haystack = "sadbutsad", needle = "sad"
// Output: 0
// Explanation: "sad" occurs at index 0 and 6.
// The first occurrence is at index 0, so we return 0.
// Example 2:

// Input: haystack = "leetcode", needle = "leeto"
// Output: -1
// Explanation: "leeto" did not occur in "leetcode", so we return -1.


/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    let output;
    if(haystack.includes(needle))
    {
        let index = haystack.indexOf(needle)
        console.log("The first occurrence is at index " + index + " ,so we return "+index);
        output = index;

    }
    else
    {
        console.log(needle + " did not occur in " + haystack +" ,so we return -1");
        output = -1;
    }

    return output;

};



strStr("sadbutsad","sad")
strStr("leetcode","leeto")

strStr("mississippi","issip")


