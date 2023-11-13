// console.log("JavaScript Functions");
// function display()
// {
//     console.log("This is my Simple Display function!");
// }

// console.log("Normal Statement!");
// display()

// var a = 10, b = 2 
// console.log(`The Sum is ${a+b}`);
// console.log("Something");
// var c = 2, d = 30
// console.log(`The Sum is ${c+d}`);

// Functions
// function sum(num1,num2,num3,num4,num5) 
// {
//     // return (num1+num2+num3+num4+num5)
//     let res = num1+num2+num3+num4+num5
//     console.log(`The sum is :${res}`);
//     const a = 10
//     // console.log(a);
//     // console.log(a);
//     // console.log(a);
//     // console.log(a);
//     // console.log(a);
//     a = 20 
//     console.log(a);
// }
// sum(1,2,3,4,5)
// console.log(res);
// console.log(res);
function evenOdd(a)
{
    if (a%2 == 0)
    {
        console.log(`${a} is Even`);
        document.write(`<h4> ${a} is Even</h4>`)
    }
    else
    {
        console.log(`${a} is Odd`);
        document.write(`<h4> ${a} is Odd</h4>`)
    }
}
var a = parseInt(prompt("Enter a Number! "))
evenOdd(a)