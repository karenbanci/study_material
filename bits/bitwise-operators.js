const decimalA = 5;
const decimalB = 3;

console.log("------- AND ----------");
//  operador AND (&)
function operatorAnd(decimalA, decimalB) {
  const binaryA = decimalA.toString(2);
  console.log(`${decimalA} em numero binario: ` + binaryA);

  const binaryB = decimalB.toString(2);
  console.log(`${decimalB} em numero binario: ` + binaryB);

  const and = decimalA & decimalB;
  console.log(`${decimalA} AND ${decimalB}: ` + and);
  console.log(`${and} Em numero binario: ` + and.toString(2));
}

console.log(operatorAnd(decimalA, decimalB));

console.log('------- OR ----------')
//  operador OR (|)
function operatorOr(decimalA, decimalB) {
  const binaryA = decimalA.toString(2);
  console.log(`${decimalA} em numero binario: ` + binaryA);

  const binaryB = decimalB.toString(2);
  console.log(`${decimalB} em numero binario: ` + binaryB);

  const and = decimalA | decimalB;
  console.log(`${decimalA} OR ${decimalB}: ` + and);
  console.log(`${and} Em numero binario: ` + and.toString(2));
}

console.log(operatorOr(decimalA, decimalB));


console.log("------- XOR ----------");
//  operador XOR
function operatorXor(decimalA, decimalB) {
  const binaryA = decimalA.toString(2);
  console.log(`${decimalA} em numero binario: ` + binaryA);

  const binaryB = decimalB.toString(2);
  console.log(`${decimalB} em numero binario: ` + binaryB);

  const and = decimalA ^ decimalB;
  console.log(`${decimalA} XOR ${decimalB}: ` + and);
  console.log(`${and} Em numero binario: ` + and.toString(2));
}

console.log(operatorXor(decimalA, decimalB));

console.log("------- << bit a bit ----------");
//  operador << bit a bit
function operatorLeftDeslocate(decimalA, decimalB) {
  const binaryA = decimalA.toString(2);
  console.log(`${decimalA} em numero binario: ` + binaryA);

  const binaryB = decimalB.toString(2);
  console.log(`${decimalB} em numero binario: ` + binaryB);

  const and = decimalA << decimalB;
  console.log(`${decimalA} << ${decimalB}: ` + and);
  console.log(`${and} Em numero binario: ` + and.toString(2));
}

console.log(operatorLeftDeslocate(decimalA, decimalB));

console.log("------- >> bit a bit ----------");
//  operador >> bit a bit
function operatorRightDeslocate(decimalA, decimalB) {
  const binaryA = decimalA.toString(2);
  console.log(`${decimalA} em numero binario: ` + binaryA);

  const binaryB = decimalB.toString(2);
  console.log(`${decimalB} em numero binario: ` + binaryB);

  const and = decimalA >> decimalB;
  console.log(`${decimalA} << ${decimalB}: ` + and);
  console.log(`${and} Em numero binario: ` + and.toString(2));
}

console.log(operatorRightDeslocate(decimalA, decimalB));
