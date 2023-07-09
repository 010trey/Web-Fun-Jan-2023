var arr = ["a", "b", "c", "d", "e"];

function reverse(array) {
    // Code Goes Here
    var newArray = []
    for(var i = array.length-1;i>-1;i--){
        // console.log(array[i]);
        newArray.push(array[i])
    }
    return newArray
}

// Invoke the function
console.log("REVERSE ONE ", reverse(arr))


function reverse2 (array){
    for(var i=0;i<= array.length/2 ;i++) {
        var temp = array[i]
        array[i] = array[array.length -1 - i]
        array[array.length -1 - i] = temp
    }
    return array
}
console.log("REVERSE TWO ",reverse2(arr))