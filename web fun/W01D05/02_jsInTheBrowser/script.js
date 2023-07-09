function sayHello(){
    console.log('Hello from HTML')
}

function changeButton(element){
    console.log(element.innerHTML);
    if(element.innerHTML == "ON"){
        element.innerHTML = "OFF"
        element.style.backgroundColor = "red"
    } else {
        element.innerHTML = "ON"
        element.style.backgroundColor = "green"
    }
}