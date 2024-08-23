class Vehicle:

    def __init__(self, max_speed, max_mileage):
        self.max_speed = max_speed
        self.max_mileage = max_mileage
    
    def find_maximum_milege(self):
        print(f'Vehicles mileage is : {self.max_mileage}')
     
    def find_maximum_speed(self):
        print(f'Vehicles speed is : {self.max_speed}')

vehicle=Vehicle(200, 280)
vehicle.find_maximum_milege()
vehicle.find_maximum_speed()

class AutoMobile(Vehicle):
    def __init__(self, max_speed, max_mileage):
        super().__init__(max_speed, max_mileage)
        self.max_mileage *=1.2
        self.max_speed *= 1.5

    def find_maximum_milege(self):
        print(f'Automobiles mileage is : {self.max_mileage}')
    def find_maximum_speed(self):
        print(f'AutoMobiles speed is : {self.max_speed}')

automobile = AutoMobile(200, 280)
automobile.find_maximum_milege()
automobile.find_maximum_speed()

class SUV(Vehicle):
    def __init__(self, max_speed, max_mileage):
        super().__init__(max_speed, max_mileage)
        self.max_speed *= 1.3

    def find_maximum_speed(self):
        print(f'SUVs speed is : {self.max_speed}')

    def write_guarantee(self, guarantee_years):
        guaran_years = (self.max_speed / self.max_mileage) * guarantee_years

        return guaran_years
    
suv = SUV(200,280)
suv.find_maximum_speed()
print(f"Guarantee years for SUV:",suv.write_guarantee(2))

class Person:
    def __init__(self, name, surname, birth_year):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def write_fullname(self):
        print(f"{self.name } {self.surname}")

    def write_age(self):
        age = 2024 - self.birth_year
        return age
    
person = Person(name = "Farrukh", surname =  "Madaminov", birth_year = 2001)
person.write_fullname()
print("Age: ", person.write_age())


class Student(Person):
    def __init__(self, name, surname, birth_year):
        super().__init__(name, surname, birth_year)

    def write_year(self):
        year = "4th year student"
        return year
    
    def write_major(self):
        major = "Economics"
        return major

student = Student(name = "Farrukh", surname =  "Madaminov", birth_year = 2001)
print("Full name:")
student.write_fullname()
print("Year:")
print(student.write_year())
print('Major:')
print(student.write_major())

class Update(Student):
    def __init__(self, name, surname, birth_year, current_year):
        super().__init__(name, surname, birth_year)
        self.current_year = current_year

    def write_update(self, year):
        farq = year - self.current_year
        update_y = self.write_year() + farq
        return f"The student will be {str(update_y)} year {self.write_major()} major student in {year}."
    
student_update = Update(name = "Farrukh", surname =  "Madaminov", birth_year = 2001, current_year = 2024)
print(student_update.write_update(2026))


