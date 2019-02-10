let list = [1,2,3,4,5,6,7,8,9,10];

function evenNumber(number) {
    return (number%2 === 0); 
};

function getEvenNumber(list) {
   return list.filter(evenNumber);
};

const arrSum = list => list.reduce((a,b) => a + b, 0);
const arrSquare = list => list.reduce((a,b) => a * a, 0);
function squareNumber(number) {
    return (number*number); 
};

function getSquareNumber(list) {
   return list.filter(squareNumber);
};

function square(arr) {
    return list.map(function (x) {
      return Math.pow(x, 2);
    });
  }
console.log(arrSum(list));
console.log(getEvenNumber(list));
console.log(list);
console.log(getSquareNumber(list));
console.log(square(list));