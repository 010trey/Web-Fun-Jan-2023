    /* 
    Given a string,
    return a new string with the duplicates excluded

    Bonus: Keep only the last instance of each character.
    */

    const str1 = "abcABC";
    const expected1 = "abcABC";

    const str2 = "helloo";
    const expected2 = "helo";

    const str3 = "";
    const expected3 = "";

    const str4 = "aa";
    const expected4 = "a";

    function stringDedupe(str) {}
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
    Given an array of strings
    return the number of times each string occurs (a frequency / hash table)
    */

    const arr1 = ["a", "a", "a"];
    const expected1 = {
    a: 3,
    };

    const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
    const expected2 = {
    a: 2,
    b: 1,
    c: 3,
    B: 1,
    d: 1,
    };

    const arr3 = [];
    const expected3 = {};

    function makeFrequencyTable(arr) {}
