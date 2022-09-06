/*
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == color.
ruleKey == "name" and ruleValue == name.
Return the number of items that match the given rule.

Example 1:
Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

Example 2:
Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
Output: 2
Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.
*/
/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */
var countMatches = function (items, ruleKey, ruleValue) {
  let count = 0;

  for (let i = 0; i < items.length; i++) {
    // estou dizendo que o items[i][0] é tipo
    if (ruleKey === "type") {
      // se o index 0 for igual ao ruleValue
      if (ruleValue === items[i][0]) {
        count++;
      }
    }

    // estou dizendo que o items[i][1] é cor
    if (ruleKey === "color") {
      // se o index 1 for igual ao ruleValue
      if (ruleValue === items[i][1]) {
        count++;
      }
    }

    // estou dizendo que o items[i][2] é nome
    if (ruleKey === "name") {
      // se o index 2 for igual ao ruleValue
      if (ruleValue === items[i][2]) {
        count++;
      }
    }
  }
  return count;
};

const items = [
  ["phone", "blue", "pixel"],
  ["computer", "silver", "phone"],
  ["phone", "gold", "iphone"],
];

const ruleKey = "type";
const ruleValue = "phone";
console.log(countMatches(items, ruleKey, ruleValue));


/*
Runtime: 134 ms, faster than 19.26% of JavaScript online submissions for Count Items Matching a Rule.

Memory Usage: 45.9 MB, less than 73.27% of JavaScript online submissions for Count Items Matching a Rule.
*/
