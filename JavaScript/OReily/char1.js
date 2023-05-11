console.log("Hello World!")

// object
let student = {
  name: "Karen", // property: value
  age: 30
};

console.log(`The student name is: ${student.name}, and age: ${student.age}`);

student.hometown = "São Bernardo do Campo";

console.log(`Student's hometown is: ${student.hometown}`);

student.niece = ["Amanda", "Gabi", "Vanessa", "Alice"]
console.log(student.niece)
console.log(`Older niece is: ${student.niece[2]}, the new niece is ${student.niece[3]}`);

student.niece[4] = {name: "Amanda", age: 20, mon: "Thais"}
console.log(
  `The ${student.niece[4].name} is ${student.niece[4].age} years old and her mon is ${student.niece[4].mon}`
);

function plus(x){
  return x + 1
}

// functions can be assigned to variables
let square = function (x) {
  return x * x
}

// classes
class Point {
  constructor (x,y){
    this.x = x;
    this.y = y;
  }

  distance(){
    return Math.sqrt(this.x * this.x + this.y * this.y)
  }
}

let newPoint = new Point();
console.log(`Novo ponto: ${newPoint.distance}`)


