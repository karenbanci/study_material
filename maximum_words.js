/*
I have a array that sentence, I need to return the sentence has the maximum number of words


                            first                       second                      third
Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
words                       5                           4                             6

1o step:
I can to split, account how many words has in each sentence,
entrar em cada string
iterar e contar quantas palavras tem na string

2o step:
just return the number of sentence that has maximum number of words

aqui estou entrando na array (fazer uma busca da sentença)
var maxWords = 0;
for (let i = 0; i < sentences.length; i++) {

  var words = str.split(" ");
  var numberOfWords = words.length;
  0
  "alice and bob love leetcode", "i think so too", "this is great thanks very much"

  words:                words:            words:
  "alice"               "i"                "this"
  "and"                 "think"            "is"
  "bob"                 "so"               "great"
  "love"                "to"               "thanks"
  "leetcode"                               "very"
  "much"
  numberOfWords = 5       4                 6

  var maxWords = 5        5            6;

  if (numberOfWords > maxWords) {
    maxWords = numberOfWords
  }
}
*/

sentences = [
  "alice and bob love leetcode",
  "i think so too",
  "this is great thanks very much",
];

var mostWordsFound = function (sentences) {
  var maxWords = 0;

  for (let i = 0; i < sentences.length; i++) {
    var words = sentences[i].split(" ");
    var numberOfWords = words.length;
    //aqui eu faço comparativo de quem tem o valor maior
    maxWords = Math.max(maxWords, numberOfWords);

  }
  console.log(`numero de palavras ${maxWords}`);
  return maxWords;
};

mostWordsFound(sentences);


// var mostWordsFound = function (sentences) {
//   var maxWords = 0;

//   for (let i = 0; i < sentences.length; i++) {
//     var words = sentences[i].split(" ");
//     var numberOfWords = words.length;

//     if (numberOfWords > maxWords) {
//       maxWords = numberOfWords
//     }
//   }
//   console.log(`numero de palavras ${maxWords}`)
//   return maxWords
// };

// mostWordsFound(sentences);
