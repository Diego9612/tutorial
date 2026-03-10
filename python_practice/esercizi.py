class Person:
    def __init__(self, name, age):
        self.name = name 
        self._age = age # leading underscore:  somewhat private atrribute

    def get_age(self):
        return self._age
        
    def set_age(self, new_age):
        #add some checks here
        if new_age < 0:
            raise ValueError
        self._age = new_age

   # def presentation(self):
   #    return f"Its a me, {self.name}! I'm {self._age} years old"
    
    def __str__(self):
        return f"Its a-me, {self.name}! I'm {self._age} years old"
    
    def __bool__(self):
        return self._age >= 18
    
    def __add__(self, num):
        self.set_age(self.get_age() + num)
p = Person (name ="Mar10", age = 41)

print(p.name)
print(p.get_age())
p.set_age(42)
print(p.get_age())
#print(p.presentation())
print(p)
print(bool(p))
#print(p._age)


class Worker(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job
    
    def __str__(self):
    #    old_presentation = super().__str__()
    #    job_presentation = f"I work as a {self.job}"
    #    return old_presentation + job_presentation
        return super().__str__()+ f"\nI work as a {self.job}"
    
w = Worker("Luigi", 40, "Plumber")
print(w)
    
w.job = "Ghost Hunter"
print(w)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self._age = age 
        

    def get_age(self):
        return self._age 
    
    def set_age(self, new_age):

d = Dog("Rocky", 3)
print(d.name)
print(g.get._age())  

