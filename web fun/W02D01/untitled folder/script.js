function deleteElement(id) {
    // console.log("Element to remove = ",document.getElementById(id) );
    document.getElementById(id).remove()
    // document.querySelector(`#${id}`).remove()
    console.log("Element Removed ✅✅ ID = ", id);
}

// // function like(id){
// //     console.log("Like ♥", document.getElementById(id).innerText);
// //     var like = parseInt(document.getElementById(id).innerText);
//     // like ++;
// //     console.log("Like ♥", like);
// //     document.getElementById(id).innerText = like;
// // }

function likeTwo(e){
    // console.log(e);
    e.innerText++
}

// // function onImage(e) {
// //     console.log(e.src);
// //     if(e.src == 'http://127.0.0.1:5502/images/1.jpg'){
// //        e.src = './images/5.png'
// //     }    
// //     else{
// //        e.src = './images/1.jpg'
// //     }
// // }

function onMouseImage(id){
    document.getElementById(id).src = './images/6.png'
}

function outMouseImage(id) {
    document.getElementById(id).src = './images/2.jpg'
}

// function login() {
//     setTimeout(enterName, 3000)
// }

// // login()
// function raiseAlert(){
//     alert('Please try To Register')
// }
// function enterName() {
//     var name = prompt('Put Your name')
//     var age = prompt('Put Your age')
//     console.log(name, age);
// }
// // function message() {
// //     console.log("Delayed message");    
// // }
    
// // console.log("Start"); //1
// // setTimeout(message, 5000);//5
// // console.log("End");//1
// // //5 

// function showInput(e) {
//     console.log(e.value);
// }