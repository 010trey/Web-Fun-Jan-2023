// Data Types : Primitive :  Passed by value
// Strings  :  "Alex"
// Numbers  : 2 , 1.25
// Boolean   : true , false
// undefined / null

// -------------------------

// Complex Data Types  : Data Structures : Passed by reference
// Arrays 
// Objects

var animals = ["🐻", "🦁"]

// var objectUser = {"Key": "value"}
var objectUser = {}
// console.log(objectUser);

// Bracket Notation
objectUser["firstName"] = "John"

// Dot Notation
objectUser.lastName = "Smith"
objectUser.age = 41
objectUser.favAnimals = animals
objectUser.isFunny = false
objectUser.favSinger = {"firstName":"Mac", "lastName":"Miller"}

// objectUser.userInfo = function showInfo(){
//     console.log("User First Name : ", objectUser.firstName);
//     console.log(objectUser.lastName);
//     console.log(objectUser.age);
// }

objectUser.userInfo = function (){
    console.log("This is this : " , this);
    // console.log("User First Name : ", this.firstName);
    // console.log(this.lastName);
    // console.log(this.age);
}
objectUser.userInfo()
// console.log(objectUser.favSinger.firstName)