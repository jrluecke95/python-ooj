class Person:
    def __init__(self, name, email, phone, friends = [], greeting_count = 0, greeted_people = []):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends
        self.greeting_count = greeting_count
        self.greeted_people = greeted_people

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        if other_person in self.greeted_people:
            pass
        else:
            self.greeted_people.append(other_person)

    def num_unique_people_greeted(self):
        return len(self.greeted_people)

    def print_contact_info(self):
        print(f"""
        {self.name}'s email: {self.email}
        {self.name}'s phone number: {self.phone}""")
    
    def add_friends(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        return len(self.friends)

    def __str__(self):
        return f"""
        Person: {self.name} {self.email} {self.phone}
        """

sonny = Person('Sonny', 'sonny@hotmail.com', '483-4854948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
jake = Person('Jake', 'jrluecke95@gmail.com', '225-241-6586')

print(sonny.num_unique_people_greeted())
sonny.greet(jordan)
print(sonny.num_unique_people_greeted())
sonny.greet(jordan)
print(sonny.num_unique_people_greeted())
sonny.greet(jake)
print(sonny.num_unique_people_greeted())



class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print(f"""
        {self.year} {self.make} {self.model}
        """)

car = Vehicle("Toyota", "Corolla", "2016")
# car.print_info()
