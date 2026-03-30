const money = 80;
const time = 5;
const day = 5;
const totalTime = 40;
const totalDay = 9;

const dayWork = totalTime / day;
const yesOrNot = dayWork <= totalDay;

console.log(`Успеем ${yesOrNot}`)

const totalMoney = totalTime * money;
console.log(`Стоимость = ${totalMoney}$`)