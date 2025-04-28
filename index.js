let task = "I eat rice"
let Firstname = ' Durodola '
let Number = 5;


let arry1 = ["Apple", "Banana", "Orange"]

console.log(arry1[0])
console.log(arry1[1])
console.log(arry1[2])

console.log(arry1)

console.log( typeof 5);

// Assignment operator

let var1 = "apple"

// comparison operator

// == === && ||
console.log('5' == 5);
console.log('5' === 5);
console.log('apple' && 0);
console.log(0 || -1);





// Arithmetic operator





// String Properties
console.log(Firstname.slice(0, 3))
console.log(Firstname.slice(0, -3))
console.log(Firstname.slice(3))
console.log(Firstname.slice(-3))
console.log(Firstname.indexOf('o'))
console.log(Firstname.lastIndexOf('o'))
console.log(Firstname.charAt(3))
console.log(Firstname.replace('D', 'T'))
console.log(Firstname.repeat(3))
console.log(Firstname.trim())
console.log(Firstname.trimStart())
console.log(Firstname.trimEnd())
console.log(Firstname.concat(' Ola'))
console.log(Firstname.concat(' Ola', ' Durodola'))
console.log(Firstname.concat(' Chris', ' Tomi', ' Praise', ' Aisha', ' Olamide', ' Roseline'))
console.log(task.replace ("rice", "spaghetti"))


// // Number Properties
// console.log(number.toString()); // convert number to string '5'
// console.log(number.toFixed(2)); // show 2 decimal places
// console.log(number.toPrecision(1)); // show 1 digit
// console.log(number.toExponential(2)); // show in exponential notation with 2 decimal places 5.00e+0
// console.log(number.valueOf());



console.log(task.replace('Rice', 'Spaghetti'))

function replaceString() {
   let str = document.getElementById("inputBox1").value;
   let n = str.toUpperCase();
   document
}

function replaceUpperCase() {
    // Get the text from the first input box
    const inputText = document.getElementById('inputBox1').value;

    // Replace lowercase 'rice' with uppercase 'RICE'
    const replacedText = inputText.toUpperCase();

    // Display the replaced text in the second input box
    document.getElementById('inputBox2').value = uppercaseText;
}


function multiplyvalue() {
    // Get values from the input boxes
  let firtsvalue = document.getElementById("inputBox1").value;
  let firstvalue =  document.getElementById('inputBox2').value;

  let result = parseFloat(firstvalue) * parseFloat(secondValue)

  if (!isNaN(result)) {
    document.getElementById('inputBox1').textContent = "Result: " + result;
  }
}

function Thanks() {
    // Set the "Thank you" text in the input box
    const inputText = document.getElementById('inputBox1').value;

    const replacedText = inputText.replace("Done", "Thank you for a job well done")

    document.getElementById('inputBox1').value = replacedText
}

let gender = "tomi";

if (gender == "female"){
  console.log("Welcome ma'am")
}else if (gender == "male"){
  console.log("Welcome sir")
} else {
  console.log("Welcome")
}


if(0){
  console.log("This won't run");
}else{
  console.log("This will run");
  
}

//Loops
//for loops
for(let i = 0; i < 5; i++){
  console.log(i);
}

// //while loop
// let i = 0
// while(a < 5){
//   console.log(i);
//   i++;
// }

//do while loop
let j = 0
do{
  console.log(j);
  j++;
}while(j < 5)

let day = 3

switch(day){
  case 1: console.log("Monday");
  break
  case 2:
    console.log("Tuesday")
  break
  case 3:
    console.log("Wednesday")
  break
  case 4:
    console.log("Thursday");
  break
  case 5:
  console.log("Friday")
  break
  case 6:
    console.log("Saturday");
  break
  case 7:
    console.log("Sunday"); 
  default:
    console.log("invalid day");
}


// 1 step
function functionName(parameter) {
  //code of block
}

// 2 step
let functionName = function (parameter) {
  // code of block
}

// 3 step
let functionName = (parameter) => {
  // code of block
}

//function declaration
function greet(){
  console.log("hello")
}
greet(); // Prints " hello"

//Arrow function
let greet = () => {
  console.log("hello");
}
greet(); //Print "hello"

// conditional statement
function greet(name) {
  if (name){
    console.log('Hello ' + name);
  } else {
    console.log('Hello guest');
  }
}
greet('Aisha') //Prints "hello"