// const user = {
//     name: 'Алексей',
//     age: 27,
//     isAdmin: true
// }
// console.log(user.name);

// user.citi = 'Novosibirsk';

// console.log(user);

// const cat = {
//     name: 'Luna',
//     sayMeow: fanction() {
//         console.log('Meow');
//     }
// }

// cat.sayMeow()

// const employees = [
//     {name: "Иван", role: "admin", pin: "1234", attempts: 0},
//     {name: "Илья", role: "manadger", pin: "6666", attempts: 0},
//     {name: "Петр", role: "worker", pin: "0000", attempts: 0},
// ]

// let loginHistory = [];

// function authenticate() {
//     let pinInput = prompt(`Введите ваш PIN (exit для выхода)`);
//     if (pinInput === 'exit' || pinInput === null) return 'exit';
//     let foundUser = employees.find(user => user.pin === pinInput);
//     if (foundUser) {
//         if (foundUser.attempts >= 3) {
//             alert(`Аккаунт ${foundUser.name} заблокирован`);
//             return null;
//         }
//         else{
//             foundUser.attempts = 0;
//             return foundUser;
//         }
//     } else {
//         employees.forEach(emp => emp.attempts++);
//         alert(`Неверный PIN`);
//         return null;
//     }
// }



// function grantAccess(user) {
//     let massege;
//     if (!user) return;
//     switch (user.role) {
//         case 'admin':
//             massege = 'Полный доступ к серверной и сейфу';
//             break;
//         case 'manadger':
//             massege = 'Доступ к офисам и архиву';
//             break;
//         case 'worker':
//             massege = 'Полный доступ к серверной и сейфу';
//             break;
//         default:
//             massege = 'Доступ только в общий зал';
//     }
//     alert(`${user.name}, приветствуем! ${massege}`);
//     if (!loginHistory.includes(user.name)) {
//         loginHistory.push(user.name);
//     }
// }

// while (true) {
//     let result = authenticate()
//     if (result === 'exit') break;

//     if (result) {
//         grantAccess(result);
//     }
// }

// console.log(`Сотрудников посетившие офис: ${loginHistory.join(', ')}`);

// window - (laert, prompt, comfig)