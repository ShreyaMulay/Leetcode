// 819. Most Common Word

// Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

// The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

// Example 1:

// Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
// Output: "ball"
// Explanation: 
// "hit" occurs 3 times, but it is a banned word.
// "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
// Note that words in the paragraph are not case sensitive,
// that punctuation is ignored (even if adjacent to words, such as "ball,"), 
// and that "hit" isn't the answer even though it occurs more because it is banned.
// Example 2:

// Input: paragraph = "a.", banned = []
// Output: "a"


/**
 * @param {string} paragraph
 * @param {string[]} banned
 * @return {string}
 */
var mostCommonWord = function(paragraph, banned) {
    console.log("paragraph ",paragraph)
    // console.log("banned ",banned)

    let p1 = paragraph.toLowerCase().trim().split('');

    // let p1= paragraph.split('').filter(word =>{
    //     return word.trim();
    // })
    console.log(":p1 ", p1)

    let wordCount = {};

    for(let i=0;i<p1.length;i++)
    {   
        let cleanedWord= removeSpecialCharacters(p1[i]);

        console.log("cleanedWord ",cleanedWord)

        if(wordCount[cleanedWord])
        {
            wordCount[cleanedWord]++;
        }
        else
        {
            wordCount[cleanedWord] =1;
        }
    }
    console.log("wordCount ",wordCount)
    let max =0;
    let maxWord;
     for(let key in wordCount)
    {
        if(wordCount[key] > max && !banned.includes(key))
        {
            max = wordCount[key] ;
            maxWord = key;
        }
        
    }
    console.log(":maxWord  ", maxWord)

    return maxWord;



function removeSpecialCharacters(word) {
    let cleanedWord = '';
    for (let i = 0; i < word.length; i++) 
    {
        let char = word[i];
        console.log(char,"char")
        // if ((char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z'))
        if ((char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z') || (char >= '0' && char <= '9')) 
        {
            cleanedWord += char;
        }

    }
    return cleanedWord;
}

};

// console.log(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))

console.log(mostCommonWord("a, a, a, a, b,b,b,c, c",["a"]))
