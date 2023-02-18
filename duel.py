import random
from os import system, name
import time

def clear():
  if name == 'nt':
    _ = system("cls")
  else:
    _ = system("clear")

def fight(first_enemy, second_enemy):

    start_fight = input("Do you want them to enter the arena and fight?\nEnter 'Y'/'y' for yes. Any other key will leave the game: ")

    if start_fight.upper() == "Y":
        turn = 1
        while True:
            if turn%2 == 1:
                fighter = first_enemy
                defender = second_enemy
            else:
                fighter = second_enemy
                defender = first_enemy
            fighter_health = fighter.lives * "\u2764 "
            defender_health = defender.lives * "\u2764 "
            print(f"""
Attacker: {fighter.name}: {fighter_health}
Defender: {defender.name}: {defender_health}
            """)
            print(f"{fighter.name} attacks!")
            time.sleep(1.5)
            fighter_attack_power = fighter.weapon + random.randrange(1,6) + fighter.luck
            defender_defensive_skill = defender.shield + random.randrange(1,6) + defender.luck
            
            if fighter_attack_power > defender_defensive_skill:
                hit_power = fighter_attack_power - defender_defensive_skill
                print(f"Hit! {hit_power} wound(s)!")
                defender.lives -= hit_power
            else:
                print("Miss!")
            time.sleep(1.5)
            if defender.lives < 1:
                print(f"{defender.name} - died! {fighter.name} - wins! Hail and glory to the winner!")
                break
            if turn > 20:
                if fighter.lives > defender.lives:
                    print(f"The fight is over. {fighter.name} wins by points. Bravo!")
                elif defender.lives > fighter.lives:
                    print(f"The fight is over. {defender.name} wins by points. Bravo!")
                else:
                    print("It's a tie! Nobody wins. Glory to both of them!")
                break
            turn += 1
            clear()
    else:
        print("Fight rejected. Thank you. Have a nice day!")