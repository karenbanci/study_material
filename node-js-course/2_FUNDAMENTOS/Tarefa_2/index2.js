//npm install inquirer@8.1.2
const inquirer = require("inquirer");
const chalk = require("chalk");

let nome = "";

const pedirNome = () => {
  inquirer
    .prompt([
      {
        name: "p1",
        message: "Digite seu nome",
      },
      // {
      //   name: "p2",
      //   message: "Qual é a sua idade?",
      // },
    ])
    .then((answer) => {
      // fazer uma validaçao para verificar se a idade é um número e mostrar um erro caso não seja
      try {
        if (!answer.p1) {
          // throw new Error("O nome deve ser obrigatórios");
          console.log(chalk.bgMagenta("O nome deve ser obrigatórios"));
          pedirNome();
          return;
        }
        nome = answer.p1;
        pedirIdade();
        // console.log(answer);
        // console.log(
        //   chalk.bgYellow.black(`Olá, ${answer.p1}! Você tem ${answer.p2} anos.`)
        // );

        // se a idade nao for um numero, imprimir a mensagem de erro em vermelho
      } catch (err) {
        console.log(chalk.bgRed.white(err.message));
      }
    })
    .catch((err) => console.log(err));
};

const pedirIdade = () => {
  inquirer
    .prompt([
      {
        name: "p2",
        message: "Qual é a sua idade?",
      },
    ])
    .then((answer) => {
      // fazer uma validaçao para verificar se a idade é um número e mostrar um erro caso não seja
      try {
        if (!answer.p2) {
          // throw new Error("O nome deve ser obrigatórios");
          console.log(chalk.bgCyan("O idade deve ser obrigatórios"));
          pedirIdade();
          return;
        }
        console.log(typeof answer.p2);
        if (isNaN(answer.p2)) {
          console.log(chalk.bgCyan("O idade deve ser um número"));
          pedirIdade();
          return;
        }
        // console.log(answer);
        console.log(
          chalk.bgYellow.black(`Olá, ${nome}! Você tem ${answer.p2} anos.`)
        );

        // se a idade nao for um numero, imprimir a mensagem de erro em vermelho
      } catch (err) {
        console.log(chalk.bgRed.white(err.message));
      }
    })
    .catch((err) => console.log(err));
};

pedirNome();
