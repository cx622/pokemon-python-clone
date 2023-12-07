import random
import os
class Pokemon:
  name = ""
  level = 0
  health = 0
  max_health = 100
  type = ""
  is_knocked_out = False
  player = False
  def damage(self, poke, move):
    trainerNerf = 1
    if not self.player:
      trainerNerf = 0.95
    damage = round((((2 * self.level / 5 + 2) * 100 * 90 / 80) / 50 + 2) * random.uniform(0.6, 2) * trainerNerf)
    # damage = ((2 * attacker['level'] / 5 + 2) * move['base_power'] * attack_stat / defense_stat) / 50 + 2 original formula
    poke.health -= damage
    print("{name} uses {move}!\nIt deals {dmg} damage! {poke} now has {health} hp!".format(name=self.name,move=move, dmg=damage,poke=poke.name,health=poke.health)) 
    if poke.health <= 0:
      poke.health = 0
      print("{name} has fainted!\n".format(name=poke.name))
      poke.is_knocked_out = True
  def level_up(self):
    if self.level < 100:
      self.level += 1
    self.health = 4 * self.level + 20
    self.max_health = 4 * self.level + 20
  def heal(self):
    self.health = 4 * self.level + 30
    self.max_health = 4 * self.level + 30
    self.is_knocked_out = False
  def __init__(self, name, type, player):
    self.name = name
    if player:
      self.level = 5
    else:
      self.level = random.randint(Pokemon1[0].level - 4, Pokemon1[0].level + 2)
    self.health = 4 * self.level + 30
    self.max_health = 4 * self.level + 30
    self.type = type
    self.player = player
  def __repr__(self):
    return "{name} Statistics\n------\nLevel: {level}\nHealth: {health}/{max_health}\nType: {type}\nFainted: {faint}\n".format(name=self.name,level=self.level,health=self.health,max_health=self.max_health,type=self.type,faint=self.is_knocked_out)
  def healthBar(self):
    x = round((self.health/self.max_health * 100)/5)
    if x < 19.1:
      y = 20 - x
      bar = "[" + "=" * x + "/" + y * "_" + "]"
    else:
      bar = "[" + "=" * x + "]"
    return bar
class Trainer:
  name = ""
  items = {}
  pokemon = []
  money = 500
  wins = 0
  def __init__(self, name, items, pokemon):
    self.name = name
    self.items = items
    self.pokemon = pokemon
  def __repr__(self):
    return "{name}'s Trainer ID:\nItems: {items}\nPokemon: {pokemon}\nMoney: ${money}\nWins: {wins}\n".format(name=self.name,items=self.items,pokemon=self.pokemon, money=self.money, wins=self.wins)
  def useItem(self):
    while True:
      print("Item List")
      for i in list(self.items.keys()):
        print(self.items[i], i)
      print("\nType EXIT to leave")
      x = input("Which item would you like to use?\n> ")
      if x.lower() == "potion":
        if self.items["potion"] < 1:
          print("You don't have any potions.")
          input("Press ENTER to continue... ")
          break
        Pokemon1[0].health += 20
        if Pokemon1[0].health > Pokemon1[0].max_health:
          Pokemon1[0].health = Pokemon1[0].max_health
        self.items["potion"] -= 1
        print("{poke} has healed 20 hp!".format(poke=self.pokemon[0]))
        clearTerminal(True)
        break
      if x.lower() == "super potion":
        if self.items["super potion"] < 1:
          print("You don't have any Super Potions.")
          input("Press ENTER to continue... ")
          break
        Pokemon1[0].health += 50
        if Pokemon1[0].health > Pokemon1[0].max_health:
          Pokemon1[0].health = Pokemon1[0].max_health
        self.items["super potion"] -= 1
        print("{poke} has healed 50 hp!".format(poke=self.pokemon[0]))
        clearTerminal(True)
        break
      elif x.lower() == "exit":
        break
      clearTerminal()
  def win(self):
    money_earned = random.randint(100, 460)
    self.money += money_earned
    self.wins += 1
    print("You earned ${money} for winning the battle".format(money=money_earned))
  def pokeShop(self):
    x = ""
    while x != "exit":
        clearTerminal()
        print("Welcome to the PokeShop!\nHere is a list of items for sale:\n$300 - Potion\n$700 - Super Potion\n")
        x = input("(type exit to leave)\nYou have ${money}\nWhat would you like to buy?\n> ".format(money=self.money)).lower()
        if x == "exit":
            print("Thanks for shopping with us! We hope to see you next time!")
            clearTerminal(True)
            break
        elif x == "potion":
            while True:
                try:
                    y = int(input("How many would you like to buy? "))
                    if y < 0:
                      print("Invalid input. Quantity should be at least 1.")
                      continue
                    if y == 0:
                      break  
                    total_cost = 300 * y
                    if total_cost > self.money:
                      print("Not enough money to buy that many potions.")
                      continue
                    self.items["potion"] += y
                    self.money -= total_cost
                    print(f"You have purchased {y} potions for ${total_cost}.")
                    print(f"Remaining money: ${self.money}")
                    clearTerminal(True)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue
        elif x == "super potion":
          while True:
              try:
                  y = int(input("How many would you like to buy? "))
                  if y < 0:
                    print("Invalid input. Quantity should be at least 1.")
                    continue
                  if y == 0:
                    break  
                  total_cost = 700 * y
                  if total_cost > self.money:
                    print("Not enough money to buy that many potions.")
                    continue
                  self.items["super potion"] += y
                  self.money -= total_cost
                  print(f"You have purchased {y} super potions for ${total_cost}.")
                  print(f"Remaining money: ${self.money}")
                  clearTerminal(True)
                  break
              except ValueError:
                  print("Invalid input. Please enter a valid number.")
                  continue
def clearTerminal(x = False):
  if x is True:
    input("Press ENTER to continue... ")
  os.system('cls' if os.name == 'nt' else 'clear')


# End of classes
name1 = input("What is your name?\n> ")
pokemon_names = {"Pikachu":["Lightning",["Scratch", "Thunder Shock", "Thunder Wave"]],
                "Charmander":["Fire", ["Scratch", "Ember", "Fire Wheel"]],
                "Eevee":["Normal",["Scratch", "Tackle"]],
                "Squirtle":["Water", ["Scratch", "Water Gun"]],
                "Psyduck":["Water", ["Scratch", "Water Gun", "Confusion"]],
                 "Mudkip":["Water", ["Tackle", "Water Gun", "Rock Smash"]],
                 "Bulbasaur":["Grass", ["Tackle", "Vine Whip", "Razor Leaf"]],
                 "Litten":["Fire",["Scratch", "Ember", "Lick"]],
                 "Froakie": ["Water", ["Pound", "Water Gun", "Quick Attack"]],
                "Mewtwo": ["Physic", ["Confusion", "Swift"]],
                 "Moltres": ["Fire/Flying", ["Gust", "Ember", "Wing Attack"]]
                }


trainers = ["Ash Ketchup", "Misty Williams", "Brock Stone", "Serena Smith", "Dawn Johnson", "May Anderson", "Cynthia Davis", "Iris Brown", "Gary Taylor", "Lance Martinez", "Professor Oak"]


clearTerminal()
for i in [i for i in pokemon_names.keys() if i != "Mewtwo"]:
  print(i)
pokeselect = input("Choose a Pokemon out of the list above: ").title()
while all(p != pokeselect for p in pokemon_names):
  pokeselect = input("Invalid choice, try again: ")

Player1 = Trainer(name1, {"potion": 3, "super potion": 1}, [pokeselect])
Pokemon1 = []
for i in Player1.pokemon:
  Pokemon1.append(Pokemon(i, pokemon_names[i][0], True))
clearTerminal()
while True:
  while True:
    try:
        selecter = int(input("Options List:\n1) Check Your Trainer ID\n2) Battle a Trainer\n3) Check your party\n4) Enter PokeShop \n5) Quit Game\n> "))
        break  # Break out of the loop if the input is valid
    except ValueError:
      clearTerminal()
      print("Invalid input. Please enter a valid number.")
  if selecter == 1:
    clearTerminal()
    print(Player1)
    clearTerminal(True)
  elif selecter == 2:
    clearTerminal()
    trainerName = random.choice(trainers)
    pokeselect2 = random.choice([i for i in pokemon_names.keys() if i != "Mewtwo"])
    Player2 = Trainer(trainerName, {"potion": 2, "pokeball": 1}, [pokeselect2])

      # print(Pokemon1[0])
    Pokemon2 = []
    for i in Player2.pokemon:
      Pokemon2.append(Pokemon(i, pokemon_names[i][0], False))
    # print(Pokemon2[0])
    game_end = False
    print("Trainer {name} wishes to battle you!\n- They have the {type} Pokemon, {pokename}".format(name=Player2.name,type=Pokemon2[0].type.lower(),pokename=Pokemon2[0].name))
    while game_end == False:
      print("\nOponnent's {pokename} HP: {hp}/{maxhp}".format(pokename=Pokemon2[0].name, hp=Pokemon2[0].health, maxhp=Pokemon2[0].max_health))
      print(Pokemon2[0].healthBar())
      while True:
        try:
          selecter2 = int(input("\nSelect an option:\n1) Fight\n2) Bag\n3) Forfeit\n________________\n\nYour {pokename}'s HP: {hp}/{maxhp}\n{healthbar}\n> ".format(pokename=Pokemon1[0].name, hp=Pokemon1[0].health, maxhp=Pokemon1[0].max_health, healthbar=Pokemon1[0].healthBar())))
          break
        except ValueError:
          clearTerminal()
          print("Invalid input. Please enter a valid number.")
      clearTerminal()
      if selecter2 == 1:
        clearTerminal()
        
        move = ""
        while move != "Exit":
          print("Movelist:\n")
          for i in pokemon_names[Pokemon1[0].name][1]:
            print(i)
          move = input("\nChoose a move to use or EXIT:\n> ").title()
          # print(Pokemon2)
          # print(Player2)
          
          while move in pokemon_names[Pokemon1[0].name][1]:
            clearTerminal()
            Pokemon1[0].damage(Pokemon2[0], move)
            if Pokemon2[0].is_knocked_out == True:
              game_end = True
              Pokemon1[0].level_up()
              print("You have defeated Trainer {name}\nYour {pokename} has leveled up to lvl. {level}!".format(name=Player2.name, pokename=Pokemon1[0].name, level=Pokemon1[0].level))
              Player1.win()
              Pokemon2.pop(0)
            else:
              input("Press ENTER to continue... ")
              print("\n-------------------------\n")
              Pokemon2[0].damage(Pokemon1[0], random.choice(pokemon_names[Pokemon2[0].name][1]))
            if Pokemon1[0].is_knocked_out:
              game_end = True
              print('{name}: "My {poke} always wins!"'.format(name=Player2.name, poke=Pokemon2[0].name))
              Pokemon2.pop(0)
              Pokemon1[0].heal()
            move = "Exit"
            input("Press ENTER to continue... ")

            break
          clearTerminal()
      elif selecter2 == 2:
        Player1.useItem()
        clearTerminal()
      elif int(selecter2) == 3:
        Pokemon2.pop(0)
        break
  elif selecter == 3:
    clearTerminal()
    print(Pokemon1[0])
    clearTerminal(True)
  elif selecter == 4:
    Player1.pokeShop()
  elif selecter == 5:
    clearTerminal()
    print("Quit Succesfully")
    quit()

