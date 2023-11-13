// Traditional Way
// let StudentName1 = "Ahmed"
// let StudentName2 = "Nadia"
// console.log(StudentName1,StudentName2);
// console.log(StudentName2);


//Array
// let shopping = ['Bread','Milk','Egg',"Noodles",'Cheese',10,30,10.23]
// console.log(shopping); 
// console.log(`My favourite item is: ${shopping[4]}`);
// shopping[4] = "Chocolate"
// console.log(`Now my favourite item is: ${shopping[4]}`);
// console.log(shopping);
// console.log(typeof(shopping)); 
// const random = ["tree", 795, [0, 1, "Ahmed"]];
// console.log(random[2][2]);
// console.log(`Length of Shopping Array is:${shopping.length}`);
const pet = ["Parrot", "Cat", "Owl","Rabbit"];
console.log(pet);
// console.log(pet.indexOf('Owl'));
// console.log(pet.indexOf('Donkey'),pet.indexOf('Cat'));
// console.log(pet.indexOf('Zebra'));
pet.push("Lion","Dolphin")
console.log(pet);
pet.unshift("Diansor","Chicken","Horse")
// console.log(pet);
// pet.pop()
// pet.pop()
// console.log(pet);
// pet.shift()
// pet.shift()
// console.log(pet);
// // let index = pet.indexOf("Cat")
//  let index = 1
//  if(index !== -1)
//  {
//     console.log("Show something");
//  }
// console.log(`Type is ${typeof(index)}`);
// // index = -1
// console.log(index);
// if (index !==-1) {
//     pet.splice(index,1)
// }
// console.log(pet);
// pet.splice("Cat",1)
// console.log(pet);
// console.log(a);

console.log(pet);
for(let p of pet)
{
    console.log(p);
}


let shop = [200,100,450,700,320]
for (let i of shop) {
    let sum = 0;
    sum += i//sum = sum + i 
    console.log(`Total ${i} Total Item ${sum}`);
}


const data = "Manchester,London,Liverpool,Birmingham,Leeds,Carlisle";
const cities = data.split(",");
console.log(cities,typeof(cities));
let newww = cities.toString()
console.log(newww,typeof(newww));
// const commaSeparated = cities.join("--");
// console.log(commaSeparated,typeof(commaSeparated));