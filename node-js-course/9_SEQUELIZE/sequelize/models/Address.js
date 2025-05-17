const { DataTypes } = require("sequelize");

const db = require("../db/conn");

const User = require("./User");

const Address = db.define("Address", {
  street: {
    type: DataTypes.STRING,
    allowNull: false, // nao quero valores nulos
  },
  number: {
    type: DataTypes.STRING,
    require: true, // campo obrigatorio
  },
  city: {
    type: DataTypes.STRING,
    require: true, // campo obrigatorio
  },
});

// dentro da tabela Address, eu quero que tenha uma chave estrangeira chamada userId
Address.belongsTo(User, {
  foreignKey: {
    allowNull: false, // nao quero valores nulos
  },
});

module.exports = Address;
