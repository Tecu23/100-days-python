/* ----  CONSTANT TIME -> O(1) ---- */
const a = 5;

/* ----  LINEAR TIME -> O(n) ---- */

const large = new Array(50_000).fill('dory');

large[10] = 'nemo';

function findNemo(array) {
  let t0 = performance.now();
  for (let i = 0; i < array.length; i++) {
    if (array[i] === 'nemo') {
      console.log('Found NEMO');
      break;
    }
  }
  let t1 = performance.now(); 
  console.log(`Call to find Nemo took ${t1 - t0} miliseconds`)
}

findNemo(large) /* O(n) -> Linear Time */


/* ----  QUADRATIC TIME -> O(n^2) ---- */

const boxes = ['a', 'b', 'c', 'd', 'e'];

function loggAllPairsOfArray(array) {

  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array.length; j++) {
      console.log(array[i], array[j])
    }
  }
}
loggAllPairsOfArray(boxes) /* O(n^2) -> Quadratic Time */


