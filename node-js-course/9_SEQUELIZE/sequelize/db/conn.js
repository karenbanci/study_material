const { Sequelize } = require("sequelize");

const sequelize = new Sequelize("nodesequelize2", "root", "Nalacarolina1", {
  host: "localhost",
  dialect: "mysql",
});

try {
  sequelize.authenticate();
  console.log("Conexão com o banco de dados estabelecida com sucesso.");
} catch (error) {
  console.log("Conexão falhou: " + error);
}

module.exports = sequelize;
