/*
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

input = "eu amo muito meu amorzinho";
output = falso

- esclarecendo o problema: na frase não pode ter mais que um caractere repetido
- solução:

cada caracter será uma chave, já que em um objeto não se pode ter mais de uma chave com o mesmo nome.

string = "abbc"

1 - obj = {"a": 1}
2 - obj = {"a": 1, "b": 1}
3 - obj = {"a": 1, "b": 2} - não é mais únito, retorna falso

obj = { "a": 1, "b": 2}
*/

/* const isUnique = function(frase){

  let objeto = new Object();
  let count = 0;
 // EXEMPLO: "abbc"
  for(let i = 0; i < frase.length; i++){ // i = 2
    // se o objeto existe
    // a letra ta repetida
    if (objeto[frase[i]]) {
      // que tal se retornamos falso aqui?  return false;
      // frase[i] = "b"
      // objeto = {"a":1, "b":1}
      // objeto[frase[i]] = objeto["b"] = 1 - o "b"  existe na linha 33
      objeto[frase[i]]++;
      // objeto = {"a":1, "b":2}

      if (objeto[frase[i]] >= 2) {
        return false;
      }
      return true;
    } else {
      // a letra ainda nao foi achada anteriormente
      // objeto = {"a":1}
      objeto[frase[i]] = 1;
      // objeto = {"a":1, "b":1}
    }
    console.log(objeto);
  }
  return true

}
*/

const isUnique = function(frase){

  let objeto = new Object();
 // EXEMPLO: "abbc"
  for(let i = 0; i < frase.length; i++){ 

    // a letra já existe dentro do objeto
    if (objeto[frase[i]]) {
      // que tal se retornamos falso aqui?  return false;
      // retorna falso pq já tem caractere repetido
        return false;

    } else {
      // a letra ainda nao foi achada anteriormente
      // objeto = {"a":1}
      objeto[frase[i]] = 1;
      // objeto = {"a":1, "b":1}
    }
    console.log(objeto);
  }
  return true

}

const frase = "abbc";
console.log(isUnique(frase))


const teste2 = "aeiou";
console.log(isUnique(teste2));
