// JavaScript Data Types
// 123 Integer / bigInt
// 12.5 Float / Double
// Muhammad Zubair123  String
// TRUE / False   Boolean
// null    / Empty 
// undefined    not defined / not declare
// Operator
//  Assignment Operator = 
// var age = 23
var Name = "Muhammad Ahmed"
var per = 88.5
var check = true
var z
var a = null

console.log("My age is:"+age);
console.log("My name is:",Name);
console.log(`My age is: ${Name}'s `);
console.log(per);
console.log(check);
console.log(z);
console.log(a);
// document.write(`<h2>My name is :${Name}</h2>`)
// alert("Hi")


// Arithmetic Operator +, - , * , /
var a = 10, b = 20
//  var a
//  var b
//  a = 10
//  b = 20
add =  a + b
console.log(`The addition of ${a} and ${b} = ${add}`);
console.log(`The Multiplication of ${a} and ${b} = ${a*b}`);

// Area of rectangle
var l = 5
var w = 3
console.log(`The Area of Rentangle is ${l*w}`);

// document.write(`<h1 style="background-color:salmon;color:blue;">The Area of rectangle is: ${l*w}</h1>`)

// Arithmetic Asssignment Operator
//  +=, -=, *= , /=
var num1 = 10
var num2 = 2
// num2 = num2 + num1
num2 += num1
// num1 = num1 + num2
num1 += num2
console.log(num2);
console.log(num1);

var a = 5 
var b = 10
b -= a
console.log(b);
a += b
console.log(a);

console.log(`a == b: ${a == b}`);
console.log(`a == b: ${2 === "2"}`);

// if statement
console.log("This is normal Statement");
var age = parseInt(prompt("Please enter your age"))
if(age>=18)
{
    console.log("You are Eligible for vote");
    console.log("If statement");
}
else {
    console.log("You are not eligible");
}
console.log("This is also normal statement")

