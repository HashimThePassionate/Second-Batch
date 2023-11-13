//  Regular Function VS Anonymous Function
// Regular Function
// z(2)
// var z = function square(square) {
//     console.log(`The Square is ${square*square}`);
// }
// square(6)
// function square(square) {
//     console.log(`The Square is ${square*square}`);
// }
// console.log()
// z(3)
// square(2)
// square(1)
// square(3)
// square(4)
// square(5)
// z(10)
// j()
// var j = function()
// {
//     console.log("This is Anonymous Function");
// }
// j()
// IIFE
// (function(){console.log(10+20);})(); 

// Arrow Function
// let arrow = () => { console.log("I am an Arrow Function"); }
// arrow()
// let x = (a,b) => a+b
// let res = x(1,2);
// console.log( x(10,20));
// console.log(res);

// var condition = null

// if(condition)
// {
//     // Statements
// }
// else 
// {
//     // Statements
// }
// // ---------------------------------------------------------------------------------------
// if(condition)
// {
//     // Statement
// }
// else if(condition)
// {
//     // statements
// }
// // ...
// else 
// {
//     // Statemenst
// }


function evenOdd(x)
{
    if(x%2 == 0)
    {
        console.log(`${x} is Even Number`);
    }
    else
    {
        console.log(`${x} is Odd Number`);
    }
}
evenOdd(22)
evenOdd(23)

let x = function evenOdd(x)
{
    if(x%2 == 0)
    {
        console.log(`${x} is Even Number`);
    }
    else
    {
        console.log(`${x} is Odd Number`);
    }
}

x(10)


let z = function (x)
{
    if(x%2 == 0)
    {
        console.log(`${x} is Even Number`);
    }
    else
    {
        console.log(`${x} is Odd Number`);
    }
}
z(100)


let eo = (x) =>  t = x%2==0? `${x} is Even`:`${x} is Odd`;
console.log(eo(13));
