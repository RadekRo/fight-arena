def fight(first_enemy, second_enemy):

    start_fight = input("Do you want them to enter the arena?\nEnter 'Y' for yes. Any other key will leave the game: ")

    if start_fight.upper() == "Y":
        turn = 1
        while True:
            if turn%2 == 1:
                fighter = first_enemy
                defender = second_enemy
            else:
                fighter = second_enemy
                defender = first_enemy
            print(fighter.name)
            print(defender.name)
            turn += 1
    else:
        print("Fight rejected. Thank you. Have a nice day!")