/*
index      0 1 2 3 4 5 6
address = "1 . 1 . 1 . 1"

charactere:
index[0] = 1
index[1] = .
index[2] = 1
index[3] = .
index[4] = 1
index[5] = .
index[6] = 1

i =   ->

https://www.devmedia.com.br/javascript-replace-substituindo-valores-em-uma-string/39176#:~:text=Em%20caso%20de%20mais%20de,express%C3%A3o%20regular%20no%20primeiro%20par%C3%A2metro.

https://www.regextester.com/106224

*/

// var defangIPaddr = function(address) {
// //    [^0-9a-zA-Z]     regex de caracteres especiais
// //   / regEX /g  é para englobar todos os caracteres especiais

//     var replace = address.replace(/[^0-9a-zA-Z]/g, "[.]")
//     return replace
// };

var defangIPaddr = function (address) {
  var replace = address.replaceAll(".", "[.]");
  console.log(replace);
  return replace;
};
address = "1.1.1.1";
defangIPaddr(address);
