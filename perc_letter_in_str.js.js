 
// 2278. Percentage of Letter in String
// Example 1:

// Input: s = "foobar", letter = "o"
// Output: 33
// Explanation:
// The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.
// Example 2:

// Input: s = "jjjj", letter = "k"
// Output: 0
// Explanation:
// The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.


/**
 * @param {string} s
 * @param {character} letter
 * @return {number}
 */
var percentageLetter = function(s, letter) {

    let count=0;
    if(s.includes(letter)){
        for(let i=0;i<s.length;i++)
        {   
            if(letter == s[i])
                count++;
        }
        let perc = (count/s.length)*100;
        console.log("::perc",perc);

        return parseInt(perc);
    }
    else{
        return 0;
    }
    
};

console.log(percentageLetter("foobar",'o'))
// console.log(percentageLetter("jjjj",'o'))

console.log(percentageLetter("sgawtb",'s'))

