    // ctrl+/
    // COMMENT 

    /*
    Multi Line
    comment 
    */

    var i ;
    i = 10;
    // ! NAMING CONVENSION camelCaseConvension
    var firstName = "   JOHN         "
    var lastName = "James"
    
    // - VARIABLES
    
    // 1  String
    var firstName = "JOHN"
    var lastName = "James"
    
    // 2 Number 
    var age  = 41
    var bmi = 2.5
    
    // Boolean
    var hasCovid = false
    var isFunny = true
    
    // Null vs Undefined vs not defined
    
    var favFood
    var favArtist = null
    // console.log(favArtist);
    // console.log(favFood);
    // console.log(favColor);
    favFood = "🍕"
    // console.log(`User first name is ${firstName}, last name is ${lastName} 🎈🎈🎈`);
    
    // More strings
    // console.log(firstName.length)
    // console.log(lastName.toUpperCase());
    // console.log(lastName[2]);
    // firstName.trim("JO")
    // console.log(firstName);
    // firstName = firstName.trim();
    // console.log(firstName);
    
    // Conditionals :  IF/ELSE
    
    // if (hasCovid) {
    //     console.log("Go Home");
    // } else {
    //     console.log("You are WELCOME");
    // }
    var i = 1
    if (i === "1"){
        console.log("YES");
    } else {
        console.log("NO");
    }
    // i = 1 Assigning 
    // i == 1 checking the value
    // i === 1  checking the value & the type
    
    // if(firstName =="JOHN") {
    //     if (favFood == "🍕") {
    //         console.log("Hey");
    //     }else{
    //         console.log("Go Home");
    //     }
    // }
    var john =  [lastName,firstName, age, isFunny,hasCovid]
    console.log(john);
    user = {
        'firstName':firstName,'lastName':lastName, 'age':age
    }
    console.log(user);