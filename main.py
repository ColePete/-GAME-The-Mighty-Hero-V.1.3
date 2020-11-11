game_running = True
select_weapon = True
import os

while game_running == True:
    new_round = True
    player = {"name": "Cole", "attack": 10, "heal": 16, "health": 100}
    monster = {"name": "Shane", "attack": 12, "health": 100}
    weapon = {"close range": "Sword", "long range": "Bow and Arrow"}
    os.system('clear')
    print("---" * 7)
    print("Enter Player Name")
    player["name"] = input()
    os.system('clear')
    print("---" * 7)
    print("Enter Monster Name")
    monster["name"] = input()
    print("---" * 7)
    while select_weapon == True:
        os.system('clear')
        print("---" * 7)
        print("Please Select Weapon")
        print("1) Sword")
        print("2) Bow and Arrow")
        player_weapon = input()
        if player_weapon == "1":
            print("---" * 7)
            print("You have chosen a sword as your weapon")
            select_weapon = False
        elif player_weapon == "2":
            print("---" * 7)
            print("You have chosen a bow and arrow as your weapon")
            player = {"name": "Cole", "attack": 8, "heal": 18, "health": 100}
            monster = {"name": "Shane", "attack": 10, "health": 100}
            select_weapon = False
        else:
            print("***" * 7)
            print("ERR: Invalid Input")
            print("***" * 7)

    while new_round == True:

        player_won = False
        monster_won = False
        os.system('clear')
        print("---" * 7)
        print(player["name"] + " has " + str(player["health"]) + " health")
        print(monster["name"] + " has " + str(monster["health"]) + " health")
        print("---" * 7)
        print("Plese Select Action")
        print("1) Attack")
        print("2) Heal")
        print("3) Exit Game")

        player_choice = input()

        if player_choice == "1":
            monster["health"] = monster["health"] - player["attack"]
            if monster["health"] <= 0:
                player_won = True
            else:
                player["health"] = player["health"] - monster["attack"]
                if player["health"] <= 0:
                    monster_won = True
                    print("---" * 7)
                    print("You Lose!")
                    print("---" * 7)
                    new_round = False
                    print("Please Select Action")
                    print("1) Restart Game")
                    print("2) Exit Game")

                    player_choice = input()

                    if player_choice == "1":
                        new_round = False
                    elif player_choice == "2":
                        print("---" * 7)
                        print("Thanks for playing!!!!")
                        new_round = False
                        game_running = False
                    else:
                        print("Invalid Input")
        elif player_choice == "2":
            print("Heal player")
            player["health"] = player["health"] + player["heal"]
            if player["health"] >= 100:
                player["health"] = 100
        elif player_choice == "3":
            print("---" * 7)
            print("Thanks for playing!!!!")
            new_round = False
            game_running = False
        elif player_choice == "23":
            print("---" * 7)
            print("BOSS MODE INITIATED")
            print("---" * 7)
            player = {"name": "Cole", "attack": 20, "heal": 28, "health": 100}
            monster = {"name": "Shane", "attack": 24, "health": 300}
            print("Please Select Action")
            print("1) Attack")
            print("2) Heal")
            print("3) Exit Game")

            player_choice = input()

            if player_choice == "1":
                monster["health"] = monster["health"] - player["attack"]
                if monster["health"] <= 0:
                    player_won = True
                else:
                    player["health"] = player["health"] - monster["attack"]
                if player["health"] <= 0:
                    monster_won = True
                    print("---" * 7)
                    print("You Lose!")
                    print("---" * 7)
                    new_round = False
                    print("Please Select Action")
                    print("1) Restart Game")
                    print("2) Exit Game")

                    player_choice = input()

                    if player_choice == "1":
                        new_round = False
                    elif player_choice == "2":
                        print("---" * 7)
                        print("Thanks for playing!!!!")
                        new_round = False
                        game_running = False
                    else:
                        print("Invalid Input")
        else:
            print("***" * 7)
            print("ERR: INVALID INPUT")
            print("***" * 7)
        if player_won == True and not monster_won == True:
            os.system('clear')
            print("---" * 7)
            print("You defeated " + monster["name"])
            print("---" * 7)
            print("Please Select Action")
            print("1) Continue to next level")
            print("2) Exit Game")

            player_choice = input()

            if player_choice == "2":
                print("---" * 7)
                print("Thanks for playing!!!!")
                new_round = False
                game_running = False

            elif player_choice == "1":
                second_level = True
                weapon_select = True
                player = {
                    "name": "Cole",
                    "attack": 10,
                    "heal": 16,
                    "health": 100
                }
                monster = {"name": "Shane", "attack": 20, "health": 150}
                weapon = {
                    "close range": "Sword",
                    "long range": "Bow and Arrow"
                }
                os.system('clear')
                print("***" * 7)
                print("LEVEL TWO")
                print("***" * 7)
                while second_level == True:
                    new_round = True
                    os.system('clear')
                    print("---" * 7)
                    print("Enter Player Name")
                    player["name"] = input()
                    os.system('clear')
                    print("---" * 7)
                    print("Enter Monster Name")
                    monster["name"] = input()
                    print("---" * 7)
                    print("---" * 7)
                    while weapon_select == True:
                        os.system("clear")
                        print("---" * 7)
                        print("Please Select Weapon")
                        print("1) Sword")
                        print("2) Bow and Arrow")
                        player_weapon = input()
                        if player_weapon == "1":
                            print("---" * 7)
                            print("You have chosen a sword as your weapon")
                            weapon_select = False
                            second_level = False
                        elif player_weapon == "2":
                            print("---" * 7)
                            print(
                                "You have chosen a bow and arrow as your weapon"
                            )
                            player = {
                                "name": "Cole",
                                "attack": 8,
                                "heal": 18,
                                "health": 100
                            }
                            monster = {
                                "name": "Shane",
                                "attack": 10,
                                "health": 100
                            }
                            weapon_select = False
                            second_level = False
                        else:
                            print("Invalid Input")
                while new_round == True:

                    player_won = False
                    monster_won = False
                    os.system('clear')
                    print("---" * 7)
                    print(player["name"] + " has " + str(player["health"]) +
                          " health")
                    print(monster["name"] + " has " + str(monster["health"]) +
                          " health")
                    print("---" * 7)
                    print("Plese Select Action")
                    print("1) Attack")
                    print("2) Heal")
                    print("3) Exit Game")

                    player_choice = input()

                    if player_choice == "1":
                        monster[
                            "health"] = monster["health"] - player["attack"]
                        if monster["health"] <= 0:
                            player_won = True
                        else:
                            player["health"] = player["health"] - monster[
                                "attack"]
                            if player["health"] <= 0:
                                monster_won = True
                                print("---" * 7)
                                print("You Lose!")
                                print("---" * 7)
                                new_round = False
                                print("Please Select Action")
                                print("1) Restart Game")
                                print("2) Exit Game")

                                player_choice = input()

                                if player_choice == "1":
                                    new_round = False
                                elif player_choice == "2":
                                    print("---" * 7)
                                    print("Thanks for playing!!!!")
                                    new_round = False
                                    game_running = False
                                else:
                                    print("Invalid Input")
                    elif player_choice == "2":
                        print("Heal player")
                        player["health"] = player["health"] + player["heal"]
                        if player["health"] >= 100:
                            player["health"] = 100
                    elif player_choice == "3":
                        print("---" * 7)
                        print("Thanks for playing!!!!")
                        new_round = False
                        game_running = False
                    elif player_choice == "23":
                        print("---" * 7)
                        print("BOSS MODE INITIATED")
                        print("---" * 7)
                        player = {
                            "name": "Cole",
                            "attack": 20,
                            "heal": 28,
                            "health": 100
                        }
                        monster = {
                            "name": "Shane",
                            "attack": 24,
                            "health": 300
                        }
                        print("Please Select Action")
                        print("1) Attack")
                        print("2) Heal")
                        print("3) Exit Game")

                        player_choice = input()

                        if player_choice == "1":
                            monster["health"] = monster["health"] - player[
                                "attack"]
                            if monster["health"] <= 0:
                                player_won = True
                            else:
                                player["health"] = player["health"] - monster[
                                    "attack"]
                            if player["health"] <= 0:
                                monster_won = True
                                print("---" * 7)
                                print("You Lose!")
                                print("---" * 7)
                                new_round = False
                                print("Please Select Action")
                                print("1) Restart Game")
                                print("2) Exit Game")
                                print("3) Continue To Next Level")

                                player_choice = input()

                                if player_choice == "1":
                                    new_round = False
                                elif player_choice == "2":
                                    print("---" * 7)
                                    print("Thanks for playing!!!!")
                                    new_round = False
                                    game_running = False
                                else:
                                    print("Invalid Input")
                    if player_won == True and not monster_won == True:
                        os.system('clear')
                        print("---" * 7)
                        print("You defeated " + monster["name"])
                        print("---" * 7)
                        print("Please Select Action")
                        print("1) Continue to next level")
                        print("2) Exit Game")

                        player_choice = input()

                        if player_choice == "2":
                            print("---" * 7)
                            print("Thanks for playing!!!!")
                            new_round = False
                            game_running = False

                        elif player_choice == "1":
                            second_level = True
                            weapon_select = True
                            os.system('clear')
                            print("***" * 7)
                            print("LEVEL THREE")
                            print("***" * 7)
                            player = {
                                "name": "Cole",
                                "attack": 15,
                                "heal": 18,
                                "health": 100
                            }
                            monster = {
                                "name": "Shane",
                                "attack": 25,
                                "health": 200
                            }
                            weapon = {
                                "close range": "Sword",
                                "long range": "Bow and Arrow"
                            }

                            while second_level == True:
                                new_round = True
                                os.system('clear')
                                print("---" * 7)
                                print("Enter Player Name")
                                player["name"] = input()
                                os.system('clear')
                                print("---" * 7)
                                print("Enter Monster Name")
                                monster["name"] = input()
                                print("---" * 7)
                                print("---" * 7)
                                while weapon_select == True:
                                    os.system('clear')
                                    print("---" * 7)
                                    print("Please Select Weapon")
                                    print("1) Sword")
                                    print("2) Bow and Arrow")
                                    player_weapon = input()
                                    if player_weapon == "1":
                                        print("---" * 7)
                                        print(
                                            "You have chosen a sword as your weapon"
                                        )
                                        weapon_select = False
                                        second_level = False
                                    elif player_weapon == "2":
                                        print("---" * 7)
                                        print(
                                            "You have chosen a bow and arrow as your weapon"
                                        )
                                        player = {
                                            "name": "Cole",
                                            "attack": 8,
                                            "heal": 18,
                                            "health": 100
                                        }
                                        monster = {
                                            "name": "Shane",
                                            "attack": 10,
                                            "health": 100
                                        }
                                        weapon_select = False
                                        second_level = False
                                    else:
                                        print("Invalid Input")
                            while new_round == True:

                                player_won = False
                                monster_won = False
                                os.system('clear')

                                print("---" * 7)
                                print(player["name"] + " has " +
                                      str(player["health"]) + " health")
                                print(monster["name"] + " has " +
                                      str(monster["health"]) + " health")
                                print("---" * 7)
                                print("Plese Select Action")
                                print("1) Attack")
                                print("2) Heal")
                                print("3) Exit Game")

                                player_choice = input()

                                if player_choice == "1":
                                    monster["health"] = monster[
                                        "health"] - player["attack"]
                                    if monster["health"] <= 0:
                                        player_won = True
                                    else:
                                        player["health"] = player[
                                            "health"] - monster["attack"]
                                        if player["health"] <= 0:
                                            monster_won = True
                                            print("---" * 7)
                                            print("You Lose!")
                                            print("---" * 7)
                                            new_round = False
                                            print("Please Select Action")
                                            print("1) Restart Game")
                                            print("2) Exit Game")

                                            player_choice = input()

                                            if player_choice == "1":
                                                new_round = False
                                            elif player_choice == "2":
                                                print("---" * 7)
                                                print("Thanks for playing!!!!")
                                                new_round = False
                                                game_running = False
                                            else:
                                                print("Invalid Input")
                                elif player_choice == "2":
                                    print("Heal player")
                                    player["health"] = player[
                                        "health"] + player["heal"]
                                    if player["health"] >= 100:
                                        player["health"] = 100
                                elif player_choice == "3":
                                    print("---" * 7)
                                    print("Thanks for playing!!!!")
                                    new_round = False
                                    game_running = False
                                elif player_choice == "23":
                                    print("---" * 7)
                                    print("BOSS MODE INITIATED")
                                    print("---" * 7)
                                    player = {
                                        "name": "Cole",
                                        "attack": 20,
                                        "heal": 28,
                                        "health": 100
                                    }
                                    monster = {
                                        "name": "Shane",
                                        "attack": 24,
                                        "health": 300
                                    }
                                    print("Please Select Action")
                                    print("1) Attack")
                                    print("2) Heal")
                                    print("3) Exit Game")

                                    player_choice = input()

                                    if player_choice == "1":
                                        monster["health"] = monster[
                                            "health"] - player["attack"]
                                        if monster["health"] <= 0:
                                            player_won = True
                                        else:
                                            player["health"] = player[
                                                "health"] - monster["attack"]
                                        if player["health"] <= 0:
                                            monster_won = True
                                            print("---" * 7)
                                            print("You Lose!")
                                            print("---" * 7)
                                            new_round = False
                                            print("Please Select Action")
                                            print("1) Restart Game")
                                            print("2) Exit Game")

                                            player_choice = input()

                                            if player_choice == "1":
                                                new_round = False
                                            elif player_choice == "2":
                                                print("---" * 7)
                                                print("Thanks for playing!!!!")
                                                new_round = False
                                                game_running = False
                                            else:
                                                print("Invalid Input")
                                if player_won == True and not monster_won == True:
                                    os.system('clear')
                                    print("---" * 7)
                                    print("You defeated " + monster["name"] +
                                          " and saved the village")
                                    print("---" * 7)
                                    print("Please Select Action")
                                    print("1) Restart Game")
                                    print("2) Exit Game")

                                    player_choice = input()

                                    if player_choice == "1":
                                        new_round = False
                                    elif player_choice == "2":
                                        print("---" * 7)
                                        print("Thanks for playing!!!!")
                                        new_round = False
                                        game_running = False

                                    else:
                                        print("Invalid Input")

                        else:
                            print("Invalid Input")
