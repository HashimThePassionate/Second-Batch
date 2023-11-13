// Ternary Operator
// var age = 18
// var a = parseInt(prompt("Please Enter Your Age!"))
// var res = (a >= age)? "Congratulations You are Eligible for Vote" : "Sorry you are not eligible for vote" 
// console.log(res); 

// if else if condition , last condition else
// var grade = parseInt(prompt("Please Enter your grade in Integers"))
// // 91  (91>=90 && 91<=100) 
// if(grade>=90 && grade <=100) 
// {
//     console.log("Your grade is A+")
// }
// else if(grade>=80 && grade<90)
// {
//     console.log("Your grade is A")
// }
// else if(grade>=70 && grade<80)
// {
//     console.log("Your grade is B")
// }
// else if(grade>=60 && grade<70)
// {
//     console.log("Your grade is C")
// }
// else if(grade>=50 && grade<60)
// {
//     console.log("Your grade is Pass")
// }
// else if(grade>=0 && grade<50)
// {
//     console.log("You are Fail!")
// }
// else {
//     console.log("Invalid");
// }

// Nested if Statement
// var num1 = 10, num2 = 130, num3 = 50
// if(num3>num1)
// {
//     if(num3>num2)
//     {
//         console.log(`${num3} is greater than ${num2}  and ${num1} `);
//     }
//     else {
//         console.log(`${num3} is greater than ${num1} but not ${num2} `);
//     }
// }
// else{
//     console.log(`${num3} is neither greater than ${num2}  nor  ${num1} `);
// }


// Switch Statement
var vowels = prompt("Please Enter a letter!")
switch (vowels) {
    case 'a' :
    case 'A' :
    console.log(`${vowels} is vowel`);
    break;
    case 'e' :
    case 'E' :
    console.log(`${vowels} is vowel`);
    break;
    case 'i':
    case 'I':
    console.log(`${vowels} is vowel`);
    break;
    case 'o':
    case 'O':
    console.log(`${vowels} is vowel`);
    break;
    case 'u':
    case 'U':
    console.log(`${vowels} is vowel`);
    break;
    default:
    console.log("Letters is consonants!");
}