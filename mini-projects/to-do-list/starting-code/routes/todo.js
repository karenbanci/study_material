// require express and it's router component
const express = require('express');

const router = express.Router();

// require the middlewares and callback functions from the controller directory
const { create, read, removeTodo } = require('../controller');

// Create POST route to create an todo
router.post('/todo/create', create);
// Create GET route to read an todo
router.get('/todos', read);
// Create DELETE route to remove an todo
router.delete('/todo/:id', removeTodo);

module.exports = router;
