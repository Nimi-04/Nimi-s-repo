function multiply() {
    
    let number1 = document.getElementById('number1').value;
    let operator = document.getElementById('operator').value;
    let number2 = document.getElementById('number2').value;

    let num1 = Number(number1);
    let num2 = Number(number2);
    let result = document.getElementById('display')
    result.innerHTML = "";

    for (let i = 0; i <= num2; i++) {
        let ans = `${num1} X ${i}= ${num1 * i} <br>`;
        result.innerHTML += ans;
    }

switch (operator) {
    case '+': 
        result.innerHTML = `${num1} + ${num2} = ${num1 + num2}`;
        break;

    case '-': 
        result.innerHTML = `${num1} - ${num2} = ${num1 - num2}`;
        break;

    case 'x': 
        result.innerHTML = `${num1} * ${num2} = ${num1 * num2}`;
        break;

    case '/': 
        if (num2 !== 0) {
            result.innerHTML = `${num1} / ${num2} = ${num1 / num2}`;
        } else {
            result.innerHTML = "Division by zero is undefined.";
        }
        break;

    case '%': // Percentage
        result.innerHTML = `${num1} % of ${num2} = ${(num1 / 100) * num2}`;
        break;  

    case 'log':
        if (num1 > 0 && num2 > 0) {
            result.innerHTML = `Log base ${num2} of ${num1} = ${Math.log(num1) / Math.log(num2)}`;
        } else {
            result.innerHTML = "Logarithm inputs must be positive numbers.";
        }
        break;

    default:
        result.innerHTML = "Invalid operator";
  }
}