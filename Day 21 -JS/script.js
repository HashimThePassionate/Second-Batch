document.write("<h2 style='background-color:salmon; color:white; text-align:center;font-size:40px'>Welcome to JS Objects</h2>")
var Name = "Ahmed"
    x = {
        "welcome":"Welcome to Objects in JS",
        2:25,
        Name,
        "Ahmed Raheem":"My Name!",
        ishaq:23,
        walk:(x) => ` I Walked in ${x} miles`
    }
    var y = {}
    y.age = 23
    y.Name = "Ishaq"
// -------------------------
// for in 
for (const key in x) {
 console.log(`${key} = ${x[key]}`);
//  console.log(`${key} = ${y[key]}`);
}

console.log(y);
console.log("Running......");
console.log(x);
console.log(x["welcome"]);
console.log(x[2]);
console.log(x["Ahmed Raheem"]);
console.log(x.walk(15));


const myHonda = {
    color: "red",
    wheels: 4,
    engine: { "cylinder s": 4, size: 2.2 },
  };
console.log(myHonda.engine["cylinder s"]);

// Constructor Functions
function Car(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
  }


var audi = new Car("AUDI","A7",2018)
var tesla = new Car("Tesla","ModelX",2020)
console.log(audi);
console.log(audi.year);
console.log(tesla);
console.log(typeof(tesla));
console.log(typeof(myHonda));

