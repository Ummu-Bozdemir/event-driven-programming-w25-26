car = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : 1964
}

student = {
    'name': 'Ummu',
    'ID': 35449
}


print(student['name'])
print(car['brand'])

class student:
    def __init__(self, name, ID):
        self.name = name
        self.ID =ID
p1 = student('Ummu', 35449)

print(p1.name)
print(p1.ID)

car = ['ford', 'opel', 'bmw']
print(car)

