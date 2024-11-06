// 557. Reverse Words in a String III


// Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

// Example 1:

// Input: s = "Let's take LeetCode contest"
// Output: "s'teL ekat edoCteeL tsetnoc"
// Example 2:

// Input: s = "Mr Ding"
// Output: "rM gniD"


/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {

    let arr= s.trim().split(" ")
    let a=[]
    for(let i=0;i<arr.length;i++)
    {
        a.push(reverseword(arr[i]))
    }   

    

    function reverseword(str)
    {
        return str.split('').reverse().join('')
    }

    return a.join(' ')
    
};

console.log(reverseWords("Let's take LeetCode contest")