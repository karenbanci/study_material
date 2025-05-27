const { Sequelize } = require("sequelize");

const sequelize = new Sequelize("nodemvc", "root", "Nalacarolina1", {
  host: "localhost",
  dialect: "mysql",
});

try {
  sequelize.authenticate();
  console.log("Connection to the database has been established successfully.");
} catch (error) {
  console.log("Error connecting to the database: ", error);
}

module.exports = sequelize;
