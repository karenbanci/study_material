const flattenObject = (object) => {
  let result = {};

  for (const i in object) {
    if (typeof object[i] === "object" && !Array.isArray(object[i])) {
      const temp = flattenObject(object[i]);
      for (const j in temp) {
        if (j in result) {
          result["restaurantId"] = temp[j];
        } else {
          result[j] = temp[j];
        }
      }
    } else {
      result[i] = object[i];
    }
  }
  return result;
};

module.exports = flattenObject;
