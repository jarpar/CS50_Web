people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw" },
    {"name": "Draco", "house": "Slytherin"}
]


"""
def f(person):
    return person["name"]

people.sort(key=f)
"""
people.sort(ket=lambda person: person["name"])

print(people)