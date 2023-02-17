import random
from os import system, name
from heroes import Hero
from duel import fight

def clear():
  # for windows
  if name == 'nt':
    _ = system('cls')

  # for mac and linux(here, os.name is 'posix')
  else:
    _ = system('clear')

names = ["James", "Conan", "Eric", "Bertrand", "Jason", "Jacob", "George", "Adam", "Sylvo", "Siergiej", "Marek", "Robert", "Simon", "Bob", "Caspar", "Slavko", "Neo", "Harold", "Kirsten"]

p1 = Hero(random.choice(names))
p2 = Hero(random.choice(names))
print("These are the today's gladiators:\n*********************************")
p1.present_yourself()
p2.present_yourself()
fight(p1, p2)