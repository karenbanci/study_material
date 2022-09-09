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

 fazer um split para separar cada elemento da string
 s = "[{}]{[]}"
 s.split("")
 index    0    1    2    3     4    5    6   7
.....s = "[", "{", "}", "]", "{", "[", "]", "}"

vai ter que iterar cada elemento da array para cada caracter atual for o caracter index s[i]

colocar dentro de uma array vazia os caracteres de abertura
arr = [];
arr.push(s)
arr = [     [, {, {, [      ]
essa array precisa dos seus caracteres de fechamento
se abertura for [, seu fechamento será ]
se abertura for {, seu fechamento será }

entao a quantidade de caracteres de abertura que está na array tem que ser a mesma quantidade de caracteres de fechamento, além disso tem que ser do mesmo tipo
se o caracter do S for igual ao caracter do fechamento, terá que remover o último caractere da array
arr.pop()

caso contrário retornará falso se todos os caracteres de abertura não tiver seu par de fechamento (se nao for igual)

retornar true se a array estiver vazia

retornar falso se a array nao tiver caracter fechador para todos os abertos

 */

var isValid = function(s) {
    //let parentesisFechado = true;
    // uma array vazia que irei incluir os caracteres abertos, conta a quantidade e tipo de caracteres que abrem para comparar e da match com a quantidade e tipo dos caracteres de fechamento
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

        // se o ultimoAberto é "(", então o fechador seria: ); e assim por diante com todos os fechadores
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


  // outra solucao
var isValid = function (s) {
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    let c = s.charAt(i);
    switch (c) {
      case "(":
        stack.push(")");
        break;
      case "[":
        stack.push("]");
        break;
      case "{":
        stack.push("}");
        break;
      default:
        if (c !== stack.pop()) {
          return false;
        }
    }
  }

  return stack.length === 0;
};
