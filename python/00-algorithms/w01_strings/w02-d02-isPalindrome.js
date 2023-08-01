    /* 
    String: Is Palindrome

    Create a function that returns a boolean whether the string is a strict palindrome. 
        - palindrome = string that is same forwards and backwards
    
    Do not ignore spaces, punctuation and capitalization
    */

    const str1 = "a x a";
    const expected1 = true;
    
    const str2 = "racecar";
    const expected2 = true;
    
    const str3 = "Dud";
    const expected3 = false;
    
    const str4 = "oho!";
    const expected4 = false;
    
    function isPalindrome(str) {}






















function isPalindrome(str = "") {
for (let i = 0; i < Math.floor(str.length / 2); i++) {
    // Looping inwards from both sides.
    if (str[i] !== str[str.length - 1 - i]) {
    return false; // early exit
    }
}
return true;
}
console.log(isPalindrome(str1));
console.log(isPalindrome(str2));
console.log(isPalindrome(str3));
console.log(isPalindrome(str4));
// const functionIsPalindrome = (str = "") =>
// str === str.split("").reverse().join("");


