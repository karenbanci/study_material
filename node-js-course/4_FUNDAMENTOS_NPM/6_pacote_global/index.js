const _ = require("lodash"); // simbole do lodash _
// import _ from "lodash";
// npm global
// objetivo de usar npm link lodash é utilizar o pacote sem instalar diretamente no projeto

const arr = [1, 2, 2, 3, 3, 3, 4, 5];
console.log(_.sortedUniq(arr));
