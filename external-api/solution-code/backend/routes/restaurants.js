const express = require("express");
const router = express.Router();
const supabaseProvider = require("../provider/supabase");
const restaurantsProvider = supabaseProvider.from("restaurants");

/**
 * Feature 1: Getting a list of restaurants
 */
router.get("/", async (_req, res) => {
  const { data } = await restaurantsProvider.select("*");

  res.json(data);
});

/**
 * Feature 2: Getting a specific restaurant
 */
router.get("/:id", async (req, res) => {
  const { id } = req.params;

  // Find the restaurant with the matching id.
  const { data } = await restaurantsProvider.select("*").eq("id", id);
  const restaurant = data.length > 0 ? data[0] : undefined;

  // If the restaurant doesn't exist, let the client know.
  if (!restaurant) {
    res.sendStatus(404);
    return;
  }

  res.json(restaurant);
});

/**
 * Feature 3: Adding a new restaurant
 */
router.post("/", async (req, res) => {
  const { body } = req;
  const { name } = body;

  const { data, error } = await restaurantsProvider.insert([{ name }]);

  if (error || data.length !== 1) {
    res.status(400).send({ error });
  }

  res.json(data[0]);
});

/**
 * Feature 4: Deleting a restaurant.
 */
router.delete("/:id", async (req, res) => {
  const { id } = req.params;

  const { error } = await restaurantsProvider.delete().match({ id });

  if (error) {
    res.status(404).send({ error });
  }

  res.sendStatus(200);
});

/**
 * Feature 5: Updating the name of a restaurant.
 */
router.put("/:id", async (req, res) => {
  const { id } = req.params;
  const { newName } = req.body;

  const { error } = await restaurantsProvider
    .update({ name: newName })
    .match({ id });

  if (error) {
    res.status(404).send({ error });
    return;
  }

  res.sendStatus(200);
});

exports.router = router;
