from Birthday import Birthday


class Person:

    def __init__(self, first_name, last_name):
        """A person is defined by a first and last name, a birthday in the 
        form (month, day), and a city they live in. Additional fields may 
        be added here later. A new object requires only a first and last 
        name to instatiate. The remaining fields can be set later using 
        the corresponding mutator methods."""
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = None
        self.city = None

    def introduce(self):
        """Simple way for a person object to introduce itself."""
        print(
            f"Hello, my name is {self.first_name} and my birthday is on {self.say_birthday()}"
        )

    def set_birthday(self, month, day):
        """Mutator for birthday. Uses our very own Birthday class."""
        self._birthday = Birthday(month, day)

    def set_city(self, city):
        """Mutator for city."""
        self.city = city

    def get_first_name(self):
        """Accessor for first name"""
        return self.first_name

    def get_last_name(self):
        """Accessor for last name"""
        return self.last_name

    def __str__(self):
        """String representation for the object"""
        return f"[ {self.first_name} {self.last_name}]"
    
    def say_birthday(self): 
        months_of_year = ["January", "February", "March", "April", "May", "June", "July", "August", 
        "September", "October", "November", "December"]
        day = self._birthday.get_day()
        month = self._birthday.get_month()
        if day == 1 or day == 31:
            print(f"{day}st of {months_of_year[month - 1]}")
        elif day == 2:
            print(f"{day}nd of {months_of_year[month - 1]}")
        elif day == 3:
            print(f"{day}rd of {months_of_year[month - 1]}")
        else:
            print(f"{day}th of {months_of_year[month - 1]}")
    
    def __1t__(self, other):
        is_alpha = None 
        if self.first_name < other.first_name:
           is_alpha = True
        else:
            is_alpha = False 
        return is_alpha   
  
  
Bertha = Person("Bertha", "Walters")
Bertha.set_birthday(8, 8)
Bertha.say_birthday()
other = Person("Alfreda", "Fields")
print(Bertha.__1t__(other))


                        
            
                     
                




