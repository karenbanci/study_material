const express = require("express");
const router = express.Router();
const supabaseProvider = require("../provider/supabase");
const flattenObject = require("../utils/flattenObject");
const restaurantsProvider = supabaseProvider.from("restaurants");
const starredRestaurantsProvider = supabaseProvider.from("starred_restaurants");

/**
 * Feature 6: Getting the list of all starred restaurants.
 */
router.get("/", async (_req, res) => {
  const { data } = await starredRestaurantsProvider.select(`
		id,
		comment,
		restaurants (
			id,
			name
		)
	`);

  // Flatten the data. We are doing this because the database will return a nested structure.
  // For demo purposes, we change the structure to make it easier to handle on the frontend.
  const flattenedData = data.map((record) => flattenObject(record));

  res.json(flattenedData);
});

/**
 * Feature 7: Getting a specific starred restaurant.
 */
router.get("/:id", async (req, res) => {
  const { id } = req.params;

  // Find the restaurant with the matching id.
  const { data } = await starredRestaurantsProvider.select("*").eq("id", id);
  const restaurant = data.length > 0 ? data[0] : undefined;

  // If the restaurant doesn't exist, let the client know.
  if (!restaurant) {
    res.sendStatus(404);
    return;
  }

  res.json(restaurant);
});

/**
 * Feature 8: Adding to your list of starred restaurants.
 */
router.post("/", async (req, res) => {
  const { body } = req;
  const { id } = body;

  // Find the restaurant with the matching id.
  const { data: restaurantData } = await restaurantsProvider
    .select("*")
    .eq("id", id);
  const restaurant = restaurantData.length > 0 ? restaurantData[0] : undefined;

  if (!restaurant) {
    res.sendStatus(404);
    return;
  }

  const { data, error } = await starredRestaurantsProvider.insert([
    { restaurantId: id, comment: null },
  ]);

  if (error || data.length !== 1) {
    res.status(400).send({ error });
  }

  res.json(flattenObject(data[0]));
});

/**
 * Feature 9: Deleting from your list of starred restaurants.
 */
router.delete("/:id", async (req, res) => {
  const { id } = req.params;

  const { error } = await starredRestaurantsProvider
    .delete()
    .match({ restaurantId: id });

  if (error) {
    res.status(404).send({ error });
  }

  res.sendStatus(200);
});

/**
 * Feature 10: Updating your comment of a starred restaurant.
 */
router.put("/:id", async (req, res) => {
  const { id } = req.params;
  const { newComment } = req.body;

  const { error } = await starredRestaurantsProvider
    .update({ comment: newComment })
    .match({ id: id });
  if (error) {
    res.status(404).send({ error });
    return;
  }

  res.sendStatus(200);
});

module.exports = router;
