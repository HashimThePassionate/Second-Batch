
for(let step = 1; step <=5; step++)
{
    console.log("Walking east one step",step);
}

// 1 <= 5
// Walking east one step 1
// 2 <= 5
// Walking east one step 2
let i = 0;
do {
  i++;
  console.log(i);
} while (i == 5);

// // 

// let n = 0;
// let x = 0;
// while (n < 3) {
//   n++;
//   x += n;
//   console.log(x);
// }


// var myArray = [];
// var limit = parseInt(prompt("Enter Limit to repeat For loop"));
// for (let k = 0; k < limit;k++) {
//     var temp = parseInt(prompt("Enter Number"));
//     myArray.push(temp);
//     console.log(`Array Index ${k} = ${myArray[k]}`);
// }

// var tableNo = parseInt(prompt("Please Enter Table No"));
// var tableLimit = parseInt(prompt("Please Enter table limit "));
// for (let j = 1; j <= tableLimit; j++) {
//     let t = tableNo * j;
//   console.log(`${tableNo} * ${j} = ${t}`);
// }

// tableNo = 5
// tablelimit = 10
// j <= tableLimit  1 <= 10
// 5 * 1 = 5
// j <= tableLimit  2 <= 10
// 5 * 2 = 10

// var mr = Math.random() *10;
// var rn = Math.floor(mr);
// // console.log(mr);
// // console.log(rn);
// // console.log("Welcome to guess no game!");
// // console.log("Here is guess number game");
// var nooftries = 0;
// var playGuess;
// while(playGuess!==rn)
// {
//     playGuess = parseInt(prompt("Guess The Number :"));
//     nooftries++;
//     if(playGuess<rn)
//     {
//         console.log("You are to Low!");
//     }
//     else
//     {
//         console.log("You are two High!");
//     }
// }
// console.log(`Congratulation You guessed the number ${nooftries} tries`);



// var pass = "hashimtahir";
// var userpass;
// var  attempts = 0;
// do {
//     userpass = prompt("Please Enter your password");
//     attempts++;
//     if(userpass!==pass)
//     {
//         console.log("Incorrect Password Please try again!");
//     }
// } while (userpass!==pass);
// alert("Authentication successful it took you "+attempts+" attempts");

// a = ["Ahsan",20,"Junaid",1,2,3,4,5,6]
// theValue = "Junaid"
// for (let i = 0; i < a.length; i++) {
//     if (a[i] === theValue) {
//       continue;
//     }
//     console.log(a[i]);
//   }
  

// const arr = [3, 5, 7,8,10];
// arr.foo = "hello";
// arr.name = "Ahmed";
// for (const i in arr) {
//   console.log(i);
// }
// // "0" "1" "2" "foo"

// for (const i of arr) {
//   console.log(i);
// }

// const obj = 
//     {
//      foo: 1, 
//      bar: 2 
//     };

// for (const [k, v] of Object.entries(obj)) {
// console.log(k, v);
// }


// const array1 = ['a', 'b', 'c','d','e','f',12,2,3];

// array1.forEach((element) => console.log(element));



