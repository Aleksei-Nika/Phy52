// Number
// String
// Boolean true/false
// null
// undefined

// Object: array, function, object

// let age = 20;
// let name = 'Sasha';
// let isStudent = true;
// console.log(`Name: ${name}, age: ${age}, `);

// let testVar;
// console.log(`Значение testVar: ${testVar}`);
// console.log(typeof testVar);

// let car = null;
// console.log(`Значение car: ${car}`);
// console.log(typeof car);

// console.log(null == undefined);
// console.log(null === undefined);

// console.log(5 == '5');
// console.log(5 === '5');
// pi = 3;

// console.log(y);
// var y = 10;
// console.log(y)

// // инкремент ++ --
// let a = 10;
// let b = 5;

// console.log(a / 3);
// console.log(a ** b);
// a ++;
// let hasMoney = true;

// console.log('5' + 2);
// console.log('5' - 2);
// console.log('five' * 2);

// alert('Hello');

// // document.write();

// prompt(`5`);

// let userName = prompt('как вас зовут?');
// if (userName !== null) {
//     console.log(`привет, ${userName}`);
// }

// let tet = confirm('администратор?');
// console.log(`доступ: ${tet}`);

// console.log((tet) ? '!' : '-');

// let color = prompt('color?');
// switch (color) {
//     case 'green':
//         console.log('go');
//         break;
//     case 'red':
//         console.log('stop');
//         break;
//     default:
//         console.log('warning');
// }

// let i = 0;
// while (i < 3) {
//     i ++;
//     console.log(i)
// }

// for (let iter = 0; iter < 3; iter++) {
//     console.log(iter);
// }

// let ret = 3;
// do {
//     ret--;
//     console.log(ret);
// }
// while (ret !== 0);

// for (let i = 1; i <= 100; i++) {
//     if (i%3 === 0 && i%5 === 0) {
//         console.log('FizzBuzz');
//     } else if (i % 3 === 0) {
//         console.log('Fizz');
//     } else if (i % 5 === 0) {
//         console.log('Buzz');
//     } else {
//         console.log(i);
//     }
// }

let str = 'abcdefg';
// console.log(str.length);
// console.log(str.toUpperCase());
// console.log(str.includes('def'));
// console.log(str.slice(5,6));

let str2 = '              apple, orange,    kiwi         ';
// console.log(str2.trim());
// console.log(str2.split(','));

for (let i = 0; i < str.length; i++) {
    console.log(str[i]);
}


let nums = [6, 3, 6, 1, 3, 7];

nums.push(10);

// nums.forEach(num => console.log(num ** 2));

// let rere = nums.map(num => num ** 2);
// rere.forEach(num => console.log(num));

let evens = nums.filter(num => num % 2 === 0);
console.log(evens);

function sayHello(name) {
    return `Hello, ${name}`;
}

let massege = sayHello('ret');
alert(massege);

const multiply = function(a, b) {
    return a * b;
}

console.log(multiply(5, 5));

const sqare = (n) => {
    return n * n;
}

const sqare2 = n => n ** 2;

console.log(sqare2(3));