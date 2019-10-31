// Problem 1
// Multiples of 3 and 5
// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

// Find the sum of all the multiples of 3 or 5 below 1000.

'use strict';
function multiples(num) {
    let x = [];
    for (let i=0; i<num; i++) {
        if(i % 3 === 0 || i % 5 === 0) {
            x.push(i)          
        }
    };
        let sumOf =  x.reduce((a,b)=>a+b)
        console.log(sumOf)
} 

console.time('\nResult generated in');
multiples(1000);
console.timeEnd('\nResult generated in');
// result is 233168