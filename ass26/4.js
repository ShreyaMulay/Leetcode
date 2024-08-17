// 4. Write a program which accept string from user and copy small
// characters of that string into another string.
// Input : “Marvellous multi OS”
// Output : “arvellous multi”
// void StrCpySmall(char *src, char *dest)


function StrCpySmall(str)
{
    console.log("str : ",str);
    let lower ='';
    for(var i=0; i<str.length; i++)
    {
        if(str[i] == str[i].toLowerCase())
        {
            lower +=str[i]
        }
    }
    return lower;

}
console.log(StrCpySmall('Marvellous multi OS'))