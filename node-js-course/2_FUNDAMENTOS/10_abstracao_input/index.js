const inquirer = require("inquirer");

inquirer
  .prompt([
    {
      name: "p1",
      message: "Qual é a primeira nota?",
    },
    {
      name: "p2",
      message: "Qual é a segunda note?",
    },
  ])
  .then((answer) => {
    console.log(answer);
    const media = (parseInt(answer.p1) + parseInt(answer.p2)) / 2;
    console.log(`A média é ${media}`);
  })
  .catch((err) => console.log(err));
