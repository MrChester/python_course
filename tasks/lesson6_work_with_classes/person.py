class Person:
    def __init__(self, first_name, last_name, qualification=1):
        self.first_name = first_name
        self.last_name = last_name
        self.qualification = qualification

    def person_info(self):
        print("First name: {}\nLast name: {}\nQualification: {}".format(
            self.first_name, self.last_name, self.qualification))


new_person = Person("Yauheni", "Ramankou")
new_person.person_info()
