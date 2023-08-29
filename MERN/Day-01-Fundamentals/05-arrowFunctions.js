
// console.log(pow(5));

// ! Hoisting 
// ! Globally scoped

// * Named function 
// function pow(e){
//     console.log(this);
//     return e**3
// }

// * Named Function with hoisting solution
const myFunction = function pow(e) {
    return e**3
}
// console.log(pow(3));

// * Anonymous Function with hoisting solution
const myFunctionAnonymous = function(e) {
    console.log("This Anonymous = ", this);
    return e**3
}
// console.log(myFunctionAnonymous(52));

// * Arrow Function with hoisting solution
const myFunctionArrow = (e) => {
    console.log("This Arrow = ", this);
    return e**3 // Explicit  return 
}

const myFunctionArrowOneLine = e => e**3 // Implicit  return 

console.log(myFunctionArrowOneLine(9));


