const chalk = require("chalk");

const nota = 2;

// console.log(chalk.green.bold("Sua nota é: " + nota));

if (nota >= 7) {
  console.log(chalk.green.bold("Aprovado"));
} else {
  console.log(chalk.bgRed.bold("Reprovado"));
  console.log(chalk.red.bold("Reprovado"));
}
