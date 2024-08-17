// 5. Write a program which 2 strings from user and concat second string
// after first string. (Implement strcat() function).
// Input : “Marvellous Infosystems”
// “Logic Building”
// Output : “Marvellous Infosystems Logic Building”


function strcat(str1,str2)
{
    let lower ='';
    // for(var i=0; i<str.length; i++)
    // {
    //     if(str[i] == str[i].toLowerCase())
    //     {
    //         lower +=str[i]
    //     }
    // }
    return str1.concat(str2);

}
console.log(strcat('Marvellous Infosystems','Logic Building'))