game_running = True
select_weapon = True
rnum = 1
import os
from termcolor import colored
import random 
import time 
def clear(seconds = 0):
   time.sleep(seconds)
   os.system('clear')

player_moves = 0
third_level = True 

monster_names = ["Brady", "Jack", "Charlie", "Jude", "Austin"] 
monster_names2 = ["Brady", "Jack", "Charlie", "Jude", "Austin"] 
boss_names = ["Brady", "Jack", "Charlie", "Jude", "Austin"]
monster_name = random.choice(monster_names) 
while game_running == True:
    new_round = True
    player = {"attack": 10, "heal": 16, "health": 100}
    monster = {"attack": 12, "health": 100}
    weapon = {"close range": "Sword", "long range": "Bow and Arrow"}
    
    clear(.1)
    random_name = random.randint( 0, 4)
    monster_name1 = monster_names[random_name]
    del monster_names2[random_name]
    random_name = random.randint( 0, 3)
    monster_name2 = monster_names2[random_name]
    del boss_names[random_name]
    random_name = random.randint( 0, 2)
    boss_name = boss_names[random_name]
    

    print("---" * 7)
    print("Enter PLAYER Name")
    player_name = input() 
    clear() 
    while select_weapon == True:
        clear(1)
        print("---" * 7)
        print("Please Select Weapon")
        print("1) Sword")
        print("2) Bow and Arrow")
        player_weapon = input()
        if player_weapon == "1":
            print("---" * 7)
            print("You have chosen a sword as your weapon")
            player = {"attack": 14, "heal": 12, "health": 100}
            monster = {"attack" : 16, "health" : 100, "name" : random_name}
            select_weapon = False
        elif player_weapon == "2":
            print("---" * 7)
            print("You have chosen a bow and arrow as your weapon")
            player = {"attack": 8, "heal": 20, "health": 100}
            monster = {"attack" : 16, "health" : 100, "name" : random_name}
            select_weapon = False
        else:
            print("***" * 7)
            print("ERR: Invalid Input")
            print("***" * 7)
    clear(1.5)
    
    

    while new_round == True:
        
        player_won = False
        monster_won = False
        if player["health"] <= 25: 
          os.system('clear')
          print("---" * 7)
          print(colored(player_name + " has " + str(player["health"]) + " health","red"))
          print(monster_name1 + " has " + str(monster["health"]) + " health")
          print("---" * 7)
          print("Plese Select Action")
          print("1) Attack")
          print("2) Heal")
          print("3) Exit Game")

        elif player["health"] <= 50:
          os.system('clear')
          print("---" * 7)
          print(colored(player_name + " has " + str(player["health"]) + " health","yellow"))
          print(monster_name1 + " has " + str(monster["health"]) + " health")
          print("---" * 7)
          print("Plese Select Action")
          print("1) Attack")
          print("2) Heal")
          print("3) Exit Game")
        
        else:
          os.system('clear')
          print("---" * 7)
          print(colored(player_name + " has " + str(player["health"]) + " health","green"))
          print(monster_name1 + " has " + str(monster["health"]) + " health") 
          print("---" * 7)
          print("Plese Select Action")
          print("1) Attack")
          print("2) Heal")
          print("3) Exit Game")

        player_choice = input()

        if player_choice == "1":
            player_moves + 1 
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
            player_moves + 1 
            print("Heal player")
            player["health"] = player["health"] + player["heal"]
            if player["health"] >= 100:
                player["health"] = 100
        elif player_choice == "3":
            player_moves + 1 
            print("---" * 7)
            print("Thanks for playing!!!!")
            new_round = False
            game_running = False
        
        else:
            print("***" * 7)
            print("ERR: INVALID INPUT")
            print("***" * 7)
        if player_won == True and not monster_won == True:
            os.system('clear') 
            print("---" * 7)
            print("You defeated " + monster_name1)
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
                    "attack": 10,
                    "heal": 16,
                    "health": 100
                }
                monster = {"attack": 20, "health": 150}
                weapon = {
                    "close range": "Sword",
                    "long range": "Bow and Arrow"
                }
                clear()
                print("***" * 7)
                print("LEVEL TWO")
                print("***" * 7)
                clear(3)
                while second_level == True:
                    new_round = True
                  

                    print("---" * 7)
                    print("Enter PLAYER Name")
                    player_name = input()
                    clear()
                     

                    while weapon_select == True:
                        clear(1)
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
                                "attack": 8,
                                "heal": 18,
                                "health": 100
                            }
                            monster = {
                                "attack": 10,
                                "health": 100
                            }
                            weapon_select = False
                            second_level = False
                        else:
                            print("Invalid Input")
                        clear(1.5)
                        
                        
                while new_round == True:

                    player_won = False
                    monster_won = False
                    if player["health"] <= 25: 
                      clear()
                      print("---" * 7)
                      print(colored(player_name + " has " + str(player["health"]) + " health","red"))
                      print(monster_name2 + " has " + str(monster["health"]) + " health")
                      print("---" * 7)
                      print("Plese Select Action")
                      print("1) Attack")
                      print("2) Heal")
                      print("3) Exit Game")

                    elif player["health"] <= 50:
                      clear()
                      print("---" * 7)
                      print(colored(player_name + " has " + str(player["health"]) + " health","yellow"))
                      print(monster_name2 + " has " + str(monster["health"]) + " health")
                      print("---" * 7)
                      print("Plese Select Action")
                      print("1) Attack")
                      print("2) Heal")
                      print("3) Exit Game")
                    
                    else:
                      clear()
                      print("---" * 7)
                      print(colored(player_name + " has " + str(player["health"]) + " health","green"))
                      print(monster_name2 + " has " + str(monster["health"]) + " health")
                      print("---" * 7)
                      print("Plese Select Action")
                      print("1) Attack")
                      print("2) Heal")
                      print("3) Exit Game")
                    
                    player_choice = input()

                    if player_choice == "1":
                      player_moves + 1 
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
                        player_moves + 1 
                        print("Heal player")
                        player["health"] = player["health"] + player["heal"]
                        if player["health"] >= 100:
                            player["health"] = 100
                            player_moves - 1
                            print("Health is already at its maximum")
                    elif player_choice == "3":
                        print("---" * 7)
                        print("Thanks for playing!!!!")
                        new_round = False
                        game_running = False
                    
                    if player_won == True and not monster_won == True:
                        while monster_won == True: 
                          os.system('clear')
                          print("---" * 7)
                          print("You defeated " + monster_name2)
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
                            
                            weapon_select = True
                            clear()
                            print("***" * 7)
                            print("LEVEL THREE")
                            print("***" * 7)
                            clear(3)
                            player = {
                                "attack": 15,
                                "heal": 18,
                                "health": 100
                            }
                            monster = {
                                "attack": 25,
                                "health": 200
                            }
                            weapon = {
                                "close range": "Sword",
                                "long range": "Bow and Arrow"
                            }
                        else: 
                            print("***" * 7)
                            print("ERR: INVAILID INPUT")
                            print("***" * 7)

                        weapon_select = True 

                        while third_level == True:
                                new_round = True
                                os.system('clear')




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
                                            "attack": 8,
                                            "heal": 18,
                                            "health": 100
                                        }
                                        monster = {
                                            "attack": 10,
                                            "health": 100
                                        }
                                        weapon_select = False
                                        second_level = False
                                    else:
                                        print("Invalid Input")
                                    clear()
                                    print("---" * 7)
                                    print("Enter PLAYER Name")
                                    player_name = input()
                                    clear()
                                    
                        while new_round == True:

                                player_won = False
                                monster_won = False
                                if player["health"] <= 25: 
                                  os.system('clear')
                                  print("---" * 7)
                                  print(colored(player_name + " has " + str(player["health"]) + " health","red"))
                                  print(boss_name + " has " + str(monster["health"]) + " health")
                                  print("---" * 7)
                                  print("Plese Select Action")
                                  print("1) Attack")
                                  print("2) Heal")
                                  print("3) Exit Game")

                                elif player["health"] <= 50:
                                  os.system('clear')
                                  print("---" * 7)
                                  print(colored(player_name + " has " + str(player["health"]) + " health","yellow"))
                                  print(boss_name + " has " + str(monster["health"]) + " health")
                                  print("---" * 7)
                                  print("Plese Select Action")
                                  print("1) Attack")
                                  print("2) Heal")
                                  print("3) Exit Game")
                                
                                else:
                                  print("---" * 7)
                                  print(colored(player_name + " has " + str(player["health"]) + " health","green")) 
                                  print(boss_name + " has " + str(monster["health"]) + " health")
                                  
                                print("---" * 7)
                                print("Plese Select Action")
                                print("1) Attack")
                                print("2) Heal")
                                print("3) Exit Game")

                                player_choice = input()

                                if player_choice == "1":
                                  player_moves + 1 
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
                                    player_moves + 1
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
                                
                                if player_won == True and not monster_won == True:
                                    os.system('clear') 
                                    print("---" * 7)
                                    print("You defeated " + monster_name)
                                    print("---" * 7)
                                    print("Please Select Action")
                                    print("1) Continue to BOSS")
                                    print("2) Exit Game")

                                    player_choice = input()

                                    if player_choice == "2":
                                        print("---" * 7)
                                        print("Thanks for playing!!!!")
                                        new_round = False
                                        game_running = False
                                    elif player_choice == "1":
                                        boss_level = True
                                        player = {"attack": 20,"heal": 28,"health": 100}
                                        monster = {"attack": 24,"health": 300}
                                        

                                        player_choice = input()

                                    select_weapon = True  

                                    while select_weapon == True:
                                        clear(1)
                                        print("---" * 7)
                                        print("Please Select Weapon")
                                        print("1) Sword")
                                        print("2) Bow and Arrow")
                                        player_weapon = input()
                                        if player_weapon == "1":
                                            print("---" * 7)
                                            print("You have chosen a sword as your weapon")
                                            player = {"attack": 14, "heal": 12, "health": 100}
                                            monster = {"attack" : 16, "health" : 100, "name" : random_name}
                                            select_weapon = False
                                        elif player_weapon == "2":
                                            print("---" * 7)
                                            print("You have chosen a bow and arrow as your weapon")
                                            player = {"attack": 8, "heal": 20, "health": 100}
                                            monster = {"attack" : 16, "health" : 100, "name" : random_name}
                                            select_weapon = False
                                        else:
                                            print("***" * 7)
                                            print("ERR: Invalid Input")
                                            print("***" * 7)
                                    clear(1.5)


                                    while boss_level == True: 
                                    
                                        if player_choice == "1":
                                          
                                          print("Please Select Action")
                                          print("1) Attack")
                                          print("2) Heal")
                                          print("3) Exit Game")

                                          player_choice = input()

                                          if player_choice == "1":
                                            player_moves + 1 
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
                                              player_moves + 1
                                              print("Heal player")
                                              player["health"] = player[
                                                  "health"] + player["heal"]
                                              if player["health"] >= 100:
                                                  player["health"] = 100

                                        else:
                                            print("Invalid Input")

                        
