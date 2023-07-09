var floor = Math.floor(1.8);
var ceiling = Math.ceil( Math.PI );
var random = Math.random();
    
// console.log(floor);
// console.log(ceiling);
// console.log(random);

var lifesAnswers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
];

function randomAnswer(){
    // Generate a random value
    var random = Math.random()
    // Get a random value from 0 to the length of the array
    // console.log(random * lifesAnswers.length);
    number = random * lifesAnswers.length
    // Get the integer out of the number 
    // console.log(Math.floor(number));
    index = Math.floor(number)
    return lifesAnswers[index]
}

console.log(randomAnswer())