my_list = [[1,2,3], [4,5,6]]
print(my_list)
# [[1,2,3], [4,5,6]]
print(my_list[1])
# [4, 5, 6]

my_list[1][1] = "Karen"
print(my_list[1])
# [4, 'Karen', 6]

print(len(my_list))
# 2

print(len(my_list[0]))
# 3
print("----------------")

for row in my_list:
    for item in row:
        print(f"Item: {item}")

print("----------------")
pets = [["dog", "Nala", 18], ["bunny", "Theodora", 6]]

for pet in pets:
    print(f"{pet[1]} is a {pet[0]} who is {pet[2]} years old")

# Nala is a dog who is 18 years old
# Theodora is a bunny who is 6 years old