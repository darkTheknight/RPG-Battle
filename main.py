from game import Person, Bcolors
from magic import Spell
from inventory import Item

print("\n\n")
print("NAME             HP                            MP")
print("                 -------------------           ---------------")
print("Valos:   460/460|                   |    65/65|               |")

print("                 -------------------           ---------------")
print("Valos:   460/460|                   |    65/65|               |")

print("                 -------------------           ---------------")
print("Valos:   460/460|                   |    65/65|               |")

# create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "Potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores one party member MP/HP", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's member MP/HP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2},
                {"item": grenade, "quantity": 5}]
# Instantiate people
player1 = Person("Valos", 460, 65, 60, 34, player_spells, player_items)  # list items are magic items
player2 = Person("Nick", 460, 65, 60, 34, player_spells, player_items)  # list items are magic items
player3 = Person("Robot", 460, 65, 60, 34, player_spells, player_items)  # list items are magic items
enemy = Person("", 1200, 65, 45, 25, [], [])  # enemy does not have magic items

players = [player1, player2, player3]

running = True
i = 0
print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)

while running:
    print(
        "=============================================================================================================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1

        if magic_choice == -1:
            continue

        # magic_dmg = player.generate_spell_damage(magic_choice)
        # spell = player.get_spell_name(magic_choice)
        # cost = player.get_spell_cost(magic_choice)

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(Bcolors.FAIL + "\nNot enough MP\n" + Bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)
        if spell.type == "white":
            player.heal(magic_dmg)
            print(Bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + Bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(Bcolors.OKBLUE + "\n" + spell.name, "deals", str(magic_dmg), "points of damage." + Bcolors.ENDC)
    elif index == 2:
        player.choose_item()
        item_choice = int(input("choose item: ")) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]["item"]

        if player.items[item_choice]["quantity"] == 0:
            print(Bcolors.FAIL + "\n" + "None left..." + Bcolors.ENDC)
            continue

        player.items[item_choice]["quantity"] -= 1

        if item.type == "potion":
            player.heal(item.prob)
            print(Bcolors.OKGREEN, "\n" + item.name, "heals for", str(item.prob), "HP" + Bcolors.ENDC)

        elif item.type == "elixer":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(Bcolors.OKGREEN + "\n" + item.name + "fully restores HP/MP" + Bcolors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prob)
            print(Bcolors.FAIL + "\n" + item.name + " deals", str(item.prob), "points of damage" + Bcolors.ENDC)

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "\n")
    # print("=============================================================================================================")
    print("Enemy HP:", Bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Bcolors.ENDC)
    print("Your HP:" + Bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + Bcolors.ENDC)
    print("Your MP:" + Bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + Bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(Bcolors.OKGREEN + "You Won!" + Bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Bcolors.OKGREEN + "Your Enemy Won!" + Bcolors.ENDC)
        running = False
    # print("You chose", player.get_spell_name(int(choice)))
    # running = False
