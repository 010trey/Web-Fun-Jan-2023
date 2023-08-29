
// console.log(dog);
// console.log(x);

// sayHi()
//  var  => let or const 
let dog = "max"
var  user = {username :"John", age:41}
console.log(`Hi ${dog}`);

function sayHi() {
    console.log("Hi There");
}

// - How Interpreter/Browser works 
// 1 - Create namespaces : objects for js files 
// 2 - Hoisting : variables and functions
// 3 -  Interpolation and Calculations
// 4 - Convert everything to string
// 5 - run it 

// ! JIT : Just In Time compilation

var needle = 'haystack';
test();
console.log(needle,"***********");
function test(){
    var needle = 'magnet';
    console.log(needle);
}

// var needle 

// function test(){
//     var needle
//     needle = "magnet"
//     console.log(needle);
// }
// needle = "haystack"
// test()