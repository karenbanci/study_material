console.log = function () {};
const { expect } = require("chai");
const rewire = require("rewire");

describe("", function () {
  it("", function () {
    try {
      var appModule = rewire("../app.js");
    } catch (e) {
      expect(
        true,
        "Double check your code. It likely has a syntax error."
      ).to.equal(false);
    }

    let printData;
    try {
      printData = appModule.__get__("printData");
    } catch (e) {
      expect(true, "Did you declare a `printData()` function?").to.equal(false);
    }

    expect(
      printData,
      "Did you create `printData()` as either a function expression or a function declaration?"
    ).to.be.an.instanceOf(Function);

    let log = [];
    appModule.__set__("console.log", (thing) => log.push(thing));

    printData("test");

    expect(
      log.includes("Item: test"),
      "Does your `printData()` function take in a string parameter and log to the console in the formal: `Item: [string parameter]`? Double check your spelling and punctuation."
    ).to.be.true;
  });
});
