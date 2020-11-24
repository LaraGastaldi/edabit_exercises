class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

p1 = Person('Michael', 'Smith', 40)
p2 = Person('Alice', 'Waters', 21)
p3 = Person('Zoey', 'Jones', 29)
p4 = Person('Susan', 'Heffley', 43)
p5 = Person('Bob', 'Fredericson', 70)
p6 = Person('Braxton', 'Leighsonley', 2)
p7 = Person('Joshua', 'Senoron', 99999999999999)
people = [p1, p2, p3, p4, p5, p6, p7]


def people_sort(lst, idx):
    resp = []
    for person in lst:
        # print(person.__dict__)
        resp.append(person)
    return resp


print(people_sort(people, "lastname"))