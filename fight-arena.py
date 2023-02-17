import random
from heroes import Hero
from os import system, name

def clear():
  # for windows
  if name == 'nt':
    _ = system('cls')

  # for mac and linux(here, os.name is 'posix')
  else:
    _ = system('clear')

names = ["James", "Conan", "Eric", "Bertrand", "Jason", "Jacob", "George", "Adam", "Sylvo", "Siergiej", "Marek", "Robert", "Simon", "Bob", "Caspar", "Slavko", "Neo", "Harold", "Kirsten"]

p1 = Hero(random.choice(names))
print(p1)