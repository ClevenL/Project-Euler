let sumOfSquares = 0
let squareOfSum = 0

for (let index = 1; index <= 100; index++) {
    sumOfSquares += index**2
    squareOfSum += index
}
squareOfSum **= 2

console.log(Math.abs(sumOfSquares - squareOfSum))