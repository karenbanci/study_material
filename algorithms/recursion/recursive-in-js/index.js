const recursiveFactorial = (n) => {
  // aqui estou adicionando um caso base
  if (n === 0) {
    return 1;
  } else if (n > 0) {
    return n * recursiveFactorial(n - 1);
  }
};

const iterativeFactorial = (n) => {
  result = 1;
  while (n > 0) {
    result *= n;
    n -= 1;
  }
  return result;
};

module.exports = {
  recursiveFactorial,
  iterativeFactorial,
};
