const mysql = require("mysql");

// objetivo é salvar as informações no cache

const pool = mysql.createPool({
  connectionLimit: 10,
  host: "localhost",
  user: "root",
  password: "Nalacarolina1",
  database: "nodemysql2",
});

module.exports = pool;
