//npm install inquirer@8.1.2
const inquirer = require("inquirer");
const chalk = require("chalk");

inquirer
  .prompt([
    {
      name: "p1",
      message: "Digite seu nome completo",
    },
    {
      name: "p2",
      message: "Qual é a sua idade?",
    },
  ])
  .then((answer) => {
    // fazer uma validaçao para verificar se a idade é um número e mostrar um erro caso não seja
    try {
      if (!answer.p1 || !answer.p2) {
        throw new Error("O nome e idade devem ser obrigatórios");
      } else if (!Number.isInteger(parseInt(answer.p2))) {
        throw new Error("A idade deve ser um número");
      }
      // caso seja um número, mostrar uma mensagem de boas vindas
      // console.log(answer);
      console.log(
        chalk.bgYellow.black(`Olá, ${answer.p1}! Você tem ${answer.p2} anos.`)
      );

      // se a idade nao for um numero, imprimir a mensagem de erro em vermelho
    } catch (err) {
      console.log(chalk.bgRed.white(err.message));
    }
  })
  .catch((err) => console.log(err));
