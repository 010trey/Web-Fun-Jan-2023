
// function sayHi() {
//     console.log("Hi");
//     sayHi()
// }

// sayHi()

function repeatHello(n) {
    var result = ""
    for(var i=0;i<n;i++){
        result+= "Hello \n"
    }
    return result
}

// console.log(repeatHello(5))

function repeatHelloRecursive(n){
    //  break point = base case
    if(n<=1){
        return "Hello \n"
    }
    return "Hello \n" + repeatHelloRecursive(n-1)
}
console.log(repeatHelloRecursive(5));