const LinkedList = require("./LinkedList");
const Node = require("./Node");

class HashMap {
  constructor(size = 0) {
    this.hashmap = new Array(size).fill(null).map(() => new LinkedList());
  }

  hash(key) {
    let hashCode = 0;
    for (let i = 0; i < key.length; i++) {
      hashCode += hashCode + key.charCodeAt(i);
    }
    return hashCode % this.hashmap.length;
  }

  assign(key, value) {
    const arrayIndex = this.hash(key);
    this.hashmap[arrayIndex] = value;
  }

  retrieve(key) {
    const arrayIndex = this.hash(key);
    return this.hashmap[arrayIndex];
  }
}

module.exports = HashMap;

const parkInventory = new HashMap(2);
parkInventory.assign("reed", "marsh plant");
parkInventory.assign("deer", "forest animal");

console.log(parkInventory.retrieve("reed"));
console.log(parkInventory.retrieve("deer"));
