/**
 1)
 No jogo de videogame, o personagem começa com health = 10, cada elemento da arr representa 1 nível, e cada nível tem o health do personagem tem um impacto

 se health < 0 - a vida nao fica negativa, set a vida para 0
 se health > 100 - set a vida para 100

 retornar a saúde final do personagem

 arr=[4,-54,25,-100]
 */
// function healthCalculator(health, arr) {
//   let currentHealth = health;

//   for (let i = 0; i < arr.length; i++) {
//     console.log("currentHealth", currentHealth, "arr[i]", arr[i]);
//     currentHealth = currentHealth + arr[i];

//     if (currentHealth < 0) {
//       currentHealth = 0;
//     } else if (currentHealth > 100) {
//       currentHealth = 100;
//     }
//   }

//   console.log(currentHealth);
//   return currentHealth;
// }
// healthCalculator(10, [5, 43, -220, 64, 32, -650]);

/*
2)
frase = [["Olá"],["Como"],["Vai"],["Você?"]]
width = 16

saída =
***********
*   Olá   *
*   Como  *
*   Vai   *
*  Você?  *
***********
 */
// const jornal = (frase, width) => {
//   const star = "*".repeat(width - 1);
//   console.log(star);
//   for (let i = 0; i < frase.length; i++) {
//     // console.log(frase[i]);
//     for (let j = 0; j < frase.length; j++) {
//       let word = frase[i][j];
//       let len = word.length;

//       // espaço da direita
//       let spaceR = " ".repeat((width - len) / 2 - 1);

//       // definir espaço da esquerda
//       let spaceL = spaceR;

//       if (len % 2 === 0) {
//         //   console.log("par")
//       } else {
//         spaceL = spaceL.slice(0, -1);
//         //   console.log("ímpar")
//       }
//       //definir o espaço da direita

//       const content = "*" + spaceL + word + spaceR + "*";
//       console.log(content);
//     }
//   }
//   console.log(star);
// };

// console.log(
//   jornal(
//     [
//       ["Olá", "Como"],
//       ["Vai", "Você?"],
//     ],
//     11
//   )
// );

/**
3)
Contar quantas ocorrências são necessárias para zerar o array,
x = arr[i]
se arr[i] < x
salvar o novo valor de x, ou seja, x = arr[i]

ocorrência = 0

index =  0  1  2  3  4
input = [3, 3, 5, 2, 3]
output = 0

x = 3  arr[0] = 3
arr[0] = arr[0] - x
arr[0] = 3 - 3
arr[0] = 0
index =  0  1  2  3  4
output = [0, 3, 5, 2, 3]
ocorrencia = 1

x = 3  arr[1] = 3
arr[1] = arr[1] - x
arr[1] = 3 - 3
arr[1] = 0
index =  0  1  2  3  4
output = [0, 0, 5, 2, 3]
ocorrencia = 2

x = 3  arr[2] = 5
arr[2] = arr[2] - x
arr[2] = 5 - 3
arr[2] = 2
index =  0  1  2  3  4
output = [0, 0, 2, 2, 3]
ocorrencia = 3

x = 3  arr[3] = 2
arr[3] = arr[3] - x
arr[3] = 2 - 3      -> atualizar o valor de X pq o resultado nao pode ser negativo
x = arr[3]
x = 2
index =  0  1  2  3  4
output = [0, 0, 2, 2, 3]

-- quando encontrar arr[i] = 0 , continuar

x = 2  arr[2] = 2
arr[2] = arr[2] - x
arr[2] = 2 - 2
arr[2] = 0
index =  0  1  2  3  4
output = [0, 0, 0, 2, 3]
ocorrencia = 4

x = 2  arr[3] = 2
arr[3] = arr[3] - x
arr[3] = 2 - 2
arr[3] = 0
index =  0  1  2  3  4
output = [0, 0, 0, 0, 3]
ocorrencia = 5

x = 2  arr[4] = 2
arr[4] = arr[4] - x
arr[4] = 3 - 2
arr[4] = 1
x = arr[4]
x = 1
index =  0  1  2  3  4
output = [0, 0, 0, 0, 1]
ocorrencia = 6

x = 1  arr[4] = 1
arr[4] = arr[4] - x
arr[4] = 1 - 1
arr[4] = 0
index =  0  1  2  3  4
output = [0, 0, 0, 0, 0]
ocorrencia = 7

//  */
// function zerarArray(arr) {
//   let count = 0;
//   let x = arr[0];

//   for (let i = 0; i < arr.length; i++) {
//     let curr;

//     console.log("x=", x, `       arr[${i}]=`, arr[i]);

//     if (arr[i] >= x) {
//       arr[i] = arr[i] - x;
//       count++;
//     } else if (arr[i] === 0) {
//       continue;
//     } else if (x > arr[i]) {
//       x = arr[i];
//       i = 0;
//     }

//     if (arr[i] > 0 && i === arr.length - 1) {
//       i = 0;
//       console.log("i");
//     }

//     console.log(`arr[${i}]=`, arr[i], "       x=", x);
//     console.log("arr", arr, "\n\n");
//     console.log("x=", x, `       arr[${i}]=`, arr[i]);
//   }
//   console.log("count", count);
//   console.log("final", arr);
// }
// zerarArray([3, 3, 5, 2, 3]);

// Problema 4

// Dado uma array
// ex. [1, 23, 135, 74, 67, 531, 23]
// Saida 2 porque 23 e 23, e 135 e 531
