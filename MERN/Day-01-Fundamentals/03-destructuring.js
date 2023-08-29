
    const favoriteSinger = {
        firstName: "Michael",
        lastName: "Jackson",
        email:"m@j.com",
        bestSong:"Bellie Jean"
    }

    const hisLastName = favoriteSinger["lastName"]
    const hisFirstName = favoriteSinger.firstName
    // console.log(`His Full Name : ${hisFirstName} ${hisLastName} `);

    const {firstName, lastName} = favoriteSinger;
    // const firstName = favoriteSinger.firstName
    // const lastName = favoriteSinger.lastName
    const {firstName:coolName, lastName:y} = favoriteSinger;
    // const coolName = favoriteSinger.firstName
    // const y = favoriteSinger.lastName
    // console.log(`His Full Name with destructuring : ${coolName} ${y} `);

    const superHeros  = ["Superman", "SpiderMan", "Batman", "WonderWoman"]

    const  [,second,,forth] = superHeros

    console.log(second, forth);

    const person = {
        firstName: 'Bob',
        lastName: 'Marley',
        email: 'bob@marley.com',
        password: 'sekureP@ssw0rd9',
        username: 'barley',
        addresses: [
        {
            address: '1600 Pennsylvania Avenue',
            city: 'Washington, D.C.',
            zipcode: '20500',
        },
        {
            address: '221B Baker St.',
            city: 'London',
            zipcode: 'WC2N 5DU',
        }
        ],
        createdAt: 1543945177623
    };

    const {addresses:[,{city:homeTown}]} = person

    console.log("Your Home Town  is ", homeTown);