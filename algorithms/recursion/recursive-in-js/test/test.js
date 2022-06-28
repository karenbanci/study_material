console.log = () => {};
const { expect } = require("chai");
const myModule = require("../index");

describe("", () => {
  it("Add a conditional so `recursiveFactorial()` returns `1` when `n` is equal to `0`.", () => {
    const expectedResult = 1;
    const inputValue = 0;

    const actualResult = myModule.recursiveFactorial(inputValue);

    expect(actualResult).to.equal(expectedResult);
  });

  it("The function does not return `1` when `1` is passed as the argument to `recursiveFactorial()`", () => {
    const inputValue = 1;
    const expectedResult = 1;

    const actualResult = myModule.recursiveFactorial(inputValue);

    expect(actualResult).to.equal(expectedResult);
  });

  it("The function does not return the correct solution when a positive number greater than `1` is passed to it. Check that your base case is `n === 0` and your recursive case is `n > 0`", () => {
    const inputValue = 4;
    const expectedResult = 24;

    const actualResult = myModule.recursiveFactorial(inputValue);

    expect(actualResult).to.equal(expectedResult);
  });
});
