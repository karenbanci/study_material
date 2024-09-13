// modulos externos
import chalk from "chalk";
import inquirer from "inquirer";

// modulos internos
import fs from "fs";

operation();

function operation() {
  // configuracao de opcoes
  inquirer
    .prompt([
      {
        type: "list",
        name: "action",
        message: "O que você deseja fazer?",
        choices: [
          "Criar Conta",
          "Consultar Saldo",
          "Depositar",
          "Sacar",
          "Transferir",
          "Histórico",
          "Sair",
        ],
      },
    ])
    .then((answer) => {
      // executar acao quando o usuário faz uma escolha
      const action = answer["action"];

      if (action === "Criar Conta") {
        createAccount();
        buildAccount();
      } else if (action == "Consultar Saldo") {
        getAccountBalance();
      } else if (action == "Depositar") {
        deposit();
      } else if (action == "Sacar") {
        widthdraw();
      } else if (action == "Transferir") {
        transfer();
      } else if (action == "Histórico") {
        history();
      } else if (action == "Sair") {
        console.log(chalk.bgBlue.black("Agradecemos sua presença!"));
        process.exit();
      }
    })
    .catch((err) => console.log(err));
}

// criar a conta
function createAccount() {
  console.log(chalk.bgGreen.black("Parabéns por escolher o nosso banco!"));
  console.log(chalk.green("Defina as opções da sua conta a seguir"));
}

function buildAccount() {
  inquirer
    .prompt([
      {
        name: "accountName",
        message: "Digite um nome para a sua conta:",
      },
    ])
    .then((answer) => {
      const accountName = answer["accountName"];
      console.info(accountName);

      // se pasta accounts não existe, irá criar o diretorio
      if (!fs.existsSync("accounts")) {
        fs.mkdirSync("accounts");
      }

      // se a conta já existe, irá lancar uma mensagem dizendo que a conta já existe
      if (fs.existsSync(`accounts/${accountName}.json`)) {
        console.log(
          chalk.bgRed.black("Essa conta já existe, escolha outro nome!")
        );
        buildAccount();
        return;
      }
      //  vai criar um arquivo para o usuário com nome da conta dele
      fs.writeFileSync(
        `accounts/${accountName}.json`,
        '{"balance": 0, "history": []}',
        function (err) {
          console.log(err);
        }
      );

      console.log(chalk.green("Parabéns! A sua conta foi criada"));
      operation();
    })
    .catch((err) => console.log(err));
}

// add an amount to user account
function deposit() {
  inquirer
    .prompt([
      {
        name: "accountName",
        message: "Qual é o nome da sua conta?",
      },
    ])
    .then((answer) => {
      const accountName = answer["accountName"];

      // verificar se a conta já existe
      if (!checkAccount(accountName)) {
        return deposit();
      }

      inquirer
        .prompt([
          {
            name: "amount",
            message: "Quanto você deseja depositar? ",
          },
        ])
        .then((answer) => {
          const amount = answer["amount"];

          // add amount
          addAmount(accountName, amount);

          // operation();
        })
        .catch((err) => console.log(err));
    })
    .catch((err) => console.log(err));
}

function checkAccount(accountName) {
  if (!fs.existsSync(`accounts/${accountName}.json`)) {
    console.log(
      chalk.bgRed.black("Esta conta não existe, escolha outro nome!")
    );
    return false;
  }
  return true;
}

function addAmount(accountName, amount) {
  const accountData = getAccount(accountName);

  if (!amount) {
    console.log(
      chalk.bgRed.black("Ocorreu um erro, tente novamente mais tarde!")
    );
    return deposit();
  }
  accountData.balance = parseFloat(amount) + parseFloat(accountData.balance);

  accountData.history.push(
    `Foi depositado o valor de R$${amount} na sua conta`
  );

  fs.writeFileSync(
    `accounts/${accountName}.json`,
    JSON.stringify(accountData),
    function (err) {
      console.log(err);
    }
  );

  console.log(
    chalk.bgCyanBright.black(
      `Foi depositado o valor de R$${amount} na sua conta`
    )
  );
  operation();
}

function getAccount(accountName) {
  const accountJSON = fs.readFileSync(`accounts/${accountName}.json`, {
    encoding: "utf8",
    flag: "r",
  });
  return JSON.parse(accountJSON);
}

// show account balance
function getAccountBalance() {
  inquirer
    .prompt([
      {
        name: "accountName",
        message: "Qual é o nome da sua conta?",
      },
    ])
    .then((answer) => {
      const accountName = answer["accountName"];

      // verify if account exist

      if (!checkAccount(accountName)) {
        return getAccountBalance();
      }

      const accountData = getAccount(accountName);

      console.log(
        chalk.bgBlue.black(
          `Olá, o saldo da sua conta é de R$${accountData.balance}`
        )
      );
      operation();
    })
    .catch((err) => console.log(err));
}

// transfer from an account to another account
function transfer() {
  inquirer
    .prompt([
      {
        name: "fromAccountName",
        message: "Qual é o nome da sua conta?",
      },
    ])
    .then((answer) => {
      const fromAccountName = answer["fromAccountName"];

      // verificar se a conta já existe
      if (!checkAccount(fromAccountName)) {
        return transfer();
      }

      inquirer
        .prompt([
          {
            name: "toAccountName",
            message: "Para quem você deseja transferir?",
          },
        ])
        .then((answer) => {
          const toAccountName = answer["toAccountName"];

          if (!checkAccount(toAccountName)) {
            return transfer();
          }

          inquirer
            .prompt([
              {
                name: "amount",
                message: "Quanto você deseja transferir? ",
              },
            ])
            .then((answer) => {
              const amount = answer["amount"];

              transferAmount(fromAccountName, toAccountName, amount);
            })
            .catch((err) => console.log(err));
        })
        .catch((err) => console.log(err));
    })
    .catch((err) => console.log(err));
}

// widthdraw an amount from user account
function widthdraw() {
  inquirer
    .prompt([
      {
        name: "accountName",
        message: "Qual é o nome da sua conta?",
      },
    ])
    .then((answer) => {
      const accountName = answer["accountName"];

      if (!checkAccount(accountName)) {
        return widthdraw();
      }

      inquirer
        .prompt([
          {
            name: "amount",
            message: "Quanto você deseja sacar?",
          },
        ])
        .then((answer) => {
          const amount = answer["amount"];

          removeAmount(accountName, amount);
        })
        .catch((err) => console.log(err));
    })
    .catch((err) => console.log(err));
}

function transferAmount(fromAccountName, toAccountName, amount) {
  const fromAccountData = getAccount(fromAccountName);
  const toAccountData = getAccount(toAccountName);

  if (!amount) {
    console.log(chalk.bgRed.black("Deu problema, tente novamente mais tarde!"));
    return transfer();
  }

  if (fromAccountData.balance < amount) {
    console.log(chalk.bgRed.black("Valor indisponível na sua conta!"));
    return transfer();
  }

  // atualizar o valor do usuário que está transferindo o dinheiro
  fromAccountData.balance =
    parseFloat(fromAccountData.balance) - parseFloat(amount);

  fromAccountData.history.push(
    `Você transferiu R$${amount} da sua conta para a conta ${toAccountName}`
  );

  fs.writeFileSync(
    `accounts/${fromAccountName}.json`,
    JSON.stringify(fromAccountData),
    function (err) {
      console.log(err);
    }
  );

  // atualizar o valor do usuário que está recebendo o dinheiro
  toAccountData.balance =
    parseFloat(amount) + parseFloat(toAccountData.balance);

  toAccountData.history.push(
    `${fromAccountName} transferiu R$${amount} para a sua conta`
  );
  fs.writeFileSync(
    `accounts/${toAccountName}.json`,
    JSON.stringify(toAccountData),
    function (err) {
      console.log(err);
    }
  );

  console.log(
    chalk.green(
      `Foi transferido R$${amount} da sua conta para a conta ${toAccountName}`
    )
  );

  operation();
}

function history() {
  inquirer
    .prompt([
      {
        name: "accountName",
        message: "Qual é o nome da sua conta?",
      },
    ])
    .then((answer) => {
      const accountName = answer["accountName"];

      // verify if account exist

      if (!checkAccount(accountName)) {
        return history();
      }

      const accountData = getAccount(accountName);

      const data = accountData.history;

      function printData(data) {
        for (let d of data) {
          console.log(chalk.yellow(d));
        }
      }

      printData(data);
      operation();
    })
    .catch((err) => console.log(err));
}

function removeAmount(accountName, amount) {
  const accountData = getAccount(accountName);

  if (!amount) {
    console.log(chalk.bgRed.black("Deu problema, tente novamente mais tarde!"));
    return widthdraw();
  }

  if (accountData.balance < amount) {
    console.log(chalk.bgRed.black("Valor indisponível na sua conta!"));
    return widthdraw();
  }

  accountData.balance = parseFloat(accountData.balance) - parseFloat(amount);

  accountData.history.push(
    `Foi realizado um saque de R$${amount} da sua conta!`
  );

  fs.writeFileSync(
    `accounts/${accountName}.json`,
    JSON.stringify(accountData),
    function (err) {
      console.log(err);
    }
  );
  console.log(
    chalk.green(`Foi realizado um saque de R$${amount} da sua conta!`)
  );

  operation();
}
