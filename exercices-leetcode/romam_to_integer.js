/*
Rules:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Abrir uma array que assoscia os simbolos com os valores

const romansKeyValues = {
 'I': 1,
 'V': 5,
 'X': 10,
 'L': 50,
 'C': 100,
 'D': 500,
 'M': 1000
}

 Se o I vem antes do V e X = ele se tornará o 4 e 9;
 IV = 4
 IX = 9

 Se o X vem antes do L e C = ele se tornará o 40 e 90;
 XL = 40
 XC = 90

 Se o C vem antes do D e M = ele se tornara 400 e 900;
 CD = 400
 CM = 900

 tenho que pegar o S do input e transformá-lo em um número

*/

var romanToInt = function (s) {
  // vou separar cada item do input
  var s = s.split("");

  let total = 0;

  // aqui vou especificar o valor de cada String
  const romansKeyValues = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "I") {
      if (s[i + 1] === "V") {
        total += 4;

        i++;
      } else if (s[i + 1] === "X") {
        total += 9;
        i++;
      } else {
        total += romansKeyValues[s[i]];
        // continue;
      }
    } else if (s[i] === "X") {
      if (s[i + 1] === "L") {
        total += 40;
        i++;
      } else if (s[i + 1] === "C") {
        total += 90;
        i++;
      } else {
        total += romansKeyValues[s[i]];
      }
    } else if (s[i] === "C") {
      if (s[i + 1] === "D") {
        total += 400;
        i++;
      } else if (s[i + 1] === "M") {
        total += 900;
        i++;
      } else {
        total += romansKeyValues[s[i]];
      }
    } else {
      total += romansKeyValues[s[i]];
    }
  }
  return total;
};

// I I I
// 1 1 1 = 3
//01 2 3

//i 0. 1. 2  3  4
//  L  V  I  I  I
//  50 5  1  1  1
// 0 50 55

//"LVIII"
//"MCMXCIV"
