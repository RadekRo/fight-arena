import random 

char_class = ["peasant", "thief", "pikeman", "knight", "templar", "berserker", "hero"]

class Hero:
  
  def __init__(self, name):
    self.name = name
    self.age = random.randint(18, 35)
    self.weight = random.randint(75, 115)
    self.height = random.randint(165, 215)
    self.health = int((self.weight*self.height/100)-self.age)
    self.lives = int((self.health / 10) + self.age/20)
    self.weapon = random.randint(1, 9)
    self.shield = random.randint(0, 7)
    self.power = self.weapon + self.shield
    if self.power < 3:
      self.char_class = char_class[0]
    elif 2 < self.power < 5:
      self.char_class = char_class[1]
    elif 4 < self.power < 7:
      self.char_class = char_class[2]
    elif 6 < self.power < 10:
      self.char_class = char_class[3]
    elif 9 < self.power < 12:
      self.char_class = char_class[4]
    elif 11 < self.power < 14:
      self.char_class = char_class[5]
    else:
      self.char_class = char_class[6]
    self.luck = random.randint(0, 1)
    #self.speed = random.randint(1, 3)
    
  def present_yourself(self):
    lives = self.lives * "\u2764 "
    print(f"""Name: {self.name}
Class: {self.char_class}
Age: {self.age}
Weight: {self.weight} kg
Height: {self.height} cm
Health: {lives}
Weapon: {self.weapon}
Shield: {self.shield}
Luck: {self.luck}
    """)