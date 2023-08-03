# odd_num = [1, 2, 3, 4, 5, 6]
# odd_numbers = list(filter(lambda x: x % 2 == 1, odd_num))

# print(odd_numbers)

# class CO:
#   def subn(self,a,b):
#            return a-b
#   def addn(self,a,b):
#            return a+b
  
# obj=CO()
# print("addition of two number is ", obj.addn(5,5))
# print("suns of two number is ", obj.subn(18,8))

# class Animal:
#     def animal_sound(self):
#         return "make sound"
# class Cat(Animal):
#     def cat_sound(self):
#         return self.animal_sound()+ "Meow"
#     def _str_(self):
#         return "CAT"
    
# catobj=Cat()
# print(catobj,catobj.cat_sound())


# class Animal:
#     def animal_sound(self):
#         return "make sound"
# class Cat(Animal):
#     def cat_sound(self):
#         return self.animal_sound()+ "Meow"
#     def _str_(self):
#         return "CAT"
# class Dog(Animal):
#     def dog_sound(self):
#         return self.animal_sound()+" BOW"
#     def _str_(self):
#         return "DOG"
  
# catobj=Cat()
# print(catobj,catobj.cat_sound())
# dogobj=Dog()
# print(dogobj,dogobj.dog_sound())

#multilevel
# class Animal:
#     def animal_sound(self):
#         return "make sound"
# class Cat(Animal):
#     def cat_sound(self):
#         return self.animal_sound()+ "Meow"
# class Catcolor(Cat):
#     def _str_(self):
#         return "CAT"
#     def color(self):
#         return "color is black"
    
# catcolor=Catcolor()
# print(catcolor,catcolor.cat_sound())
# print(catcolor,catcolor.color())



class Animal:
    def animal_sound(self):
        return "make sound"
class Cat(Animal):
    def cat_sound(self):
        return self.animal_sound()+ "Meow"
class Catcolor(Cat):
    def _str_(self):
        return "CAT"
    def color(self):
        return "color is black"
class Dog(Animal):
    def dog_sound(self):
        return self.animal_sound()+ "BOW"
class Dogcolor(Dog):
    def _str_(self):
        return "DOG"
    def color(self):
        return "color is WHITE"
    
catcolor=Catcolor()
print(catcolor,catcolor.cat_sound())
print(catcolor,catcolor.color())
dogcolor=Dogcolor()
print(dogcolor,dogcolor.dog_sound())
print(dogcolor,dogcolor.color())