/*
    * Complete the 'GetOptimalContentStorage' function below.
//  *
//  * The function is expected to return an INTEGER.
//  * The function accepts INTEGER_ARRAY tiktokStorage as parameter.

// first case
// index    0.  1. 2  3  4.      0  1  2. 3. 4
//          [1, 0, 1, 0, 1]  -> [0, 0, 1, 1, 1] - 1 operation
// swap arr[0] and arr[3]

// second case
//index     0   1  2  3  4. 5  6. 7. 8       0. 1. 2. 3. 4. 5. 6. 7. 8
//          [1, 0, 0, 1, 1, 0, 0, 0, 1]    [1, 1, 0, 1, 1, 0, 0, 0, 0]
// fist operation   arr[1]  and arr[8]

//.   0. 1. 2. 3. 4. 5. 6. 7. 8      0. 1. 2. 3. 4. 5. 6. 7. 8
//   [1, 1, 0, 1, 1, 0, 0, 0, 0] -> [1, 1, 1, 1, 0, 0, 0, 0, 0]
// second operation   arr[2]  and arr[4]
*/

// CORRIGIR

function storage(arr) {
  const metadeDaArray = parseInt(arr.length / 2);
  // console.log(metadeDaArray, arr);
  let countEsq = 0;
  let countDir = 0;
  let definirSide = "";
  let operacoesTotais = 0;

  // define which side of array has more 1
  // left side
  for (let esq = 0; esq < metadeDaArray; esq++) {
    console.log(arr[esq]);
    if (arr[esq] === 1) {
      countEsq++;
    }
  }
  // right side
  for (let dir = arr.length; dir > metadeDaArray + 1; dir--) {
    console.log(arr[dir]);
    if (arr[dir] === 1) {
      countDir++;
    }
  }

  if (countEsq > countDir) {
    definirSide = "esquerdo";
  } else {
    definirSide = "direito";
  }

  // console.log("countEsq", countEsq, "countDir", countDir);
  console.log(definirSide);

  for (
    let ponteiroEsquerdo = 0;
    ponteiroEsquerdo < metadeDaArray;
    ponteiroEsquerdo++
  ) {
    for (
      let ponteiroDireito = arr.length;
      ponteiroDireito > metadeDaArray;
      ponteiroDireito--
    ) {
      if (ponteiroEsquerdo > ponteiroDireito) {
        break;
      }
      // começar a substtuir depois que o lado foi definido
      let temporario;
      // while (operacoesTotais < 2) {
      if (definirSide == "esquerdo") {
        if (arr[ponteiroEsquerdo] === 0 && arr[ponteiroDireito] === 1) {
          temporario = arr[ponteiroEsquerdo];
          arr[ponteiroEsquerdo] = arr[ponteiroDireito];
          arr[ponteiroDireito] = temporario;
          operacoesTotais++;
        }
      } else if (definirSide == "direito") {
        if (arr[ponteiroEsquerdo] === 1 && arr[ponteiroDireito] === 0) {
          temporario = arr[ponteiroDireito];
          arr[ponteiroDireito] = arr[ponteiroEsquerdo];
          arr[ponteiroEsquerdo] = temporario;
          operacoesTotais++;
        }
      }
    }
    // }
  }
  console.log(arr);
  console.log(operacoesTotais, "\n\n\n");
}

// storage([1, 0, 0, 1, 1, 0, 0, 0, 1])
storage([1, 0, 1, 0, 0, 1]);
storage([1, 0, 0, 0, 1, 1]);
