const { DataTypes } = require("sequelize");

const db = require("../db/conn");

const User = db.define("User", {
  name: {
    type: DataTypes.STRING,
    allowNull: false, // nao quero valores nulos
  },
  occupation: {
    type: DataTypes.STRING,
    require: true, // campo obrigatorio
  },
  newsletter: {
    type: DataTypes.BOOLEAN, //quero saber se o usuario quer receber a newsletter
  },
});

module.exports = User;
