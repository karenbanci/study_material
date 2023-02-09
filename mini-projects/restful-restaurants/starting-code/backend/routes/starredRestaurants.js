const express = require("express");
const { v4: uuidv4 } = require("uuid");
const router = express.Router();
const ALL_RESTAURANTS = require("./restaurants").restaurants;

/**
 * A list of starred restaurants.
 * In a "real" application, this data would be maintained in a database.
 */
let STARRED_RESTAURANTS = [
  {
    id: "a7272cd9-26fb-44b5-8d53-9781f55175a1",
    restaurantId: "869c848c-7a58-4ed6-ab88-72ee2e8e677c",
    comment: "Best pho in NYC",
  },
  {
    id: "8df59b21-2152-4f9b-9200-95c19aa88226",
    restaurantId: "e8036613-4b72-46f6-ab5e-edd2fc7c4fe4",
    comment: "Their lunch special is the best!",
  },
];

/**
 * Feature 6: Getting the list of all starred restaurants.
 */
router.get("/", (req, res) => {
  /**
   * We need to join our starred data with the all restaurants data to get the names.
   * Normally this join would happen in the database.
   */
  const joinedStarredRestaurants = STARRED_RESTAURANTS.map(
    (starredRestaurant) => {
      const restaurant = ALL_RESTAURANTS.find(
        (restaurant) => restaurant.id === starredRestaurant.restaurantId
      );

      return {
        id: starredRestaurant.id,
        comment: starredRestaurant.comment,
        name: restaurant.name,
      };
    }
  );

  res.json(joinedStarredRestaurants);
});

/**
 * Feature 7: Getting a specific starred restaurant.
 */
router.get("/:id", (req, res) => {
  // Join the starred data with the all restaurants data to get the name of the starred restaurant.
  // Find the restaurant in the list of restaurants.
  const { id } = req.params;

  // If the restaurant doesn’t exist, send a status code to the client to let it know the restaurant was not found.
  if(!restaurant){
    res.status(404).send("Restaurant not found");
    return;
  }

  // Otherwise, create an object with the starred restaurant’s id, comment, and name, and send the restaurant data to the front-end.
  res.json(restaurant);
});


/**
 * Feature 8: Adding to your list of starred restaurants.
 */
router.post("/", (req, res) => {
  //   Find the restaurant in the list of starred restaurants.
  const {body} = req;
  const {id} = body;

  const restaurant = ALL_RESTAURANTS.find((restaurant) => restaurant.id === id);

  // If the restaurant doesn’t exist, send a status code to the client to let it know the restaurant was not found.
  if(!restaurant){
    res.status(404).send("Restaurant not found");
    return;
  }
  // Otherwise, proceed with adding a restaurant to your starred restaurants list:
  // Generate a unique id for the new starred restaurant.
  const newId = uuidv4();

  // Create a record for the new starred restaurant.
  const newStarredRestaurant = {
    id: newId,
    restaurantId: id,
    comment: null
  };
  // Push the new record into STARRED_RESTAURANTS.
  STARRED_RESTAURANTS.push(newStarredRestaurant);
  // Set a success status code and send the restaurant data to the front-end.
  res.status(200).send({
    id: newStarredRestaurant.id,
    comment: newStarredRestaurant.comment,
    name: restaurant.name
  });
});


/**
 * Feature 9: Deleting from your list of starred restaurants.
 */

router.delete("/:id", (req, res) => {
  //   Use the .filter() method to remove this restaurant from your list of starred restaurants and save this list in a variable.
  const {id} = req.params;
  const newListOfStarredRestaurant = STARRED_RESTAURANTS.filter((restaurant) => restaurant.id !== id);
  // If the restaurant doesn’t exist, send a status code to the client to let it know the restaurant was not found.
  if(STARRED_RESTAURANTS.length === newListOfStarredRestaurant.length){
    res.status(404).send("Restaurant not found");
    return;
  }
  // Otherwise, reassign STARRED_RESTAURANTS with the updated list of starred restaurants that you stored in a variable.
  STARRED_RESTAURANTS = newListOfStarredRestaurant;
  res.sendStatus(200);
});

/**
 * Feature 10: Updating your comment of a starred restaurant.
 */
router.put("/:id", (req, res) => {
  //   Find the restaurant in the list of starred restaurants.
  const {id} = req.params;
  const newComment = req.body;
  // If the restaurant doesn’t exist, send a status code to the client to let it know the restaurant was not found.
  if(!restaurant){
    res.status(404).send("Restaurant not found");
    return;
  }
  // Otherwise, update the restaurant’s comment with the comment included in the request body.
  restaurant.comment = newComment;
  // Send a success status code to the client.
  res.sendStatus(200);
});

module.exports = router;
