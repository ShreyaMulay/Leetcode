// 3. Write a program which accept string from user and copy capital
// characters of that string into another string.
// Input : “Marvellous Multi OS”
// Output : “MMOS”



function StrCpyCap(str)
{
    console.log("str : ",str);
    let upper ='';
    for(var i=0; i<str.length; i++)
    {
        if(str[i] == str[i].toUpperCase())
        {
            upper +=str[i]
        }
    }
    // upper = upper.replaceAll(' ','')
    return upper;

}
console.log(StrCpyCap('Marvellous Multi OS'))