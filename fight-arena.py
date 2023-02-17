import random
from heroes import Hero

names = ["James", "Conan", "Eric", "Bertrand", "Jason", "Jacob", "George", "Adam", "Sylvo", "Siergiej", "Marek", "Robert", "Simon", "Bob", "Caspar", "Slavko", "Neo", "Harold", "Kirsten"]

p1 = Hero(random.choice(names))
print(p1)