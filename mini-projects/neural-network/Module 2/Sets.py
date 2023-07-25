fruit_bowl_one = [ "orange", "banana", "apple", "banana", "banana", "peach", "apple"]
print("Bowl one has: ", len(fruit_bowl_one))

fruit_bowl_two = [ "kiwi", "banana", "apple", "orange", "banana", "peach", "apple", "grapefrui"]
print("\nBowl two has: ", len(fruit_bowl_two))

fruit_bowl_one_unique = set(fruit_bowl_one)
print(f"\nBowl one has this kind of fruit: {fruit_bowl_one_unique}")

fruit_bowl_two_unique = set(fruit_bowl_two)
print(f"\nBowl two has this kind of fruit: {fruit_bowl_two_unique}")

combine_fruit = fruit_bowl_one_unique | fruit_bowl_two_unique
print(f"\nWe have {combine_fruit} fruits at home")

intersection = fruit_bowl_one_unique & fruit_bowl_two_unique
