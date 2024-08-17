// 125. Valid Palindrome

// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

// Given a string s, return true if it is a palindrome, or false otherwise.

 

// Example 1:

// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.
// Example 2:

// Input: s = "race a car"
// Output: false
// Explanation: "raceacar" is not a palindrome.
// Example 3:

// Input: s = " "
// Output: true
// Explanation: s is an empty string "" after removing non-alphanumeric characters.
// Since an empty string reads the same forward and backward, it is a palindrome.



/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let newAscii='';
    // for(let i=0;i<s.length;i++){
    //     let ascii = s[i].charCodeAt()
    //     if(ascii >= 65 && ascii <= 90  || ascii >= 97 && ascii <= 122)
    //     {
    //         let r = String.fromCharCode(ascii);
    //         newAscii +=r.toLowerCase()
    //     }
       
    // }
    const pattern = /[^a-zA-Z0-9\s]/g;
    newAscii = s.replace(pattern, '');
    newAscii = newAscii.replaceAll(" ", '');
    newAscii = newAscii.toLowerCase();
    console.log("::newAscii",newAscii)

    let reversedStr="";
     for (let i = newAscii.length - 1; i >= 0; i--) {
        reversedStr +=  newAscii[i];
    }


    console.log("::reversedStr",reversedStr)

    console.log("::reversedSt==r",reversedStr == newAscii)


    if(reversedStr === newAscii)
        return true
    else
        return false
};

console.log(isPalindrome("A man, a plan, a canal: Panama"))

console.log(isPalindrome("race a car"))


console.log(isPalindrome(" "))
console.log(isPalindrome("0P"))

