// https://leetcode.com/problems/valid-parentheses/

// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.


// Example 1:

// Input: s = "()"
// Output: true
// Example 2:

// Input: s = "()[]{}"
// Output: true
// Example 3:

// Input: s = "(]"
// Output: false


// Constraints:

// 1 <= s.length <= 104
// s consists of parentheses only '()[]{}'.

/**
 * @param {string} s
 * @return {boolean}
 * (()) > true
 *([)] > false

 *  (    >f

 *  ( )  >t
 *  ^ ^
 *  0 1 < i
 *t f t < parentesisFechado
 * o parenteses fechado retorna true no final pq ele vai dar macth com o parenteses de abertura
 */

var isValid = function(s) {
    let parentesisFechado = true;
    let abertos = [];
    caraterAtual = '';
    // s="(]"

    // Vamos transformar o string em um array de carateres
    let carateres = s.split("");

    for (let i=0; i<s.length; i++){ // para
      let caraterAtual = carateres[i];

      // se o caracter atual é abridor
      if (caraterAtual == "(" || caraterAtual == "[" || caraterAtual == "{"){
          //caracter atual é adicionado na array de abertos
        abertos.push(caraterAtual);
      } else { // se nao, o carater atual é um fechador
        let ultimoAberto = abertos[abertos.length-1];
        let fechadorDoUltimoAberto;

        // se o ultimoAberto é "(", então o fechador seria: ); e asi por diante com todos os fechadores
        if ( ultimoAberto == '(') {
          fechadorDoUltimoAberto = ')';
        }
        if ( ultimoAberto == '[') {
          fechadorDoUltimoAberto = ']';
        }
        if ( ultimoAberto == '{') {
          fechadorDoUltimoAberto = '}';
        }

        if (caraterAtual == fechadorDoUltimoAberto){ //se o carater atual é o fechador do ultimo aberto
            //apagar o ultimo elemento do array abertos
            abertos.pop();
        } else {
            console.log(`A string é invalido porque o fechador do último aberto ${ultimoAberto} é : ${fechadorDoUltimoAberto} e ao inves disso tem ${caraterAtual}`);
            return false;
        }
      }

    } // final do para

    // se abertos é vazio
    // retornar true pq é valido
    // se nao, retornar falso pq nao tem caracter fechador para todos os abertos
    if (abertos.length == 0){
      console.log(`A string é válida pq está vazia`);
      return true;
    } else {
      console.log(`A string é invalida pq nao tem caracter fechador para todos os abertos`)
      return false;
    }
  };


  // Testes
  var resultado, esperado;

  // Input: s = "("
  // Output: false
  resultado = isValid("(");
  esperado = false;
  console.log(resultado == esperado ? "CORRETO" : "incorreto :(", "deu", resultado);

  // Input: s = "()"
  // Output: true
  resultado = isValid("()");
  esperado = true;
  console.log(resultado == esperado ? "CORRETO" : "incorreto :(", "deu", resultado);

  // Input: s = "()[]{}"
  // Output: true
  resultado = isValid("()[]{}");
  esperado = true;
  console.log(resultado == esperado ? "CORRETO" : "incorreto :(", "deu", resultado);

  // Input: s = "(]"
  // Output: false
  resultado = isValid("(]");
  esperado = false;
  console.log(resultado == esperado ? "CORRETO" : "incorreto :(", "deu", resultado);

  resultado = isValid("[]");
  esperado = true;
  console.log(resultado == esperado ? "CORRETO" : "incorreto :(", "deu", resultado);

  resultado = isValid("[][");
  esperado = false;
  console.log(resultado == esperado ? "CORRETO" : "incorreto :(", "deu", resultado);

  resultado = isValid("[)");
  esperado = false;
  console.log(resultado == esperado ? "CORRETO" : "incorreto :(", "deu", resultado);





  // // se parentes está aberto, entao parentesisFechado é falso
  //     // if (caraterAtual == "(" || caraterAtual == "[" || caraterAtual == "{") {
  //       parentesisFechado = false;
  //     } else if (caraterAtual == ")" || caraterAtual == "]" || caraterAtual == "}") {
  //       parentesisFechado = true;
  //     }
  // }

  // return parentesisFechado;
