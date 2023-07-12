/**
 * Determines whether or not the strings are equal, ignoring case.
 * @param {string} strA
 * @param {string} strB
 * @returns {boolean} If the strings are equal or not.
 */

var strA1 = "ABC";
var strB1 = "abc";
var expected1 = true;

var strA2 = "ABC";
var strB2 = "abd";
var expected2 = false;

var strA3 = "ABC";
var strB3 = "bc";
var expected3 = false;

function caseInsensitiveStringCompare(strA, strB) {
    // compare strings
    if(strA. length != strB. length){
        // console.log(false)
        return false
    }else{
        strA = strA.toUpperCase()
        strA = strA.toUpperCase()
        for(var i = 0; i<strA.length; i++){
            if(strA[i]!=strB[i]){
                return false
            }
        }
    } 
} 
console.log(caseInsensitiveStringCompare(strA1, strB1))
console.log(caseInsensitiveStringCompare(strA2, strB2))
console.log(caseInsensitiveStringCompare(strA3, strB3))