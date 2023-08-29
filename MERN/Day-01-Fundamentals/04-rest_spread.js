    const a  = [10,20,3]
    const b = a
    const c = [...a]
    // 
    a.push(2000)
    b.push(9000)
    // console.log("a == ",a);//? a == [10,20,3,2000]
    // console.log("b == ",b);//? b == [10,20,3,9000]

    c.push(7000)
    console.log("a == ",a);//? a == [10,20,3,2000]
    console.log("b == ",b);//? b == [10,20,3,9000]
    console.log("c == ",c);//? b == [10,20,3,9000]

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

    const person2  = {...person, updatedAt: 123456789}
    const person3  = {...person, createdAt: 111111111}

    console.log(person, person2);