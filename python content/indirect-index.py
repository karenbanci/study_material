people = ["Jairo", "Karen", "Theodora", "Nala"]
ages = [28, 31, 6, 18]

def print_ages(order=None):
    if order is None:
        order = [0, 1, 2, 3]
    for item in order:
        print(people[item], "is", ages[item], "years old")

print_ages()
"""
('Jairo', 'is', 28, 'years old')
('Karen', 'is', 31, 'years old')
('Theodora', 'is', 6, 'years old')
('Nala', 'is', 18, 'years old')
"""

sort_ages = [2, 3, 0, 1]
print_ages(sort_ages)
"""
('Theodora', 'is', 6, 'years old')
('Nala', 'is', 18, 'years old')
('Jairo', 'is', 28, 'years old')
('Karen', 'is', 31, 'years old')
"""

males = [0]
females = [1, 2, 3]

print("males")
print_ages(males)
# ('Jairo', 'is', 28, 'years old')

print("\nfemales")
print_ages(females)
"""
('Karen', 'is', 31, 'years old')
('Theodora', 'is', 6, 'years old')
('Nala', 'is', 18, 'years old')
"""
